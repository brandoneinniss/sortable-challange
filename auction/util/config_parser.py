from models.config_data import ConfigData
from collections import namedtuple
from .json_helper import get_json_file_content

BidderData = namedtuple('BidderData', ['name', 'adjustment'])
SiteData = namedtuple('SiteData', ['name', 'bidders', 'floor'])


class ConfigParser:

    @staticmethod
    def parse(config_path):
        """Parse method to parse config json file"""
        config_data = get_json_file_content(config_path)
        if config_data:
            return ConfigParser._parse_config(config_data)

    @staticmethod
    def _parse_config(data):
        """Prepare config data from file data"""
        bidders = ConfigParser._parse_bidder(data['bidders'])
        sites = ConfigParser._parse_sites(data['sites'])
        return ConfigData(sites, bidders)

    @staticmethod
    def _parse_bidder(bidders):
        """Prepare bidders from file data"""
        bidder_objects = {}
        for bidder in bidders:
            bidder_name = bidder['name']
            bidder_adjustment = bidder['adjustment']
            bidder_objects[bidder_name] = \
                BidderData(name=bidder_name, adjustment=bidder_adjustment)
        return bidder_objects

    @staticmethod
    def _parse_sites(sites):
        """Prepare sites from file data"""
        site_objects = []
        for site in sites:
            site_name = site['name']
            site_bidders = site['bidders']
            site_floor = site['floor']
            site_objects.append(SiteData(name=site_name,
                                         bidders=site_bidders,
                                         floor=site_floor))
        return site_objects
