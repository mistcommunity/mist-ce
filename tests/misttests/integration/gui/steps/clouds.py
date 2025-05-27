import json

from behave import step

from selenium.webdriver.common.by import By

from misttests.config import safe_get_var
from time import time
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException

from misttests.integration.gui.steps.utils import safe_get_element_text, expand_shadow_root, get_page_element, has_finished_loading, add_credit_card_if_needed

from misttests.integration.gui.steps.forms import set_value_to_field, get_add_form
from misttests.integration.gui.steps.forms import clear_input_and_send_keys

from misttests.integration.gui.steps.buttons import clicketi_click
from misttests.integration.gui.steps.buttons import click_button_from_collection

from misttests.integration.gui.steps.dialog import get_dialog


def set_gce_creds(context):
    project_id = safe_get_var('clouds/gce/mist-dev-tests', 'projectId', context.mist_config['CREDENTIALS']['GCE']['projectId'])
    private_key = safe_get_var('clouds/gce/mist-dev-tests', 'privateKeyDetailed', context.mist_config['CREDENTIALS']['GCE']['privateKeyDetailed'])
    context.execute_steps('''
            Then I set the value "%s" to field "Name" in the "cloud" add form
            Then I set the value "%s" to field "Project ID" in the "cloud" add form
            Then I set the value "%s" to field "Private Key" in the "cloud" add form
            And I click the "Enable DNS support" toggle button in the "cloud" add form
        ''' % ('Google Cloud', project_id, json.dumps(private_key).replace('"', '\"')))


def set_rackspace_creds(context):
    region = safe_get_var('clouds/rackspace', 'region', context.mist_config['CREDENTIALS']['RACKSPACE']['region'])
    username = safe_get_var('clouds/rackspace', 'username', context.mist_config['CREDENTIALS']['RACKSPACE']['username'])
    api_key = safe_get_var('clouds/rackspace', 'apikey', context.mist_config['CREDENTIALS']['RACKSPACE']['apikey'])
    context.execute_steps('''
        Then I open the "Region" dropdown in the "cloud" add form
        And I wait for 1 seconds
        When I click the "%s" button in the "Region" dropdown in the "cloud" add form
        Then I set the value "Rackspace" to field "Name" in the "cloud" add form
        Then I set the value "%s" to field "Username" in the "cloud" add form
        Then I set the value "%s" to field "API Key" in the "cloud" add form
    ''' % (region, username, api_key))


def set_aws_creds(context):
    api_key = safe_get_var('clouds/aws', 'apikey', context.mist_config['CREDENTIALS']['EC2']['apikey'])
    api_secret = safe_get_var('clouds/aws', 'apisecret', context.mist_config['CREDENTIALS']['EC2']['apisecret'])
    region = safe_get_var('clouds/aws', 'region_name', context.mist_config['CREDENTIALS']['EC2']['region_name'])
    context.execute_steps('''
        Then I open the "Region" dropdown in the "cloud" add form
        And I wait for 1 seconds
        When I click the "%s" button in the "Region" dropdown in the "cloud" add form
        And I wait for 1 seconds
        Then I set the value "Amazon Web Services" to field "Name" in the "cloud" add form
        And I set the value "%s" to field "API Key" in the "cloud" add form
        And I set the value "%s" to field "API Secret" in the "cloud" add form
    ''' % (region, api_key, api_secret))


def set_aws_no_images_creds(context):
    api_key = safe_get_var('clouds/aws_no_images', 'apikey', context.mist_config['CREDENTIALS']['EC2']['apikey'])
    api_secret = safe_get_var('clouds/aws_no_images', 'apisecret', context.mist_config['CREDENTIALS']['EC2']['apisecret'])
    region = safe_get_var('clouds/aws_no_images', 'region_name', context.mist_config['CREDENTIALS']['EC2']['region_name'])
    context.execute_steps('''
        Then I open the "Region" dropdown in the "cloud" add form
        And I wait for 1 seconds
        When I click the "%s" button in the "Region" dropdown in the "cloud" add form
        And I wait for 1 seconds
        Then I set the value "Amazon Web Services" to field "Name" in the "cloud" add form
        And I set the value "%s" to field "API Key" in the "cloud" add form
        And I set the value "%s" to field "API Secret" in the "cloud" add form
    ''' % (region, api_key, api_secret))


def set_linode_creds(context):
    api_key = safe_get_var('clouds/linode', 'api_key_new', context.mist_config['CREDENTIALS']['LINODE']['apikey'])
    context.execute_steps('Then I set the value "%s" to field "API Key" in '
                          'the "cloud" add form' % api_key)


