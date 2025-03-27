import pytest
from projects.advanced.shortener import URLShortener

@pytest.fixture
def url_shortener():
    return URLShortener()

def test_shorten_url(url_shortener):
    short_url = url_shortener.shorten_url("https://example.com")
    assert isinstance(short_url, str)
    assert len(short_url) == 6

def test_resolve_url(url_shortener):
    original_url = "https://test.com"
    short_url = url_shortener.shorten_url(original_url)
    assert url_shortener.resolve_url(short_url) == original_url

@pytest.mark.parametrize("url", [
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com",
])
def test_multiple_urls(url_shortener, url):
    short_url = url_shortener.shorten_url(url)
    assert url_shortener.resolve_url(short_url) == url
