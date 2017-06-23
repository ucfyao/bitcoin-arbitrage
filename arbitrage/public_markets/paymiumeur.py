import urllib.request
import urllib.error
import urllib.parse
import json
from .market import Market


class PaymiumEUR(Market):
    def __init__(self):
        super(PaymiumEUR, self).__init__("EUR")
        # bitcoin central maximum call / day = 5000
        # keep 2500 for other operations
        self.update_rate = 24 * 60 * 60 / 2500

    def update_depth(self):
        res = urllib.request.urlopen(
            'https://paymium.com/api/data/eur/depth')
        depth = json.loads(res.read().decode('utf8'))
        self.depth = self.format_depth(depth)

if __name__ == "__main__":
    market = PaymiumEUR()
    print(market.get_ticker())
