from models.input_data import InputData
from collections import namedtuple
from util.json_helper import get_json_file_content

AuctionData = namedtuple('AuctionData', ['site', 'units', 'bids'])
BidData = namedtuple('BidData', ['bidder', 'unit', 'bid'])


class InputParser:

    @staticmethod
    def parse(input_path):
        """Parse method to parse input json file"""
        input_data = get_json_file_content(input_path)
        if input_path:
            return InputData(InputParser._parse_input(input_data))

    @staticmethod
    def _parse_input(data):
        """Prepare input data from file data"""
        auctions_object = []
        for auction in data:
            site = auction['site']
            units = InputParser._parse_units(auction['units'])
            bids = InputParser._parse_bids(auction['bids'])
            auctions_object.append(AuctionData(site=site,
                                               units=units,
                                               bids=bids))
        return auctions_object

    @staticmethod
    def _parse_units(units):
        """Prepare units from file data"""
        unit_values = []
        for unit in units:
            unit_values.append(unit)
        return unit_values

    @staticmethod
    def _parse_bids(bids):
        """Prepare bids from file data"""
        bids_object = []
        for bid in bids:
            bidder = bid['bidder']
            unit = bid['unit']
            bid = bid['bid']
            bids_object.append(BidData(bidder=bidder, unit=unit, bid=bid))
        return bids_object
