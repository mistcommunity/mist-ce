import sys
import logging
import json
from time import time, sleep
import requests
from random import randint

from misttests import config
from misttests.api.utils import assert_response_ok
from misttests.config import safe_get_var
from misttests.integration.api.main.io import MistIoApi
from misttests.api.io import conftest
from misttests.config import safe_get_var



log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

mist_api_v1 = MistIoApi(config.MIST_URL)

providers = {
    "Azure": {
        "size": "ExtraSmall",
        "location": "West Europe",
        "image": "b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-17_04-amd64-server-20170412.1-en-us-30GB"
    },
    "Azure_ARM": {
        "size": "Standard_F1",
        "location": "westeurope",
        "image": "MicrosoftWindowsServer:WindowsServer:2008-R2-SP1:2.127.20170406",
        "machine_password":"Aw3somep@ss123"
    },
    "Docker": {
        "size": "",
        "location": "",
        "image": "mist/debian-ssh"
    },
    "DigitalOcean": {
        "size": "512mb",
        "location": "ams2",
        "image": "27663881"
    },
    "Linode": {
        "size": "1",
        "location": "10",
        "disk":12576,
        "image": "146"
    },
    "AWS": {
        "size": "m1.small",
        "location": "ap-northeast-1",
        "image": "ami-5e849130"
    },
    "GCE": {
        "size": "1000",
        "location": "2101",
        "location_name":"europe-west1-b",
        "image":"7223507091408113841",
        "image_extra": { "selfLink":"https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/images/ubuntu-1610-yakkety-v20170619a" }
    },
    "Rackspace": {
        "size": "2",
        "location": "0",
        "image": "ac3dfda7-6f5a-4940-a114-b253ecb70be2"
    },
    "Openstack": {
        "size": "1",
        "size_disk_primary": "5",
        "location": "0",
        "networks":["583bb96c-36c2-483a-b4bf-667f0278d1fb"],
        "size_cpu": "1",
        "associate_floating_ip":"true",
        "size_disk_swap": "1",
        "image": "d69e1f0e-5205-4698-880e-81f95774a633"
    },
    "Equinix Metal": {
        "size": "baremetal_0",
        "location": "ams1",
        "image": "debian_8"
    },
    "Vultr": {
        "size": "201",
        "location": "7",
        "image": "193"
    },
    "CloudSigma": {
        "size": "small-1",
        "image": "749f4885-10dc-48c3-9523-b88fea7441f5",
        "location": "",
    }
}

def check_machine_creation(log_line, job_id):
    try:
        if (log_line['job_id'] == job_id) and (log_line['action'] == 'machine_creation_finished'):
            if log_line['error'] == False:
                print('Machine created succesfully')
                machine_id = log_line['machine_id']
                return machine_id
            else:
                print((log_line['error']))
                return True
        else:
            return False
    except:
        return False


def check_cloud_exists(provider):
    resp = requests.get(
        config.MIST_URL + '/api/v1/clouds',
        headers={'Authorization': config.MIST_API_TOKEN},
        verify=True
    )
    cloud_id = None

    for cloud in resp.json():
        if cloud['name'] == provider:
            cloud_id = cloud['id']
    return cloud_id


