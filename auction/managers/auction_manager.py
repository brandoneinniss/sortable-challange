from typing import List
from models.auction import Auction
from models.bid import Bid


class AuctionManager:

    def __init__(self, auctions: List[Auction], site_dict):
        self.auctions = auctions
        self.site_dict = site_dict

    def generate_auction_results(self):
        """Generate auction results each auction in list"""
        ad_wins = {'invalid': []}
        for auction in self.auctions:
            if auction is not None:
                ad_wins[auction.site.name] = auction.get_max_bids()
            else:
                ad_wins['invalid'].append({})
            self.display_result(list(ad_wins.items())[-1])
        return ad_wins

    def display_result(self, result):
        """Prints auction results to display"""
        if result[1]:
            print('----------------' + result[0] + '--------------')
            for data in result[1].items():
                print(data[0])
                print(data[1].bidder.name + ' - ' + str(data[1].bid))
        else:
            print('-----------Invalid Auction(s)--------')
            print(result[1])
