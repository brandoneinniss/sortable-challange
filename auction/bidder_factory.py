from models.bidder import Bidder
from typing import Dict
from util.config_parser import BidderData


class BidderFactory:
    @staticmethod
    def create_bidder_dict(bidders_data: Dict[str, BidderData]):
        bidder_object_dict = {}
        for key, value in bidders_data.items():
            bidder_object_dict[key] =\
                BidderFactory.create_bidder(value)
        return bidder_object_dict

    @staticmethod
    def create_bidder(bidder_data: Bidder):
        name = bidder_data.name
        adjustment = bidder_data.adjustment
        return Bidder(name, adjustment)