def set_do_creds(context):
    token = safe_get_var('clouds/digitalocean', 'token', context.mist_config['CREDENTIALS']['DIGITALOCEAN']['token'])
    context.execute_steps('Then I set the value "%s" to field "Token" in the '
                          '"cloud" add form' % token)


def set_docker_creds(context):
    if context.mist_config['LOCAL']:
        host = context.mist_config['LOCAL_DOCKER']
        port = '2375'
        context.execute_steps('''
                Then I set the value "Docker" to field "Name" in the "cloud" add form
                Then I set the value "%s" to field "Host" in the "cloud" add form
                Then I set the value "%s" to field "Port" in the "cloud" add form
        ''' % (host, port))
    else:
        host = safe_get_var('clouds/dockerhost', 'host', context.mist_config['CREDENTIALS']['DOCKER']['host'])
        port = safe_get_var('clouds/dockerhost', 'port', context.mist_config['CREDENTIALS']['DOCKER']['port'])
        context.execute_steps('''
                Then I set the value "Docker" to field "Name" in the "cloud" add form
                Then I set the value "%s" to field "Host" in the "cloud" add form
                Then I set the value "%s" to field "Port" in the "cloud" add form
            ''' % (host, port))

        certificate = safe_get_var('clouds/dockerhost', 'tlsCert', context.mist_config['CREDENTIALS']['DOCKER']['tlsCert'])
        key = safe_get_var('clouds/dockerhost', 'tlsKey', context.mist_config['CREDENTIALS']['DOCKER']['tlsKey'])
        ca = safe_get_var('clouds/dockerhost', 'tlsCaCert', context.mist_config['CREDENTIALS']['DOCKER']['tlsCaCert'])

        set_value_to_field(context, key, 'key', 'cloud', 'add')
        set_value_to_field(context, certificate, 'certificate', 'cloud', 'add')
        set_value_to_field(context, ca, 'ca certificate', 'cloud', 'add')


def set_equinix_metal_creds(context):
    api_key = safe_get_var('clouds/packet', 'apikey', context.mist_config['CREDENTIALS']['EQUINIX METAL']['apikey'])
    context.execute_steps('Then I set the value "%s" to field "API Key" in the '
                          '"cloud" add form' % api_key)


def set_openstack_creds(context):
    password = safe_get_var('clouds/vexxhost', 'password', context.mist_config['CREDENTIALS']['OPENSTACK']['password'])
    context.execute_steps('''
            Then I set the value "OpenStack" to field "Name" in the "cloud" add form
            Then I set the value "%s" to field "Username" in the "cloud" add form
            Then I set the value "%s" to field "Auth Url" in the "cloud" add form
            Then I set the value "%s" to field "Tenant Name" in the "cloud" add form
            Then I set the value "%s" to field "Region" in the "cloud" add form
        ''' % (safe_get_var('clouds/vexxhost', 'user', context.mist_config['CREDENTIALS']['OPENSTACK']['user']),
               safe_get_var('clouds/vexxhost', 'authUrl', context.mist_config['CREDENTIALS']['OPENSTACK']['authUrl']),
               safe_get_var('clouds/vexxhost', 'tenant', context.mist_config['CREDENTIALS']['OPENSTACK']['tenant']),
               safe_get_var('clouds/vexxhost', 'region', context.mist_config['CREDENTIALS']['OPENSTACK']['region']),
               ))

    set_value_to_field(context, password, 'Password', 'cloud', 'add')


def set_hostvirtual_creds(context):
    api_key = safe_get_var('clouds/hostvirtual', 'api_key', context.mist_config['CREDENTIALS']['HOSTVIRTUAL']['api_key'])
    context.execute_steps('Then I set the value "%s" to field "API Key" in '
                          '"cloud" add form' % api_key)


def set_vultr_creds(context):
    api_key = safe_get_var('clouds/vultr', 'apikey', context.mist_config['CREDENTIALS']['VULTR']['apikey'])
    context.execute_steps('Then I set the value "%s" to field "API Key" in the "cloud" add form' % api_key)