def add_cloud(provider):
    cloud_id = check_cloud_exists(provider)
    if cloud_id == None:
        if provider == 'AWS':
            response = mist_api_v1.add_cloud(name=provider, provider= 'ec2', api_token=config.MIST_API_TOKEN,
                                       api_key=safe_get_var('clouds/aws_no_images', 'apikey', config.CREDENTIALS['EC2']['apikey']),
                                       api_secret=safe_get_var('clouds/aws_no_images', 'apisecret', config.CREDENTIALS['EC2']['apisecret']),
                                       region=providers[provider]['location']).post()

        elif provider == 'DigitalOcean':
            response = mist_api_v1.add_cloud(name=provider, provider= 'digitalocean', api_token=config.MIST_API_TOKEN,
                                       token=safe_get_var('clouds/digitalocean', 'token', config.CREDENTIALS['DIGITALOCEAN']['token'])).post()

        elif provider == "Linode":
            response = mist_api_v1.add_cloud(name=provider, provider= 'linode', api_token=config.MIST_API_TOKEN,
                                       api_key=safe_get_var('clouds/linode', 'api_key_new', config.CREDENTIALS['LINODE']['apikey'])).post()

        elif provider == "Azure":
            response = mist_api_v1.add_cloud(name=provider, provider= 'azure', api_token=config.MIST_API_TOKEN,
                                       subscription_id=safe_get_var('clouds/azure', 'subscription_id', config.CREDENTIALS['AZURE']['subscription_id']),
                                       certificate=safe_get_var('clouds/azure', 'certificate', config.CREDENTIALS['AZURE']['certificate'])).post()

        elif provider == "Azure_ARM":
            response = mist_api_v1.add_cloud(name=provider, provider= 'azure_arm', api_token=config.MIST_API_TOKEN,
                                       tenant_id=safe_get_var('clouds/azure_arm', 'tenant_id',
                                                              config.CREDENTIALS['AZURE_ARM']['tenant_id']),
                                       subscription_id=safe_get_var('clouds/azure_arm', 'subscription_id',
                                                              config.CREDENTIALS['AZURE_ARM']['subscription_id']),
                                       key=safe_get_var('clouds/azure_arm', 'client_key',
                                                              config.CREDENTIALS['AZURE_ARM']['client_key']),
                                       secret=safe_get_var('clouds/azure_arm', 'client_secret',
                                                              config.CREDENTIALS['AZURE_ARM']['client_secret'])).post()

        elif provider == 'Docker':
            response = mist_api_v1.add_cloud(name=provider, provider= 'docker', api_token=config.MIST_API_TOKEN,
                                       docker_host=safe_get_var('dockerhosts/godzilla', 'host', config.CREDENTIALS['DOCKER']['host']),
                                       docker_port=safe_get_var('dockerhosts/godzilla', 'port', config.CREDENTIALS['DOCKER']['port']),
                                       authentication=safe_get_var('dockerhosts/godzilla', 'authentication', config.CREDENTIALS['DOCKER']['authentication']),
                                       ca_cert_file=safe_get_var('dockerhosts/godzilla', 'ca', config.CREDENTIALS['DOCKER']['ca']),
                                       key_file=safe_get_var('dockerhosts/godzilla', 'key', config.CREDENTIALS['DOCKER']['key']),
                                       cert_file=safe_get_var('dockerhosts/godzilla', 'cert', config.CREDENTIALS['DOCKER']['cert'])).post()

        elif provider == "GCE":
            response = mist_api_v1.add_cloud(name='GCE', provider= 'gce', api_token=config.MIST_API_TOKEN,
                                      project_id=safe_get_var('clouds/gce/mist-dev-tests', 'projectId',
                                                              config.CREDENTIALS['GCE']['projectId']),
                                      private_key = json.dumps(safe_get_var('clouds/gce/mist-dev-tests', 'privateKeyDetailed',
                                                              config.CREDENTIALS['GCE']['privateKeyDetailed']))).post()

        elif provider == "Rackspace":
            response = mist_api_v1.add_cloud(name='Rackspace', provider= 'rackspace', api_token=config.MIST_API_TOKEN,
                                       region='dfw',
                                       username = safe_get_var('clouds/rackspace', 'username',
                                                           config.CREDENTIALS['RACKSPACE']['username']),
                                       api_key = safe_get_var('clouds/rackspace', 'apikey',
                                                           config.CREDENTIALS['RACKSPACE']['apikey'])).post()

        elif provider == "Equinix Metal":
            response = mist_api_v1.add_cloud(name='Equinix Metal', provider= 'equinixmetal', api_token=config.MIST_API_TOKEN,
                                           api_key=safe_get_var('clouds/packet', 'apikey',
                                                                config.CREDENTIALS['PACKET']['apikey'])).post()

        elif provider == "Vultr":
            response = mist_api_v1.add_cloud(name='Vultr', provider= 'vultr', api_token=config.MIST_API_TOKEN,
                                       api_key=safe_get_var('clouds/vultr', 'apikey',
                                                            config.CREDENTIALS['VULTR']['apikey'])).post()

        assert_response_ok(response)
        cloud_id = response.json()['id']

    return cloud_id


