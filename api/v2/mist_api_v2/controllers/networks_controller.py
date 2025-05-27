import connexion

from mist.api.networks.models import NETWORKS
from mist.api.helpers import delete_none
from mist.api.tag.methods import add_tags_to_resource

from mist.api.exceptions import BadRequestError, NotFoundError
from mist.api.exceptions import PolicyUnauthorizedError
from mist.api.exceptions import NetworkListingError

from mist_api_v2 import util
from mist_api_v2.models.create_network_request import CreateNetworkRequest  # noqa: E501
from mist_api_v2.models.get_network_response import GetNetworkResponse  # noqa: E501
from mist_api_v2.models.list_networks_response import ListNetworksResponse  # noqa: E501

from .base import list_resources, get_resource


def get_network(network, only=None, deref='auto'):  # noqa: E501
    """Get network

    Get details about target network # noqa: E501

    :param network:
    :type network: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetNetworkResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    try:
        result = get_resource(
            auth_context, 'network', search=network, only=only, deref=deref)
    except NotFoundError:
        return 'Network does not exist', 404
    return GetNetworkResponse(data=result['data'], meta=result['meta'])


def list_networks(cloud=None, search=None, sort=None, start=None, limit=None, only=None, deref='auto', at=None):  # noqa: E501
    """List networks

    List networks owned by the active org. READ permission required on network &amp; cloud. # noqa: E501

    :param cloud:
    :type cloud: str
    :param search: Only return results matching search filter
    :type search: str
    :param sort: Order results by
    :type sort: str
    :param start: Start results from index or id
    :type start: str
    :param limit: Limit number of results, 1000 max
    :type limit: int
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str
    :param at: Limit results by specific datetime.
    :type at: str

    :rtype: ListNetworksResponse
    """
    try:
        auth_context = connexion.context['token_info']['auth_context']
    except KeyError:
        return 'Authentication failed', 401
    if at is not None:
        at = util.deserialize_datetime(at.strip('"')).isoformat()
    result = list_resources(
        auth_context, 'network', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref, at=at)
    return ListNetworksResponse(data=result['data'], meta=result['meta'])
