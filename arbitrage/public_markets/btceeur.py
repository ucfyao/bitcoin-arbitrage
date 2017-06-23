import urllib.request
import urllib.error
import urllib.parse
import json
from .market import Market


class BtceEUR(Market):
    def __init__(self):
        super(BtceEUR, self).__init__("EUR")
        # bitcoin central maximum call / day = 5000
        # keep 2500 for other operations
        self.update_rate = 60

    def update_depth(self):
        url = 'https://btc-e.com/api/2/btc_eur/depth'
        req = urllib.request.Request(url, None, headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "User-Agent": "curl/7.24.0 (x86_64-apple-darwin12.0)"})
        res = urllib.request.urlopen(req)
        depth = json.loads(res.read().decode('utf8'))
        self.depth = self.format_depth(depth)

if __name__ == "__main__":
    market = BtceEUR()
    print(market.get_ticker())