def set_aliyun_creds(context):
    context.execute_steps('''
                        Then I open the "Region" dropdown in the "cloud" add form
                        Then I wait for 2 seconds
                        Then I click the "US West 1 (Silicon Valley)" button in the "Region" dropdown in the "cloud" add form
                        Then I wait for 1 seconds
                        Then I set the value "Alibaba Cloud" to field "Name" in the "cloud" add form
                        Then I set the value "%s" to field "API Key" in the "cloud" add form
                        Then I set the value "%s" to field "API Secret" in the "cloud" add form
                    ''' % (safe_get_var('clouds/aliyun', 'apikey', context.mist_config['CREDENTIALS']['ALIYUN']['apikey']),
                           safe_get_var('clouds/aliyun', 'apisecret', context.mist_config['CREDENTIALS']['ALIYUN']['apisecret'])))

def set_azure_arm_creds(context):
    context.execute_steps('''
                    Then I set the value "Microsoft Azure" to field "Name" in the "cloud" add form
                    Then I set the value "%s" to field "Tenant ID" in the "cloud" add form
                    Then I set the value "%s" to field "Subscription ID" in the "cloud" add form
                    Then I set the value "%s" to field "Client Key" in the "cloud" add form
                    Then I set the value "%s" to field "Client Secret" in the "cloud" add form
                ''' % (safe_get_var('clouds/azure_arm', 'tenant_id', context.mist_config['CREDENTIALS']['AZURE_ARM']['tenant_id']),
                       safe_get_var('clouds/azure_arm', 'subscription_id', context.mist_config['CREDENTIALS']['AZURE_ARM']['subscription_id']),
                       safe_get_var('clouds/azure_arm', 'client_key', context.mist_config['CREDENTIALS']['AZURE_ARM']['client_key']),
                       safe_get_var('clouds/azure_arm', 'client_secret', context.mist_config['CREDENTIALS']['AZURE_ARM']['client_secret']),))


def set_kvm_creds(context):
    context.execute_steps('''
                    Then I set the value "KVM" to field "Name" in the "cloud" add form
                    Then I set the value "%s" to field "KVM hostname or IP" in the "cloud" add form
                    And I wait for 1 seconds
                    And I open the "SSH Key" dropdown in the "cloud" add form
                    And I wait for 2 seconds
                    And I click the "KVMKEY" button in the "SSH Key" dropdown in the "cloud" add form
                    And I wait for 1 seconds
                ''' % (safe_get_var('clouds/kvm', 'hostname', context.mist_config['CREDENTIALS']['KVM']['hostname']),))


def set_other_server_creds(context):
    hostname = safe_get_var('clouds/other_server', 'hostname', context.mist_config['CREDENTIALS']['KVM']['hostname'])
    context.mist_config['bare_metal_host'] = hostname
    context.execute_steps('''
                    Then I set the value "Bare Metal" to field "Cloud Name" in the "cloud" add form
                    Then I set the value "%s" to field "Hostname" in the "cloud" add form
                    And I wait for 1 seconds
                    And I open the "SSH Key" dropdown in the "cloud" add form
                    And I wait for 2 seconds
                    And I click the "KVMKEY" button in the "SSH Key" dropdown in the "cloud" add form
                    And I wait for 1 seconds
                ''' % hostname)


def set_vsphere_creds(context):
    context.execute_steps('''
                Then I set the value "%s" to field "Username" in the "cloud" add form
                Then I set the value "%s" to field "Password" in the "cloud" add form
                Then I set the value "%s" to field "Hostname" in the "cloud" add form
            ''' % (safe_get_var('clouds/vsphere', 'username', context.mist_config['CREDENTIALS']['VSPHERE']['username']),
                   safe_get_var('clouds/vsphere', 'password', context.mist_config['CREDENTIALS']['VSPHERE']['password']),
                   safe_get_var('clouds/vsphere', 'host', context.mist_config['CREDENTIALS']['VSPHERE']['host']),))
    ca = safe_get_var('clouds/vsphere', 'ca_cert_file', context.mist_config['CREDENTIALS']['VSPHERE']['ca_cert'])
    set_value_to_field(context, ca, 'ca certificate', 'cloud', 'add')


def set_onapp_creds(context):
    context.execute_steps('''
                Then I set the value "%s" to field "Username" in the "cloud" add form
                Then I set the value "%s" to field "Password" in the "cloud" add form
                Then I set the value "%s" to field "Host" in the "cloud" add form
                And I click the "Verify SSL certificate" toggle button in the "cloud" add form
            ''' % (safe_get_var('clouds/onapp', 'username', context.mist_config['CREDENTIALS']['ONAPP']['username']),
                   safe_get_var('clouds/onapp', 'apikey', context.mist_config['CREDENTIALS']['ONAPP']['apikey']),
                   safe_get_var('clouds/onapp', 'host', context.mist_config['CREDENTIALS']['ONAPP']['host']),))


