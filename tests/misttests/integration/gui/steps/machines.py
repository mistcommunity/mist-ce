from behave import step, use_step_matcher
from behave import given

from time import time
from time import sleep

from selenium.webdriver.common.by import By

from random import randrange

from misttests.integration.gui.steps.utils import safe_get_element_text, get_page_element, expand_shadow_root
from misttests.integration.gui.steps.utils import get_page, clear_input_and_send_keys
from misttests.integration.gui.steps.forms import get_add_form
from misttests.integration.gui.steps.dialog import get_dialog

from misttests.integration.gui.steps.buttons import clicketi_click, click_button_from_collection

from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


comparisons = {"==": lambda x, y: x == y,
               ">": lambda x, y: x > y,
               "<": lambda x, y: x < y,
               ">=": lambda x, y: x >= y,
               "<=": lambda x, y: x <= y,
               "!=": lambda x, y: x != y,
               }

machine_states_ordering = {
    'error': 6,
    'pending': 5,
    'rebooting': 4,
    'running': 3,
    'unknown': 2,
    'suspended': 2,
    'terminated': 1,
    'undefined': 1,
    'stopped': 0
}

# this dict contains image, size and location to be tested for each provider
machine_values_dict = {
    "aws": ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-20210223", "m1.small - Small Instance", "ap-northeast-1a "],
    "digitalocean": ["Ubuntu 14.04.5 x64", "512mb", "Amsterdam 2"],
    "equinixmetal": ["Ubuntu 14.04 LTS", "Type 0 - 8GB RAM", "Amsterdam, NL"],
    "openstack": ["CoreOS", "m1.tiny", "0"],
    "rackspace": ["Ubuntu 14.04 LTS (Trusty Tahr) (PV)", "512MB Standard Instance", "0"],
    "azure": ["Ubuntu Server 14.04 LTS", "ExtraSmall (1 cores, 768 MB) ", "West Europe"],
    "docker": ["Debian Bullseye with SSH server"]
}

@step('I click the other server machine')
def click_bare_metal_machine(context):
    context.execute_steps('Then I click on list item "%s" machine' % context.mist_config['bare_metal_host'])


def set_values_to_create_machine_form(context,provider,machine_name):
    context.execute_steps('''
                Then I set the value "%s" to field "Machine Name" in the "machine" add form
                And I wait for 1 seconds
                When I open the "Image" dropdown in the "machine" add form
                And I click the "%s" button in the "Image" dropdown in the "machine" add form
                And I wait for 1 seconds
                And I open the "Key" dropdown in the "machine" add form
                And I click the "DummyKey" button in the "Key" dropdown in the "machine" add form
                And I wait for 1 seconds
            ''' % (machine_name,
                   machine_values_dict.get(provider)[0]))

    if 'digitalocean' in provider:
        context.execute_steps('''
                    When I open the "Size" drop down in the "machine" add form
                    And I click the "%s" button in the "Size" dropdown in the "machine" add form
                    When I open the "Location" drop down in the "machine" add form
                    And I click the "%s" button in the "Location" dropdown in the "machine" add form
                ''' % ( machine_values_dict.get(provider)[1],
                       machine_values_dict.get(provider)[2]))


@step('I select the proper values for "{provider}" to create the "{machine_name}" machine')
def cloud_creds(context, provider, machine_name):
    provider = provider.strip().lower()
    if provider not in list(machine_values_dict.keys()):
        raise Exception("Unknown cloud provider")
    set_values_to_create_machine_form(context, provider, machine_name)


@step('I expect for "{key}" key to appear within max {seconds} seconds')
def key_appears(context, key, seconds):
    if context.mist_config.get(key):
        key_name = context.mist_config.get(key)
    timeout = time() + int(seconds)
    while time() < timeout:
        try:
            for key_in_list in context.browser.find_elements(By.CSS_SELECTOR, '.small-list-item'):
                if key_name == safe_get_element_text(key_in_list):
                    actions = ActionChains(context.browser)
                    actions.send_keys(Keys.ESCAPE)
                    actions.perform()
                    return True
                else:
                    pass
        except:
            sleep(1)
    assert False, "Key %s did not appear after %s seconds" % (key,seconds)


@step('I choose the "{name}" machine')
def choose_machine(context, name):
    if context.mist_config.get(name):
        name = context.mist_config.get(name)
    end_time = time() + 20
    while time() < end_time:
        machine = get_machine(context, name)
        if machine:
            checkbox = machine.find_element(By.CSS_SELECTOR, "mist-check")
            checkbox.click()
            return

        sleep(2)
    assert False, 'Could not choose/tick %s machine' % name


