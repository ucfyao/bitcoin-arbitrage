import abc


class Observer(object, metaclass=abc.ABCMeta):
    def __init__(self):
        self.is_terminated = False

    def terminate(self):
        self.is_terminated = True
    
    def begin_opportunity_finder(self, depths):
        pass

    def end_opportunity_finder(self):
        pass

    ## abstract
    @abc.abstractmethod
    def opportunity(self, profit, volume, buyprice, kask, sellprice, kbid, perc, weighted_buyprice, weighted_sellprice):
        pass
