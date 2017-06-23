import urllib.request
import urllib.error
import urllib.parse
import json
import logging
from .market import Market


class BitfinexUSD(Market):
    def __init__(self):
        super().__init__("USD")
        self.update_rate = 20
        self.depth = {'asks': [{'price': 0, 'amount': 0}], 'bids': [
            {'price': 0, 'amount': 0}]}

    def update_depth(self):
        res = urllib.request.urlopen(
            'https://api.bitfinex.com/v1/book/btcusd')
        jsonstr = res.read().decode('utf8')
        try:
            depth = json.loads(jsonstr)
        except Exception:
            logging.error("%s - Can't parse json: %s" % (self.name, jsonstr))
        self.depth = self.format_depth(depth)

