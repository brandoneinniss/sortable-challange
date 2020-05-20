class Site:
    __slots__ = ['name', 'bidders', 'floor']

    def __init__(self, name=None, bidders=[], floor=None):
        self.name = name
        self.bidders = bidders
        self.floor = floor
