from collections import namedtuple

BidderData = namedtuple('BidderData', ['name', 'adjustment'])
SiteData = namedtuple('SiteData', ['name', 'bidders', 'floor'])
AuctionData = namedtuple('AuctionData', ['site', 'units', 'bids'])
BidData = namedtuple('BidData', ['bidder', 'unit', 'bid'])


class TestData:

    @staticmethod
    def mock_config_parser_parse():
        mock_bidder_objects = {
            'AUCT': BidderData(name='AUCT', adjustment=0.0625),
            'BIDD': BidderData(name='BIDD', adjustment=0),
            'CEILING': BidderData(name='CEILING', adjustment=-0.0634)}
        mock_site_objects = [SiteData(name='houseofcheese.com',
                                      bidders=['AUCT', 'BIDD'], floor=32),
                             SiteData(name='test1.com',
                                      bidders=['AUCT', 'BIDD', 'CEILING'],
                                      floor=50),
                             SiteData(name='test2.com', bidders=['BIDD'],
                                      floor=20),
                             SiteData(name='test3.com', bidders=['AUCT',
                                                                 'CEILING'],
                                      floor=47)]
        return mock_site_objects, mock_bidder_objects

    @staticmethod
    def mock_input_parser_parse():
        auction1_bids_list = [BidData(bidder='AUCT', unit='banner', bid=35),
                              BidData(bidder='BIDD', unit='sidebar', bid=60),
                              BidData(bidder='AUCT', unit='sidebar', bid=55)]
        auction1_units_list = ['banner', 'sidebar']
        auction1_data = AuctionData(site='houseofcheese.com',
                                    units=auction1_units_list,
                                    bids=auction1_bids_list)

        auction2_bids_list = [BidData(bidder='AUCT', unit='sidebar', bid=35),
                              BidData(bidder='BIDD', unit='sidebar', bid=60),
                              BidData(bidder='CEILING', unit='sidebar', bid=60)]
        auction2_units_list = ['banner', 'sidebar']
        auction2_data = AuctionData(site='test1.com',
                                    units=auction2_units_list,
                                    bids=auction2_bids_list)

        auction3_bids_list = [BidData(bidder='AUCT', unit='sidebar', bid=35),
                              BidData(bidder='BIDD', unit='sidebar', bid=60),
                              BidData(bidder='AUCT', unit='sidebar', bid=55)]
        auction3_units_list = ['banner', 'sidebar']
        auction3_data = AuctionData(site='test2.com',
                                    units=auction3_units_list,
                                    bids=auction3_bids_list)

        auction4_bids_list = [BidData(bidder='AUCT', unit='banner', bid=11),
                              BidData(bidder='AUCT', unit='sidebar', bid=19)]
        auction4_units_list = ['banner', 'sidebar']
        auction4_data = AuctionData(site='test3.com',
                                    units=auction4_units_list,
                                    bids=auction4_bids_list)

        auction5_bids_list = [BidData(bidder='AUCT', unit='banner', bid=35),
                              BidData(bidder='BIDD', unit='sidebar', bid=60),
                              BidData(bidder='AUCT', unit='sidebar', bid=55),
                              BidData(bidder='CEILING', unit='banner', bid=45)]
        auction5_units_list = ['banner', 'sidebar']
        auction5_data = AuctionData(site='test4.com',
                                    units=auction5_units_list,
                                    bids=auction5_bids_list)
        auctions_list = [auction1_data, auction2_data, auction3_data,
                         auction4_data, auction5_data]
        return auctions_list
