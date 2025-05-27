class NetworkController(object):
    def __init__(self, network):
        """Initialize the `NetworkController` given a network.

        Most times one is expected to access a controller from inside the
        network object, like this:

          network = mist.api.networks.models.Network.objects.get(id=network_id)
          network.ctl.list_subnets()

        """
        self.network = network
        self.cloud = network.cloud

class SubnetController(object):
    def __init__(self, subnet):
        """Initialize the `SubnetController` given a subnet.

        Most times one is expected to access a controller from inside the
        subnet object, like this:

          subnet = mist.api.networks.models.Subnet.objects.get(id=subnet_id)
          subnet.ctl.delete()

        """
        self.subnet = subnet
        self.cloud = subnet.network.cloud
