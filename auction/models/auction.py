import enum
from models.bid import Bid


class AdUnit(enum.Enum):
    banner = 'banner'
    sidebar = 'sidebar'


class Auction:
    __slots__ = ['site', 'units', 'bids']

    def __init__(self, site=None, units=None, bids=None):
        self.site = site
        self.units = units
        self.bids = bids

    def get_max_bids(self):
        max_bids = {}
        for bid in self.bids:
            if all([bid.bidder in self.site.bidders,
                    AdUnit(bid.unit) in self.units,
                    bid.adjusted_bid > self.site.floor]):
                if bid.unit in max_bids:
                    max_bids[bid.unit] = \
                        bid if bid.adjusted_bid > max_bids[
                            bid.unit].adjusted_bid else max_bids[bid.unit]
                else:
                    max_bids[bid.unit] = bid

        return max_bids
