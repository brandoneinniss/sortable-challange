from dataclasses import dataclass
from typing import List, Dict


@dataclass
class ConfigData:
    sites: List
    bidders: Dict

    def get_bidder_by_name(self, name):
        bidder = self.bidders.get(name, None)
        if not bidder:
            raise Exception('No Bidder Found')
        else:
            return bidder
