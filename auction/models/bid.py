class Bid:
    __slots__ = ['_bidder', '_unit', '_bid']

    @property
    def bidder(self):
        return self._bidder

    @bidder.setter
    def bidder(self, value):
        self._bidder = value

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value

    @property
    def bid(self):
        return self._bid

    @bid.setter
    def bid(self, value):
        self._bid = value

    @property
    def adjusted_bid(self):
        return self.bid * (1 + self._bidder.adjustment)

    def __init__(self, bidder=None, unit=None, bid=None):
        self._bidder = bidder
        self._unit = unit
        self._bid = bid


