import json
import time
import importlib

import pytest

from misttests.config import MIST_URL
from misttests.integration.api.helpers import assert_response_found
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']
REDIRECT_OPERATIONS = ['ssh', 'console']

resource_name = 'NetworksController'.replace('Controller', '').lower()
resource_name_singular = resource_name.strip('s')
try:
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{resource_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True
setup_data = {}


@pytest.fixture(autouse=True)
def after_test(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    test_operation = method_name.replace('test_', '')
    callback = setup_data.get(test_operation, {}).get('callback')
    if callable(callback):
        assert callback()
    else:
        sleep = setup_data.get(test_operation, {}).get('sleep')
        if sleep:
            time.sleep(sleep)


class TestNetworksController:
    """NetworksController integration test stubs"""

    def test_get_network(self, pretty_print, owner_api_token):
        """Test case for get_network

        Get network
        """
        query_string = setup_data.get('get_network', {}).get('query_string') or [('only', 'id'),
                        ('deref', 'auto')]
        uri = MIST_URL + '/api/v2/networks/{network}'.format(
            network=setup_data.get('get_network', {}).get('network') or setup_data.get('network') or 'my-network')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'get_network' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')

    def test_list_networks(self, pretty_print, owner_api_token):
        """Test case for list_networks

        List networks
        """
        query_string = setup_data.get('list_networks', {}).get('query_string') or [('cloud', '0194030499e74b02bdf68fa7130fb0b2'),
                        ('search', 'cinet3'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', 56),
                        ('only', 'id'),
                        ('deref', 'auto'),
                        ('at', '2021-07-21T17:32:28Z')]
        uri = MIST_URL + '/api/v2/networks'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        if 'list_networks' in REDIRECT_OPERATIONS:
            assert_response_found(response)
        else:
            assert_response_ok(response)
        print('Success!!!')


if hasattr(_setup_module, 'TEST_METHOD_ORDERING'):
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestNetworksController, method_name)
        setattr(TestNetworksController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestNetworksController):
        attr = getattr(TestNetworksController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestNetworksController, key, pytest.mark.order('last')(attr))

if SETUP_MODULE_EXISTS:
    # Add setup and teardown methods to test class
    class_setup_done = False

    @pytest.fixture(scope='class')
    def setup(owner_api_token):
        global class_setup_done
        if class_setup_done:
            yield
        else:
            global setup_data
            setup_data = _setup_module.setup(owner_api_token) or {}
            yield
            _setup_module.teardown(owner_api_token, setup_data)
            class_setup_done = True
    TestNetworksController = pytest.mark.usefixtures('setup')(
        TestNetworksController)
