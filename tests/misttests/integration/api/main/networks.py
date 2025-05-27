from misttests.integration.api.helpers import *
from misttests import config
from misttests.config import safe_get_var
import pytest

############################################################################
#                             Unit Testing                                 #
############################################################################


def test_list_networks_wrong_cloud_id(pretty_print, mist_api_v1, owner_api_token):
    response = mist_api_v1.list_networks(api_token=owner_api_token,
                                       cloud_id='dummy').get()
    assert_response_not_found(response)
    print("Success!!!")


def test_list_networks_wrong_api_token(pretty_print, mist_api_v1):
    response = mist_api_v1.list_networks(api_token='dummy',
                                       cloud_id='dummy').get()
    assert_response_unauthorized(response)
    print("Success!!!")


def test_list_networks_no_api_token(pretty_print, mist_api_v1):
    response = mist_api_v1.list_networks(api_token='',
                                       cloud_id='dummy').get()
    assert_response_unauthorized(response)
    print("Success!!!")


############################################################################
#                          Functional Testing                              #
############################################################################

@pytest.mark.incremental
class TestNetworksFunctionality:
