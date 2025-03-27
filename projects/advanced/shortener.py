import hashlib

class URLShortener:

    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        short_url = hashlib.md5(original_url.encode()).hexdigest()[:6]
        self.url_mapping[short_url] = original_url
        return short_url

    def resolve_url(self, short_url):
        return self.url_mapping.get(short_url, None)