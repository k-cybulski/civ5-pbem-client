"""
This module contians account related actions, such as registration.
"""

from urllib.parse import urlparse, urlunparse, urljoin
import requests

from civ5client import ServerError, log_responses, log_response

class AccountTakenError(Exception):
    """Raised when attempting to register a taken account."""

def register_account(server_address, username, email, log=log_responses):
    """Sends a registration request with a given email and username."""
    register_request = requests.post(
        urljoin(server_address,"/user-accounts/register"),
        json={'email':email, 'username':username})
    if log:
        log_response(register_request)
    # TODO: A non-200 status code could mean a lot of things
    if register_request.status_code != 200:
        raise AccountTakenError

def request_credentials(interface):
    """Requests credentials given by a specific Interface, i.e.
    related to a specific access token on a server.
    """
    request = interface.get_request("/user-accounts/current")
    return request

def reset_access_token(server_address, email, log=log_responses):
    """Sends a request to reset the access token and send a new
    one via mail.
    """
    reset_request = requests.post(
        urljoin(server_address,"/user-accounts/reset-access-token"),
        json={'email':email})
    if log:
        log_response(reset_request)
    return reset_request
