import urllib.request
import urllib.error
import urllib.parse
import json
import sys
from .market import Market


class BitstampUSD(Market):
    def __init__(self):
        super(BitstampUSD, self).__init__("USD")
        self.update_rate = 20

    def update_depth(self):
        url = 'https://www.bitstamp.net/api/order_book/'
        req = urllib.request.Request(url, None, headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "User-Agent": "curl/7.24.0 (x86_64-apple-darwin12.0)"})
        res = urllib.request.urlopen(req)
        depth = json.loads(res.read().decode('utf8'))
        self.depth = self.format_depth(depth)


if __name__ == "__main__":
    market = BitstampUSD()
    print(market.get_ticker())
