from typing import Dict

from models.bid import Bid
from models.bidder import Bidder


class BidFactory:
    @staticmethod
    def create_bids(bids_data, bidders_data: Dict[str, Bidder]):
        """Creates a list of bids objects and returns a list"""
        bids_object_list = []
        for bid in bids_data:
            if bid.bidder in bidders_data:
                bids_object_list. \
                    append(BidFactory._create_bid(bid,
                                                  bidders_data.get(bid.bidder)))
        return bids_object_list

    @staticmethod
    def _create_bid(bid_data, bidder: Bidder):
        """Creates a single bid object and returns a bid"""
        bid_bidder = bidder
        bid_unit = bid_data.unit
        bid = bid_data.bid
        return Bid(bid_bidder, bid_unit, bid)