def set_second_packet_creds(context):
    api_key = safe_get_var('clouds/packet_2', 'apikey', context.mist_config['CREDENTIALS']['PACKET_2']['apikey'])
    context.execute_steps('Then I set the value "%s" to field "API Key" in '
                          '"cloud" edit form' % api_key)


def set_maxihost_creds(context):
    api_key = safe_get_var('clouds/maxihost', 'token', context.mist_config['CREDENTIALS']['MAXIHOST']['token'])
    context.execute_steps('''
                Then I set the value "%s" to field "API token" in the "cloud" add form
            ''' % api_key)

def set_kubevirt_creds(context):
    context.execute_steps('''
                Then I set the value "%s" to field "Hostname or IP" in the "cloud" add form
                Then I set the value "%s" to field "Port" in the "cloud" add form
            ''' % (safe_get_var('clouds/kubevirt', 'host', context.mist_config['CREDENTIALS']['KUBEVIRT']['host']),
                   safe_get_var('clouds/kubevirt', 'port', context.mist_config['CREDENTIALS']['KUBEVIRT']['port']),
            ))

    ca = safe_get_var('clouds/kubevirt', 'tlsCaCert', context.mist_config['CREDENTIALS']['KUBEVIRT']['tlsCaCert'])
    if ca:
        set_value_to_field(context, ca, 'ca certificate', 'cloud', 'add')
    cert = safe_get_var('clouds/kubevirt', 'cert', context.mist_config['CREDENTIALS']['KUBEVIRT']['cert'])
    if cert:
        set_value_to_field(context, cert, 'User Certificate', 'cloud', 'add')
    key = safe_get_var('clouds/kubevirt', 'key', context.mist_config['CREDENTIALS']['KUBEVIRT']['key'])
    if key:
        set_value_to_field(context, key, 'Private Key', 'cloud', 'add')



def set_lxd_creds(context):
    context.execute_steps('''
                Then I set the value "%s" to field "Host" in the "cloud" add form
            ''' % (safe_get_var('clouds/lxd', 'host', context.mist_config['CREDENTIALS']['LXD']['host']),
    ))
    key = safe_get_var('clouds/lxd', 'tlsKey', context.mist_config['CREDENTIALS']['LXD']['tlsKey'])
    cert = safe_get_var('clouds/lxd', 'tlsCert', context.mist_config['CREDENTIALS']['LXD']['tlsCert'])
    ca = safe_get_var('clouds/lxd', 'ca', context.mist_config['CREDENTIALS']['LXD']['ca'])
    set_value_to_field(context, key, 'client private key', 'cloud', 'add')
    set_value_to_field(context, cert, 'client certificate', 'cloud', 'add')
    set_value_to_field(context, ca, 'ca certificate', 'cloud', 'add')

def set_g8_creds(context):
    api_key = safe_get_var('clouds/gig_g8', 'api_key', context.mist_config['CREDENTIALS']['GIG_G8']['api_key'])
    set_value_to_field(context, api_key, 'API key (JWT)', 'cloud', 'add')
    context.execute_steps('''
                Then I set the value "%s" to field "API url" in the "cloud" add form
                Then I set the value "%s" to field "User ID" in the "cloud" add form
            ''' % (safe_get_var('clouds/gig_g8', 'url', context.mist_config['CREDENTIALS']['GIG_G8']['url']),
                   safe_get_var('clouds/gig_g8', 'user_id', context.mist_config['CREDENTIALS']['GIG_G8']['user_id']),))

def set_cloudsigma_creds(context):
    email = safe_get_var('clouds/cloudsigma', 'email', context.mist_config['CREDENTIALS']['CLOUDSIGMA']['email'])
    password = safe_get_var('clouds/cloudsigma', 'password', context.mist_config['CREDENTIALS']['CLOUDSIGMA']['password'])
    context.execute_steps('''
                        Then I open the "Region" dropdown in the "cloud" add form
                        Then I wait for 2 seconds
                        Then I click the "San Jose, CA" button in the "Region" dropdown in the "cloud" add form
                        Then I wait for 1 seconds
                        Then I set the value "CloudSigma" to field "Name" in the "cloud" add form
                        Then I set the value "%s" to field "Username" in the "cloud" add form
                        Then I set the value "%s" to field "Password" in the "cloud" add form
                    ''' % (email, password))