@step('I should see the "{name}" machine added within {seconds} seconds')
def assert_machine_added(context, name, seconds):
    if context.mist_config.get(name):
        name = context.mist_config.get(name)

    end_time = time() + int(seconds)
    while time() < end_time:
        machine = get_machine(context, name)
        if machine:
            return
        sleep(2)

    assert False, '%s is not added' % name


def get_machine(context, name):
    try:
        placeholder = context.browser.find_element(By.CSS_SELECTOR, "page-machines").find_element(By.CSS_SELECTOR, "#items")
        machines = placeholder.find_elements(By.CSS_SELECTOR, "vaadin-grid-table-row")

        for machine in machines:
            machine_text = safe_get_element_text(machine)
            if name in machine_text:
                return machine

        return None
    except NoSuchElementException:
        return None
    except StaleElementReferenceException:
        return None

@step('I wait for probing to finish for {seconds} seconds max')
def wait_for_loader_to_finish(context, seconds):
    rows = context.browser.find_elements(By.CSS_SELECTOR, 'tr')
    for row in rows:
        cells = row.find_elements(By.CSS_SELECTOR, 'td')
        cells_text = safe_get_element_text(cells[0])
        if cells_text == 'Last probed':
            end_time = time() + int(seconds)
            while time() < end_time:
                try:
                    cells[1].find_element(By.CSS_SELECTOR, '.ajax-loader')
                    sleep(1)
                except NoSuchElementException:
                    sleep(1)
                    return
            assert False, "Ajax loading hasn't finished after %s seconds" % seconds
    assert False, "Could not locate ajax loader"


@step('probing was successful')
def check_probing(context):
    rows = context.browser.find_elements(By.CSS_SELECTOR, 'tr')
    for row in rows:
        cells = row.find_elements(By.CSS_SELECTOR, 'td')
        cells_zero_text = safe_get_element_text(cells[0])
        if cells_zero_text == 'Last probed':
            cells_one_text = safe_get_element_text(cells[1])
            message = cells_one_text.split('\n')[0].lower()
            assert message == 'just now', "Probing of machine failed" \
                                          "(message is: %s)" % cells_one_text
            return
    assert False, "Could not find any line about probing"


@step('I give a default script for python script')
def fill_default_script(context):
    textfield = context.browser.find_element(By.CSS_SELECTOR, "#custom-plugin-script")
    textfield.clear()
    my_script ="import time\n\ntry:\n    from urllib2 import urlopen \n\n" \
               "except ImportError:\n    from urllib import urlopen\n" \
               "URL = 'https://mist.io'\n\n" \
               "TEXT = 'GOVERN YOUR CLOUDS'\nCHECK_TIMES = 10\nRESULT = -1\n\n" \
               "def read():\n    global CHECK_TIMES\n    global RESULT\n" \
               "    if CHECK_TIMES < 10:\n        CHECK_TIMES += 1\n        return RESULT\n" \
               "    CHECK_TIMES = 0\n\n    start=time.time()\n    try:\n" \
               "        nf=urlopen(URL)\n    except:\n        RESULT = -1\n" \
               "        return RESULT\n    page=nf.read()\n    end=time.time()\n" \
               "    nf.close()\n    if TEXT in page:\n        RESULT = end - start\n" \
               "    else:\n        RESULT =  -1\n    return RESULT"
    for letter in my_script:
        textfield.send_keys(letter)


@step('rule "{rule}" should be {state} in the "{page}" page')
def verify_rule_is_present(context, rule, state, page):
    found = False
    state = state.lower()
    if state not in ['present', 'absent']:
        raise Exception('Unknown state %s' % state)
    page_element = get_page(context, page)
    page_shadow = expand_shadow_root(context, page_element)
    rules = page_shadow.find_element(By.CSS_SELECTOR, 'mist-rules').text.replace('\n','').replace(' ','').lower()
    rule = rule.replace(" ", "").lower()
    if rule in rules:
        found = True
    if state == 'present' and found:
        return True
    if state == 'absent' and not found:
        return True
    assert False, "Rule %s was not %s in existing rules for the monitored machine" % (rule, state)


