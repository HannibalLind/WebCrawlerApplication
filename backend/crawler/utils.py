from urllib.parse import urlparse, urlunparse
from fastapi import HTTPException
import requests

def is_same_domain(base_url: str, test_url: str) -> bool:
    """
    Return True if test_url is within the same domain as base_url
    """
    base_domain = urlparse(base_url).hostname
    test_domain = urlparse(test_url).hostname
    return base_domain == test_domain

def make_full_url(start_of_url: str, addon: str) -> str:
    """
    Returns a full length URL from a href on the same domain.
    """
    if not addon.startswith("http"):
        abs_url = requests.compat.urljoin(start_of_url, addon)
    else:
        abs_url = addon # + "/" Potential addition
    return abs_url


def validate_url(check_url: str):
    """
    Raises errors if the URL is invalid
    """
    parsed_url = urlparse(check_url)

    if not parsed_url.scheme.startswith("http"):
        raise HTTPException(status_code=400, detail="Invalid URL, missing HTTP/HTTPS")  
    if not parsed_url.netloc:
        raise HTTPException(status_code=400, detail="Invalid URL, missing target")