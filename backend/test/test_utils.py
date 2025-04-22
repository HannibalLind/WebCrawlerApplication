import pytest

from crawler.utils import *

def test_same_domain():
    url1 = "https://example.com/"
    url2 = "https://example.com/side1"

    assert is_same_domain(url1, url2) == True

def test_different_domain():
    url1 = "https://example.com/"
    url2 = "https://filip-ph-johansson.github.io/"

    assert is_same_domain(url1, url2) == False

def test_make_full_url():
    url = "https://filip-ph-johansson.github.io/"
    addon = "about.html"
    
    correct = "https://filip-ph-johansson.github.io/about.html"

    full = make_full_url(url, addon)
    assert correct == full

def test_make_full_url():
    url = "https://filip-ph-johansson.github.io/"
    addon = "https://example.com"
    
    correct = "https://example.com"

    full = make_full_url(url, addon)
    assert correct == full

def test_validation_lacks_http():
    url = "s://filip-ph-johansson.github.io/"
    with pytest.raises(HTTPException) as exc_info:
        validate_url(url)
    assert isinstance(exc_info.value, HTTPException)
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Invalid URL, missing HTTP/HTTPS"

def test_validation_lacks_host():
    url = "https:///about.html"
    with pytest.raises(HTTPException) as exc_info:
        validate_url(url)
    assert isinstance(exc_info.value, HTTPException)
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Invalid URL, missing target"