def create_machine(cloud_id, provider):
    #creating machine
    try:
        disk = providers[provider]['disk']
    except:
        disk = ''
    try:
        location_name=providers[provider]['location_name']
    except:
        location_name = ''
    try:
        networks=providers[provider]['networks']
    except:
        networks = []
    try:
        image_extra=providers[provider]['image_extra']
    except:
        image_extra = ''

    try:
        ex_storage_account=providers[provider]['ex_storage_account']
    except:
        ex_storage_account = ''

    try:
        machine_password=providers[provider]['machine_password']
    except:
        machine_password = ''

    try:
        ex_resource_group=providers[provider]['ex_resource_group']
    except:
        ex_resource_group = ''

    name = provider.replace(" ", "").replace("_","").lower() + str(randint(0,9999))

    payload = {'cloud_id':cloud_id,
                    'name': name,
                    'provider':provider,
                    'image':providers[provider]['image'],
                    'image_extra':image_extra,
                    'size':providers[provider]['size'],
                    'disk':disk,
                    'key_id':config.KEY_ID,
                    'location':providers[provider]['location'],
                    'location_name':location_name,
                    'ex_storage_account':ex_storage_account,
                    'machine_password':machine_password,
                    'ex_resource_group':ex_resource_group,
                    'networks':networks,
                    'async':True,
                    'cron_enable':False,
                    'monitoring':False
            }

    if provider == "Azure_ARM":
        payload['create_resource_group'] = True
        payload['create_storage_account'] = True
        payload['create_network'] = True
        payload['new_resource_group'] = name
        payload['new_storage_account'] = name + 'disks'
        payload['new_network'] = name + '-vnet'
        payload['machine_username'] = 'azureuser'

    response = requests.post(
        config.MIST_URL + '/api/v1/clouds/' + cloud_id + '/machines',
            headers={'Authorization': config.MIST_API_TOKEN},
            data=json.dumps(payload)
        )

    try:
        assert_response_ok(response)
        print(("\n " + provider + ": Machine creation command has been submitted successfully. Now polling!\n"))
    except AssertionError as e:
        print("Machine creation was not successful!")
        raise e

    job_id = json.loads(response.content)['job_id']

    return job_id


def main():
    for provider in providers:
        if provider in ['AWS', 'DigitalOcean', 'Linode', 'Azure', 'GCE', 'Rackspace', 'Equinix Metal', 'Vultr', 'Azure_ARM', 'CloudSigma']:
            #add the provider if not there
            cloud_id = add_cloud(provider)

            job_id = create_machine(cloud_id, provider)

            # waiting for the creation of the machine to finish
            log_found = False
            machine_id = None
            timeout = time() + 240
            while time() < timeout:
                resp = requests.get(
                    config.MIST_URL + '/api/v1/logs',
                    headers={'Authorization': config.MIST_API_TOKEN},
                    verify=True
                )

                for log_line in resp.json():
                    machine_creation = check_machine_creation(log_line, job_id)
                    if machine_creation:
                        machine_id = machine_creation
                        log_found = True
                        break
                    else:
                        pass
                if log_found:
                    break
                sleep(5)

            #destroy the machine
#            if machine_id:
#                resp = requests.post(
#                    config.MIST_URL + '/api/v1/clouds/' + cloud_id + '/machines/' + machine_id,
#                    headers={'Authorization': config.MIST_API_TOKEN},
#                    data = {'action':'destroy'},
#                    verify=True
#                )
#
#                try:
#                    assert_response_ok(resp)
#                    print "\n " + provider + ": Machine destroyed successfully\n"
#                except AssertionError as e:
#                    print "Could not destroy machine!"
#                    raise e

if __name__ == "__main__":
    main()
