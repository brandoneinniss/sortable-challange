from dataclasses import dataclass
from typing import List
from models.auction import AdUnit, Auction
from models.bid import Bid


@dataclass
class InputData:
    auctions: List
    # site: str
    # units: List[AdUnit]
    # bids: List[Bid]
