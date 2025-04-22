import requests
from typing import List
from bs4 import BeautifulSoup
from .utils import *

async def crawl_website(start_url: str) -> List[str]:
    """
    Crawl the given URL and return a list of internal page URLs.
    """
    # Validate start url
    target_url = start_url
    validate_url(target_url)

    urls_found = [target_url]
    urls_to_visit = [target_url]

    while urls_to_visit:
        # Get the page to visit from the list
        current_url = urls_to_visit.pop()

        # Fetching the URL
        response = requests.get(current_url)
        response.raise_for_status()

        # Parse the HTML
        soup = BeautifulSoup(response.text, features="html.parser")

        # Collect all the links
        href_elements = soup.select("a[href]")
        img_elements = soup.select("img")
        elements = href_elements + img_elements

        # Loop over each element
        # if make full url if needed
        # Adds the url to the found or to visit pages if not there.
        for element in elements:
            url = element.get("href") or element.get("src")
            extended_url = make_full_url(current_url, url)
            if is_same_domain(start_url, extended_url) and extended_url not in urls_found:
                urls_to_visit.append(extended_url)
            if extended_url not in urls_found:
                urls_found.append(extended_url)

    return urls_found