@step('I use my second AWS credentials')
def set_second_aws_creds(context):
    context.execute_steps('''
                Then I set the value "%s" to field "API KEY" in the "Edit Credentials" dialog
                Then I set the value "%s" to field "API SECRET" in the "Edit Credentials" dialog
            ''' % (safe_get_var('clouds/aws', 'apikey', context.mist_config['CREDENTIALS']['AWS_2']['apikey']),
                   safe_get_var('clouds/aws', 'apisecret', context.mist_config['CREDENTIALS']['AWS_2']['apisecret']),))


cloud_creds_dict = {
    "google cloud": set_gce_creds,
    "rackspace": set_rackspace_creds,
    "ibm cloud": set_ibm_clouds_creds,
    "amazon web services": set_aws_creds,
    "amazon web services no images": set_aws_no_images_creds,
    "linode": set_linode_creds,
    "digitalocean": set_do_creds,
    "docker": set_docker_creds,
    "equinix metal": set_equinix_metal_creds,
    "openstack": set_openstack_creds,
    "hostvirtual": set_hostvirtual_creds,
    "vultr": set_vultr_creds,
    "microsoft azure": set_azure_arm_creds,
    "kvm": set_kvm_creds,
    "other server": set_other_server_creds,
    "vmware vsphere": set_vsphere_creds,
    "onapp": set_onapp_creds,
    "alibaba cloud": set_aliyun_creds,
    "maxihost": set_maxihost_creds,
    "kubevirt": set_kubevirt_creds,
    "lxd": set_lxd_creds,
    "g8": set_g8_creds,
    "cloudsigma": set_cloudsigma_creds,
}


cloud_second_creds_dict = {
    "aws": set_second_aws_creds
}


@step('I select the "{provider}" provider')
def select_provider_in_cloud_add_form(context, provider):
    form_element = get_add_form(context, 'cloud')
    form_shadow = expand_shadow_root(context, form_element)
    # if in mist-hs repo and user has not provided mist
    # with a billing card, then a cc-required dialog appears
    add_credit_card_if_needed(context, form_shadow)
    provider_name = provider.lower()
    providers_lists = form_shadow.find_elements(By.CSS_SELECTOR, 'paper-listbox')
    providers = []
    for provider_type in providers_lists:
        providers += provider_type.find_elements(By.CSS_SELECTOR, 'paper-item')

    for p in providers:
        if safe_get_element_text(p).replace("\n", "").lower().strip() == provider_name:
            clicketi_click(context, p)
            return


@step('I use my "{provider}" credentials')
def cloud_creds(context, provider):
    provider = provider.strip().lower()
    if provider not in list(cloud_creds_dict.keys()):
        raise Exception("Unknown cloud provider", provider)
    cloud_creds_dict.get(provider)(context)


@step('I use my second "{provider}" credentials in cloud edit form')
def cloud_second_creds(context, provider):
    provider = provider.strip().lower()
    if provider not in list(cloud_second_creds_dict.keys()):
        raise Exception("Unknown cloud provider")
    cloud_second_creds_dict.get(provider)(context)


@step('I should have {clouds} clouds added')
def check_error_message(context, clouds):
    page_dashboard = get_page_element(context, 'dashboard')
    page_dashboard_shadow = expand_shadow_root(context, page_dashboard)
    cloud_chips = page_dashboard_shadow.find_elements(By.CSS_SELECTOR, 'cloud-chip')
    if len(cloud_chips) == int(clouds):
        return
    else:
        assert False, "There are %s clouds added, not %s"%(len(cloud_chips), clouds)


def find_cloud(context, cloud_name):
    page_dashboard = get_page_element(context, 'dashboard')
    page_dashboard_shadow = expand_shadow_root(context, page_dashboard)
    if page_dashboard_shadow is None:
        sleep(1)
        page_dashboard_shadow = expand_shadow_root(context, page_dashboard)

    end_time = time() + 10
    while time() < end_time:
        cloud_chips = page_dashboard_shadow.find_elements(By.CSS_SELECTOR, 'cloud-chip')
        if cloud_chips or has_finished_loading(context, 'clouds'):
            break
        sleep(2)

    for cloud in cloud_chips:
        if cloud.is_displayed:
            name = cloud.find_element(By.CSS_SELECTOR, '.cloud-name')
            if safe_get_element_text(name).lower().strip() == cloud_name:
                return cloud
    return None


