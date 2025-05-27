from misttests.integration.api.helpers import *
from misttests import config
from misttests.config import safe_get_var
import pytest

############################################################################
#                         Functional Testing                               #
############################################################################


@pytest.mark.incremental
class TestLibcloudFunctionality:

    def test_list_machines_linode(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.add_cloud(name='Linode', provider= 'linode', api_token=owner_api_token,
                                       api_key=safe_get_var('clouds/linode', 'api_key_new', config.CREDENTIALS['LINODE']['apikey'])).post()
        assert_response_ok(response)
        cache.set('linode_cloud_id', response.json()['id'])
        response = mist_api_v1.list_machines(cloud_id=cache.get('linode_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) >= 0, "List Linode machines did not return a proper result"
        print("Success!!!")

    def test_list_machines_equinix_metal(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.add_cloud(name='Equinix Metal', provider= 'equinixmetal', api_token=owner_api_token,
                                       api_key=safe_get_var('clouds/packet', 'apikey',
                                                            config.CREDENTIALS['EQUINIX METAL']['apikey'])).post()
        assert_response_ok(response)
        cache.set('equinix_metal_cloud_id', response.json()['id'])
        response = mist_api_v1.list_machines(cloud_id=cache.get('equinix_metal_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) >= 0, "List Equinix Metal machines did not return a proper result"
        print("Success!!!")

    def test_list_machines_openstack(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.add_cloud(name='Openstack', provider= 'openstack', api_token=owner_api_token,
                                        username=safe_get_var('clouds/vexxhost', 'user', config.CREDENTIALS['OPENSTACK']['user']),
                                        auth_url=safe_get_var('clouds/vexxhost', 'authUrl', config.CREDENTIALS['OPENSTACK']['authUrl']),
                                        tenant=safe_get_var('clouds/vexxhost', 'tenant', config.CREDENTIALS['OPENSTACK']['tenant']),
                                        password=safe_get_var('clouds/vexxhost', 'password', config.CREDENTIALS['OPENSTACK']['password']),
                                        region=safe_get_var('clouds/vexxhost', 'region', config.CREDENTIALS['OPENSTACK']['region'])).post()
        assert_response_ok(response)
        cache.set('openstack_cloud_id', response.json()['id'])
        response = mist_api_v1.list_machines(cloud_id=cache.get('openstack_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) >= 0, "List Openstack machines did not return a proper result"
        print("Success!!!")

#    def test_list_machines_vultr(self, pretty_print, mist_api_v1, cache, owner_api_token):
#        response = mist_api_v1.add_cloud(name='Vultr', provider= 'vultr', api_token=owner_api_token,
#                                       api_key=safe_get_var('clouds/vultr', 'apikey',
#                                                            config.CREDENTIALS['VULTR']['apikey'])).post()
#        assert_response_ok(response)
#        cache.set('vultr_cloud_id', response.json()['id'])
#        response = mist_api_v1.list_machines(cloud_id=cache.get('vultr_cloud_id', ''), api_token=owner_api_token).get()
#        assert_response_ok(response)
#        assert len(response.json()) >= 0, "List Vultr machines did not return a proper result"
#        print "Success!!!"

    def test_list_machines_azure_arm(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.add_cloud(name='Azure_arm', provider= 'azure_arm', api_token=owner_api_token,
                                       tenant_id=safe_get_var('clouds/azure_arm', 'tenant_id',
                                                              config.CREDENTIALS['AZURE_ARM']['tenant_id']),
                                       subscription_id=safe_get_var('clouds/azure_arm', 'subscription_id',
                                                              config.CREDENTIALS['AZURE_ARM']['subscription_id']),
                                       key=safe_get_var('clouds/azure_arm', 'client_key',
                                                              config.CREDENTIALS['AZURE_ARM']['client_key']),
                                       secret=safe_get_var('clouds/azure_arm', 'client_secret',
                                                              config.CREDENTIALS['AZURE_ARM']['client_secret'])).post()
        assert_response_ok(response)
        cache.set('azure_arm_cloud_id', response.json()['id'])
        response = mist_api_v1.list_machines(cloud_id=cache.get('azure_arm_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) >= 0, "List Azure_arm machines did not return a proper result"
        print("Success!!!")

    def test_list_sizes_linode(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_sizes(cloud_id=cache.get('linode_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Linode sizes did not return any sizes"
        print("Success!!!")

    def test_list_sizes_equinix_metal(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_sizes(cloud_id=cache.get('equinix_metal_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Equinix Metal sizes did not return any sizes"
        print("Success!!!")

    def test_list_sizes_openstack(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_sizes(cloud_id=cache.get('openstack_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Openstack sizes did not return any sizes"
        print("Success!!!")

#    def test_list_sizes_vultr(self, pretty_print, mist_api_v1, cache, owner_api_token):
#        response = mist_api_v1.list_sizes(cloud_id=cache.get('vultr_cloud_id', ''), api_token=owner_api_token).get()
#        assert_response_ok(response)
#        assert len(response.json()) > 0, "List Vultr sizes did not return any sizes"
#        print "Success!!!"

    def test_list_sizes_azure_arm(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_sizes(cloud_id=cache.get('azure_arm_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Azure_arm sizes did not return any sizes"
        print("Success!!!")

    def test_list_locations_linode(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_locations(cloud_id=cache.get('linode_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Linode locations did not return any locations"
        print("Success!!!")

    def test_list_locations_equinix_metal(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_locations(cloud_id=cache.get('equinix_metal_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Equinix Metal locations did not return any locations"
        print("Success!!!")

    def test_list_locations_openstack(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_locations(cloud_id=cache.get('openstack_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Openstack locations did not return any locations"
        print("Success!!!")

#    def test_list_locations_vultr(self, pretty_print, mist_api_v1, cache, owner_api_token):
#        response = mist_api_v1.list_locations(cloud_id=cache.get('vultr_cloud_id', ''), api_token=owner_api_token).get()
#        assert_response_ok(response)
#        assert len(response.json()) > 0, "List Vultr locations did not return any locations"
#        print "Success!!!"

    def test_list_locations_azure_arm(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_sizes(cloud_id=cache.get('azure_arm_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Azure_arm locations did not return any locations"
        print("Success!!!")

    def test_list_images_linode(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_images(cloud_id=cache.get('linode_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Linode images did not return any images"
        print("Success!!!")

    def test_list_images_equinix_metal(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_images(cloud_id=cache.get('equinix_metal_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Equinix Metal images did not return any images"
        print("Success!!!")

    def test_list_images_openstack(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_images(cloud_id=cache.get('openstack_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Openstack images did not return any images"
        print("Success!!!")

#    def test_list_images_vultr(self, pretty_print, mist_api_v1, cache, owner_api_token):
#        response = mist_api_v1.list_images(cloud_id=cache.get('vultr_cloud_id', ''), api_token=owner_api_token).get()
#        assert_response_ok(response)
#        assert len(response.json()) > 0, "List Vultr images did not return any images"
#        print "Success!!!"

    def test_list_images_azure_arm(self, pretty_print, mist_api_v1, cache, owner_api_token):
         response = mist_api_v1.list_images(cloud_id=cache.get('azure_arm_cloud_id', ''), api_token=owner_api_token).get()
         assert_response_ok(response)
         assert len(response.json()) > 0, "List Azure_arm images did not return any images"
         print("Success!!!")
