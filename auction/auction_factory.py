from typing import Dict

from models.auction import AdUnit, Auction
from models.site import Site
from bid_factory import BidFactory


class AuctionFactory:

    @staticmethod
    def create_auctions(auctions_data, sites_data, bidders_data):
        """Creates a list of auction objects and returns the list"""
        auctions_list = []
        for auction_data in auctions_data:
            auctions_list.append(AuctionFactory._create_auction(auction_data,
                                                                sites_data,
                                                                bidders_data))
        return auctions_list

    @staticmethod
    def _create_auction(auction_data, site_data: Dict[str, Site], bidders_dict):
        """Creates a single auction object and returns the auction"""
        auction_site = site_data.get(auction_data.site, None)
        if not auction_site:
            return None
        auction_units = [AdUnit(name) for name in auction_data.units]
        auction_bids = BidFactory.create_bids(auction_data.bids, bidders_dict)
        return Auction(auction_site, auction_units, auction_bids)


