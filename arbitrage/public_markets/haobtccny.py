# Copyright (C) 2017, JackYao <yaozihao@yaozihao.cn>

import urllib.request
import urllib.error
import urllib.parse
import json
from .market import Market

class HaobtcCNY(Market):
    def __init__(self):
        super().__init__('CNY')
        self.update_rate = 1
        self.event = 'depth_haobtc'
        self.start_websocket_depth()

    def update_depth(self):
        url = 'https://haobtc.com/exchange/api/v1/depth/?size=50'
        req = urllib.request.Request(url, headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "User-Agent": "curl/7.24.0 (x86_64-apple-darwin12.0)"})
        res = urllib.request.urlopen(req)
        depth = json.loads(res.read().decode('utf8'))
        self.depth = self.format_depth(depth)
