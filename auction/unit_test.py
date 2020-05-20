"""Tests for the /query API endpoint."""
import unittest
from jsonschema import validate
from nose.plugins.attrib import attr
from test_data import TestData
from util.config_parser import ConfigParser
from models.config_data import ConfigData
from util.input_parser import InputParser
from models.input_data import InputData
from util.json_helper import get_json_file_content
from models.site import Site
from models.bidder import Bidder
from models.bid import Bid
from models.auction import Auction, AdUnit
import jsonschema


@attr('integration')
class UnitTests(unittest.TestCase):
    """End-to-end Smoke Test"""
    config_schema_path = '/auction/util/config_schema.json'
    input_schema_path = '/auction/util/input_schema.json'
    test_config_path = '/auction/test_config.json'
    test_input_path = '/auction/test_input.json'

    def setUp(self):
        self.operator = TestData()

    @attr('unittest')
    def test_config_schema(self):
        """Check that config data matches valid schema"""
        config_data = get_json_file_content(self.test_config_path)
        config_schema = get_json_file_content(self.config_schema_path)
        result = True
        try:
            validate(config_data, config_schema)
        except jsonschema.exceptions.ValidationError as e:
            result = False
        self.assertEqual(result, True, 'Invalid File Data')

    @attr('unittest')
    def test_input_schema(self):
        """Check that input data format matches valid schema"""
        input_data = get_json_file_content(self.test_input_path)
        input_schema = get_json_file_content(self.input_schema_path)
        result = True
        try:
            validate(input_data, input_schema)
        except jsonschema.exceptions.ValidationError as e:
            result = False
        self.assertEqual(result, True, 'Invalid File Data')

    @attr('unittest')
    def test_config_parser_parse(self):
        """Test config parser -> parse method"""
        result = ConfigParser.parse(self.test_config_path)
        expected = ConfigData(*self.operator.mock_config_parser_parse())
        self.assertEqual(result, expected, 'Invalid Config Data')

    @attr('unittest')
    def test_input_parser_parse(self):
        """Test input parser -> parse method"""
        result = InputParser.parse(self.test_input_path)
        expected = InputData(self.operator.mock_input_parser_parse())
        self.assertEqual(result, expected, 'Invalid Input Data')

    @attr('unittest')
    def test_auction_results(self):
        """Test auction bids result calculation"""
        bids = [Bid(Bidder('BRANDON', -0.001), 'banner', 50),
                Bid(Bidder('ASEMA', -0.0432), 'banner', 51)]
        site = Site('test.com', [bids[0].bidder, bids[1].bidder], 40)
        auction = Auction(site, [AdUnit.banner], bids)
        actual = auction.get_max_bids()
        self.assertEqual(actual['banner'].bid, 50, 'Invalid Auction')


if __name__ == '__main__':
    unittest.main()