def find_cloud_info(context, cloud_name):
    clouds = context.browser.find_elements(By.CSS_SELECTOR, 'cloud-info')
    clouds = [el for el in clouds if el.is_displayed()]
    for c in clouds:
        try:
            input_containers = c.find_elements(By.CSS_SELECTOR, '#labelAndInputContainer')
            for container in input_containers:
                text = safe_get_element_text(container.find_element(By.CSS_SELECTOR, 'label')).lower().strip()
                if text == 'name':
                    text = container.find_element(By.CSS_SELECTOR, 'input').\
                            get_attribute('value').lower().strip()
                    if text == cloud_name:
                        return c
        except NoSuchElementException:
            pass
    return None


@step('"{cloud}" cloud has been added')
def given_cloud(context, cloud):
    if find_cloud(context, cloud.lower()):
        return True

    context.execute_steps('''
        When I click the fab button in the "dashboard" page
        Then I expect the "Cloud" add form to be visible within max 5 seconds
    ''')

    if 'amazon web services no images' in cloud.lower():
        cloud_type = 'amazon web services'
    else:
        cloud_type = cloud

    context.execute_steps('''When I select the "%s" provider''' % cloud_type)

    context.execute_steps('''
        Then I expect the field "Name" in the cloud add form to be visible within max 4 seconds
        When I use my "%s" credentials
        And I focus on the button "Add Cloud" in the "cloud" add form
        And I click the button "Add Cloud" in the "cloud" add form
        And I wait for the dashboard to load
        And I scroll the clouds list into view
        Then the "%s" provider should be added within 120 seconds
    ''' % (cloud, cloud))


@step('I {action} the cloud page for "{provider}"')
def open_cloud_menu(context, action, provider):
    action = action.lower()
    if action not in ['open', 'close']:
        raise Exception('Unrecognized action')
    if action == 'open':
        cloud = find_cloud(context, provider.lower())
        assert cloud, "Provider %s is not available" % provider
        clicketi_click(context, cloud)
    cloud_info = find_cloud_info(context, provider.lower())
    if action == 'close':
        close_button = cloud_info.find_element(By.CSS_SELECTOR, '#close-btn')
        clicketi_click(context, close_button)


@step('I remove the "{provider}" cloud')
def remove_cloud(context, provider):
    cloud_info = find_cloud_info(context, provider.lower())
    assert cloud_info, "Cloud page has not been found"
    cloud_menu_buttons = cloud_info.find_elements(By.CSS_SELECTOR, 'paper-button')
    click_button_from_collection(context, 'Remove Cloud', cloud_menu_buttons)


@step('the "{cloud}" provider should be added within {seconds} seconds')
def cloud_added(context, cloud, seconds):
    end_time = time() + int(seconds)
    while time() < end_time:
        if find_cloud(context, cloud.lower()):
            return True
        sleep(2)
    assert False, '%s is not added within %s seconds' % (cloud, seconds)


@step('the "{cloud}" cloud should be removed')
def cloud_removed(context, cloud):
    if find_cloud(context, cloud.lower()):
        return False


@step('the "{cloud}" cloud should be removed within "{seconds}" seconds')
def cloud_removed(context, cloud, seconds):
    timeout = time() + int(seconds)
    while time() < timeout:
        if not find_cloud(context, cloud.lower()):
            return True
        sleep(1)
    assert False, "Cloud has not been removed after %s seconds" % seconds


@step('I ensure "{name}" cloud is enabled')
def ensure_cloud_enabled(context, name):
    cloud = find_cloud(context, name.lower())
    assert cloud, "Cloud %s has not been added" % name
    return 'offline' in cloud.get_attibute('class')


@step('I add the key needed for Other Server')
def add_key_for_provider(context):

    context.execute_steps('''
        When I visit the Keys page
        When I click the button "+"
        Then I expect the "Key" add form to be visible within max 10 seconds
        When I set the value "KVMKey" to field "Name" in the "key" add form
    ''')

    key = safe_get_var('clouds/other_server', 'key', context.mist_config['CREDENTIALS']['KVM']['key'])
    set_value_to_field(context, key, 'Private Key', 'key', 'add')

    context.execute_steps('''
        When I expect for the button "Add" in the "key" add form to be clickable within 9 seconds
        And I focus on the button "Add" in the "key" add form
        And I click the button "Add" in the "key" add form
        Then I expect the "key" page to be visible within max 7 seconds
        And I visit the Home page
        When I visit the Keys page
        Then "KVMKey" key should be present within 15 seconds
        Then I visit the Home page
        When I wait for the dashboard to load
    ''')