@step('"{key}" key should be associated with the machine "{machine}"')
def check_for_associated_key(context, key, machine):
    page = get_page(context, "machine")
    page_shadow = expand_shadow_root(context, page)
    machine_keys_class = page_shadow.find_elements(By.CSS_SELECTOR, 'div.associatedKeys > div.machine-key')
    for element in machine_keys_class:
        if safe_get_element_text(element) == key:
            return
    assert False, "The key has not been associated with the machine!"


use_step_matcher("re")
@step('"(?P<key>[A-Za-z0-9]+)" key should be associated with the machine "(?P<machine>[A-Za-z0-9 \-]+)" within (?P<seconds>[0-9]+) seconds')
def check_for_associated_key_within(context, key, machine, seconds):
    timeout = time() + int(seconds)
    page = get_page(context, "machine")
    page_shadow = expand_shadow_root(context, page)
    while time() < timeout:
        machine_keys_class = page_shadow.find_elements(By.CSS_SELECTOR, 'div.associatedKeys > div.machine-key')
        for element in machine_keys_class:
            if safe_get_element_text(element) == key:
                return
        sleep(1)
    assert False, "The key has not been associated with the machine!"


use_step_matcher("parse")
@step('I delete the associated key "{key}"')
def disassociate_key(context, key):
    _, page = get_page_element(context, "machines", "machine")
    page_shadow = expand_shadow_root(context, page)
    machine_keys_class = page_shadow.find_elements(By.CSS_SELECTOR, 'div.associatedKeys > div.machine-key')
    for element in machine_keys_class:
        if safe_get_element_text(element) == key:
            delete_btn = element.find_element(By.CSS_SELECTOR, '.delete')
            clicketi_click(context, delete_btn)
            return


@step('there should be {keys} keys associated with the machine within {seconds} seconds')
def keys_associated_with_machine(context, keys, seconds):
    timeout = time() + int(seconds)
    _, page = get_page_element(context, "machines", "machine")
    page_shadow = expand_shadow_root(context, page)
    while time() < timeout:
        machine_keys_class = page_shadow.find_elements(By.CSS_SELECTOR, 'div.associatedKeys > div.machine-key')
        associated_keys_with_machine = 0
        for element in machine_keys_class:
            try:
                element.find_element(By.CSS_SELECTOR, 'a')
                associated_keys_with_machine += 1
            except:
                pass
        if associated_keys_with_machine == int(keys):
            return
        sleep(1)
    assert False, "There are %s keys associated with the machine" % associated_keys_with_machine


@step('I set an expiration in "{exp_num}" "{exp_unit}" with a notify of "{notify_num}" "{notify_unit}" before in the "{form}"')
def set_expiration(context, exp_num, exp_unit, notify_num, notify_unit, form):
    if form == "create machine form":
        form = get_add_form(context, 'machine')
        form_shadow = expand_shadow_root(context, form)
        sub_form = form_shadow.find_element(By.CSS_SELECTOR, 'app-form')

    elif form == "expiration dialog":
        dialog = get_dialog(context, 'Edit expiration date')
        dialog_shadow = expand_shadow_root(context, dialog)
        sub_form = dialog_shadow.find_element(By.CSS_SELECTOR, 'app-form')

    sub_form_shadow = expand_shadow_root(context, sub_form)
    sub_fieldgroups = sub_form_shadow.find_elements(By.CSS_SELECTOR, 'sub-fieldgroup')
    for sub_fg in sub_fieldgroups:
        if sub_fg.text.startswith('Set expiration'):
            sub_fieldgroup = sub_fg
            break
        if sub_fg.get_attribute('id') == "fieldgroup-machine-expiration-edit":
            sub_fieldgroup = sub_fg
            break
    sub_field_shadow = expand_shadow_root(context, sub_fieldgroup)
    nested_app_form=sub_field_shadow.find_element(By.CSS_SELECTOR, 'app-form')
    nested_app_form_shadow = expand_shadow_root(context, nested_app_form)
    dur_fields=nested_app_form_shadow.find_elements(By.CSS_SELECTOR, 'duration-field')
    # set expiration params
    expiration=dur_fields[0]
    expiration_shadow_root=expand_shadow_root(context, expiration)
    exp_input=expiration_shadow_root.find_element(By.CSS_SELECTOR, 'paper-input')
    clear_input_and_send_keys(exp_input, exp_num)
    exp_dropdown=expiration_shadow_root.find_element(By.CSS_SELECTOR, 'paper-dropdown-menu')
    exp_dropdown.click()
    sleep(0.5)
    buttons = exp_dropdown.find_elements(By.CSS_SELECTOR, 'paper-item')
    click_button_from_collection(context, exp_unit, buttons)
    # set notify params
    notify=dur_fields[1]
    notify_shadow_root=expand_shadow_root(context, notify)
    notify_input=notify_shadow_root.find_element(By.CSS_SELECTOR, 'paper-input')
    clear_input_and_send_keys(notify_input, notify_num)
    notify_dropdown=notify_shadow_root.find_element(By.CSS_SELECTOR, 'paper-dropdown-menu')
    notify_dropdown.click()
    sleep(0.5)
    buttons = notify_dropdown.find_elements(By.CSS_SELECTOR, 'paper-item')
    click_button_from_collection(context, notify_unit, buttons)

