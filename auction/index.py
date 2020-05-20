import sys
from util.config_parser import ConfigParser
from util.input_parser import InputParser
from auction_factory import AuctionFactory
from bidder_factory import BidderFactory
from site_factory import SiteFactory
from managers.auction_manager import AuctionManager

if __name__ == '__main__':
    config_path, input_path = sys.argv[1:3]
    config_data = ConfigParser.parse(config_path)
    input_data = InputParser.parse(input_path)

    bidder_object_dict = \
        BidderFactory.create_bidder_dict(config_data.bidders)
    site_object_dict = SiteFactory.create_site_dict(config_data.sites,
                                                    bidder_object_dict)

    auction_manager = AuctionManager(AuctionFactory.create_auctions(
        input_data.auctions, site_object_dict, bidder_object_dict),
        site_object_dict)
    auction_results = auction_manager.generate_auction_results()
    pass
