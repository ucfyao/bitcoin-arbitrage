# Copyright (C) 2017, JackYao <yaozihao@yaozihao.cn>

from ._huobi import Huobi

class HuobiCNY(Huobi):
    def __init__(self):
        super().__init__("CNY", "btc")
