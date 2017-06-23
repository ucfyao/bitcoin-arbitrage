import urllib.request
import urllib.error
import urllib.parse
import json
from .market import Market

class Coinbase(Market):
    def __init__(self, currency, code):
        super().__init__(currency)
        self.code = code
        self.update_rate = 30

    def update_depth(self):
        url = 'https://api.exchange.coinbase.com/products/%s/book?level=2' % self.code
        req = urllib.request.Request(url, headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "User-Agent": "curl/7.24.0 (x86_64-apple-darwin12.0)"})
        res = urllib.request.urlopen(req)
        depth = json.loads(res.read().decode('utf8'))
        self.depth = self.format_depth(depth)
