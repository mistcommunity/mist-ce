from misttests.integration.api.helpers import *
from misttests import config
from misttests.config import safe_get_var

import pytest
import json

############################################################################
#                         Functional Testing                               #
############################################################################


@pytest.mark.incremental
class TestLibcloudFunctionality:

    def test_list_machines_docker(self, pretty_print, mist_api_v1, cache, owner_api_token):
        if config.LOCAL:
            response = mist_api_v1.add_cloud(name='Docker', provider='docker', api_token=owner_api_token,
                                       docker_host=config.LOCAL_DOCKER,
                                       docker_port='2375', show_all=True).post()
        else:
            response = mist_api_v1.add_cloud(name='Docker', provider='docker', api_token=owner_api_token,
                                       docker_host=safe_get_var('clouds/dockerhost', 'host',
                                                                config.CREDENTIALS['DOCKER']['host']),
                                       docker_port=safe_get_var('clouds/dockerhost', 'port',
                                                                config.CREDENTIALS['DOCKER']['port']),
                                       authentication=safe_get_var('clouds/dockerhost', 'authentication',
                                                                   config.CREDENTIALS['DOCKER']['authentication']),
                                       ca_cert_file=safe_get_var('clouds/dockerhost', 'tlsCaCert',
                                                                 config.CREDENTIALS['DOCKER']['tlsCaCert']),
                                       key_file=safe_get_var('clouds/dockerhost', 'tlsKey',
                                                             config.CREDENTIALS['DOCKER']['tlsKey']),
                                       cert_file=safe_get_var('clouds/dockerhost', 'tlsCert',
                                                              config.CREDENTIALS['DOCKER']['tlsCert']), show_all=True).post()
        assert_response_ok(response)
        cache.set('docker_cloud_id', response.json()['id'])
        response = mist_api_v1.list_machines(cloud_id=cache.get('docker_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Docker machines did not return any machines"
        print("Success!!!")

    def test_list_machines_rackspace(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.add_cloud(name='Rackspace', provider= 'rackspace', api_token=owner_api_token,
                                       region='dfw',
                                       username = safe_get_var('clouds/rackspace', 'username',
                                                           config.CREDENTIALS['RACKSPACE']['username']),
                                       api_key = safe_get_var('clouds/rackspace', 'apikey',
                                                           config.CREDENTIALS['RACKSPACE']['apikey'])).post()
        assert_response_ok(response)
        cache.set('rackspace_cloud_id', response.json()['id'])
        response = mist_api_v1.list_machines(cloud_id=cache.get('rackspace_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) >= 0, "List Rackspace machines did not return a proper result"
        print("Success!!!")

    def test_list_machines_aws(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.add_cloud(name='AWS', provider= 'ec2', api_token=owner_api_token,
                                       api_key=safe_get_var('clouds/aws', 'apikey', config.CREDENTIALS['EC2']['apikey']),
                                       api_secret=safe_get_var('clouds/aws', 'apisecret', config.CREDENTIALS['EC2']['apisecret']),
                                       region='ap-northeast-1').post()
        assert_response_ok(response)
        cache.set('aws_cloud_id', response.json()['id'])
        response = mist_api_v1.list_machines(cloud_id=cache.get('aws_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) >= 0, "List AWS machines did not return a proper result"
        print("Success!!!")

    def test_list_machines_digitalocean(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.add_cloud(name='Digital Ocean', provider= 'digitalocean', api_token=owner_api_token,
                                       token=safe_get_var('clouds/digitalocean', 'token', config.CREDENTIALS['DIGITALOCEAN']['token'])).post()
        assert_response_ok(response)
        cache.set('digitalocean_cloud_id', response.json()['id'])
        response = mist_api_v1.list_machines(cloud_id=cache.get('digitalocean_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) >= 0, "List Digital Ocean machines did not return a proper result"
        print("Success!!!")

    def test_list_machines_gce(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.add_cloud(name='GCE', provider= 'gce', api_token=owner_api_token,
                                         project_id=safe_get_var('clouds/gce/mist-dev-tests', 'projectId',
                                                                 config.CREDENTIALS['GCE']['projectId']),
                                         private_key = json.dumps(safe_get_var('clouds/gce/mist-dev-tests', 'privateKeyDetailed',
                                                                  config.CREDENTIALS['GCE']['privateKeyDetailed']))).post()
        assert_response_ok(response)
        cache.set('gce_cloud_id', response.json()['id'])
        response = mist_api_v1.list_machines(cloud_id=cache.get('gce_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) >= 0, "List GCE machines did not return a proper result"
        print("Success!!!")

    def test_list_machines_vultr(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.add_cloud(name='Vultr', provider='vultr', api_token=owner_api_token,
                                       api_key=safe_get_var('clouds/vultr',
                                                            'apikey',
                                                            config.CREDENTIALS['VULTR']['apikey']
                                                            )
                                       ).post()
        assert_response_ok(response)
        cache.set('vultr_cloud_id', response.json()['id'])
        response = mist_api_v1.list_machines(cloud_id=cache.get(
            'vultr_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json(
        )) >= 0, "List Vultr machines did not return a proper result"
        print("Success!!!")

    def test_list_sizes_docker(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_sizes(cloud_id=cache.get('docker_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) == 0, "List Docker sizes did not return any sizes"
        print("Success!!!")

    def test_list_sizes_rackspace(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_sizes(cloud_id=cache.get('rackspace_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Rackspace sizes did not return any sizes"
        print("Success!!!")

    def test_list_sizes_aws(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_sizes(cloud_id=cache.get('aws_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List AWS sizes did not return any sizes"
        print("Success!!!")

    def test_list_sizes_digitalocean(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_sizes(cloud_id=cache.get('digitalocean_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Digital Ocean sizes did not return any sizes"
        print("Success!!!")

    def test_list_sizes_gce(self, pretty_print, mist_api_v1, cache, owner_api_token):
       response = mist_api_v1.list_sizes(cloud_id=cache.get('gce_cloud_id', ''), api_token=owner_api_token).get()
       assert_response_ok(response)
       assert len(response.json()) > 0, "List GCE sizes did not return any sizes"
       print("Success!!!")

    def test_list_sizes_vultr(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_sizes(cloud_id=cache.get(
            'vultr_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()
                   ) > 0, "List Vultr sizes did not return any sizes"
        print("Success!!!")

    def test_list_locations_rackspace(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_locations(cloud_id=cache.get('rackspace_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Rackspace locations did not return any locations"
        print("Success!!!")

    def test_list_locations_aws(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_locations(cloud_id=cache.get('aws_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List AWS locations did not return any locations"
        print("Success!!!")

    def test_list_locations_digitalocean(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_locations(cloud_id=cache.get('digitalocean_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Digital Ocean locations did not return any locations"
        print("Success!!!")

    def test_list_locations_gce(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_locations(cloud_id=cache.get('gce_cloud_id', ''), api_token=owner_api_token).get()
        i = 0
        while response.status_code == 422 and i < 10:
            sleep(10)
            response = mist_api_v1.list_locations(cloud_id=cache.get('gce_cloud_id', ''), api_token=owner_api_token).get()
            i += 1
        assert_response_ok(response)
        assert len(response.json()) > 0, "List GCE locations did not return any locations"
        print("Success!!!")

    def test_list_locations_vultr(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_locations(cloud_id=cache.get(
            'vultr_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()
                   ) > 0, "List Vultr locations did not return any locations"
        print("Success!!!")

    def test_list_images_docker(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_images(cloud_id=cache.get('docker_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Docker images did not return any images"
        print("Success!!!")

    def test_list_images_rackspace(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_images(cloud_id=cache.get('rackspace_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Rackspace images did not return any images"
        print("Success!!!")

    def test_list_images_aws(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_images(cloud_id=cache.get('aws_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List AWS images did not return any images"
        print("Success!!!")

    def test_list_images_digitalocean(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_images(cloud_id=cache.get('digitalocean_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()) > 0, "List Digital Ocean images did not return any images"
        print("Success!!!")

    def test_list_images_gce(self, pretty_print, mist_api_v1, cache, owner_api_token):
       response = mist_api_v1.list_images(cloud_id=cache.get('gce_cloud_id', ''), api_token=owner_api_token).get()
       assert_response_ok(response)
       assert len(response.json()) > 0, "List GCE images did not return any images"
       print("Success!!!")

    def test_list_images_vultr(self, pretty_print, mist_api_v1, cache, owner_api_token):
        response = mist_api_v1.list_images(cloud_id=cache.get(
            'vultr_cloud_id', ''), api_token=owner_api_token).get()
        assert_response_ok(response)
        assert len(response.json()
                   ) > 0, "List Vultr images did not return any images"
        print("Success!!!")
