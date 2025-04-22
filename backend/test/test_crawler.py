import pytest
import asyncio

from crawler.crawler import crawl_website

def run(coro):
    return asyncio.run(coro)

def test_crawler_returns_list():
    result = run(crawl_website("https://filip-ph-johansson.github.io/"))
    assert isinstance(result, list)

def test_crawler_includes_start_url():
    start_url = "https://filip-ph-johansson.github.io/"
    result = run(crawl_website(start_url))
    assert start_url in result