@step('I set the expiration to "{exp_num}" "{exp_unit}" in the expiration dialog')
def set_expiration_duration_only(context, exp_num, exp_unit):
    dialog = get_dialog(context, 'Edit expiration date')
    dialog_shadow = expand_shadow_root(context, dialog)
    form = dialog_shadow.find_element(By.CSS_SELECTOR, 'app-form')
    form_shadow = expand_shadow_root(context, form)
    sub_fieldgroup = form_shadow.find_element(By.CSS_SELECTOR, 'sub-fieldgroup')
    sub_fieldgroup_shadow = expand_shadow_root(context, sub_fieldgroup)
    form2 = sub_fieldgroup_shadow.find_element(By.CSS_SELECTOR, 'app-form')
    form2_shadow = expand_shadow_root(context, form2)
    duration_field = form2_shadow.find_element(By.CSS_SELECTOR, 'duration-field')
    duration_field_shadow = expand_shadow_root(context, duration_field)
    duration_paper_input = duration_field_shadow.find_element(By.CSS_SELECTOR, 'paper-input')
    duration_paper_input_shadow = expand_shadow_root(context, duration_paper_input)
    duration_input = duration_paper_input_shadow.find_element(By.CSS_SELECTOR, 'input')
    duration_input.send_keys(Keys.CONTROL + 'a')
    sleep(0.3)
    duration_input.send_keys(Keys.BACKSPACE)
    sleep(0.3)
    duration_input.send_keys(int(exp_num))
    sleep(1)
    duration_paper_dropdown = duration_field_shadow.find_element(By.CSS_SELECTOR, 'paper-dropdown-menu')
    clicketi_click(context, duration_paper_dropdown)
    sleep(0.5)
    duration_paper_items = duration_paper_dropdown.find_elements(By.CSS_SELECTOR, 'paper-item')
    duration_item = None
    for item in duration_paper_items:
        if safe_get_element_text(item) == exp_unit:
            duration_item = item
    clicketi_click(context, duration_item)

@step('I expect to see "{duration_text}" in the expiration section of the machine page')
def check_duration_until_expiration(context, duration_text):
    _, machine_page = get_page_element(context, 'machines', 'machine')
    machine_page_shadow = expand_shadow_root(context, machine_page)
    expiration_cell = machine_page_shadow.find_element(By.CSS_SELECTOR, ".cell.expiration")
    error_msg = "Expiration time left is wrong {}".format(expiration_cell.text)
    # minutes are too short to get an accurate reading
    if duration_text == "in x minutes":
        assert 'in' in expiration_cell.text and 'minutes' in expiration_cell.text, error_msg
    else:
        assert expiration_cell.text == duration_text, error_msg

@step('I expect the field "{size_field}" to have 2 options')
def check_create_size_field(context, size_field):
    page = get_add_form(context, 'machine')
    page_shadow = expand_shadow_root(context, page)
    app_form = page_shadow.find_element(By.CSS_SELECTOR, 'app-form')
    app_form_shadow = expand_shadow_root(context, app_form)
    mist_size = app_form_shadow.find_element(By.CSS_SELECTOR, 'mist-size-field')
    mist_size_shadow = expand_shadow_root(context, mist_size)
    try:
        size_dropdown = mist_size_shadow.find_element(By.CSS_SELECTOR, 'paper-dropdown-menu')
        clicketi_click(context, size_dropdown)
        sleep(0.5)
    except NoSuchElementException:
        print("Size was expected to be a dropdown due to the constraints in place")
    sizes = size_dropdown.find_elements(By.CSS_SELECTOR, 'paper-item')
    assert len(sizes) == 2, "Expected only 2 sizes but found {}".format(len(sizes))
