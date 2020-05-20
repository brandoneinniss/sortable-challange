from models.site import Site


class SiteFactory:
    @staticmethod
    def create_site_dict(sites_data, bidders):
        site_object_dict = {}
        for site in sites_data:
            site_object_dict[site.name] = \
                SiteFactory._create_site(site, bidders)
        return site_object_dict

    @staticmethod
    def _create_site(site_data, bidders_input):
        name = site_data.name
        bidders = [bidders_input[name] for name in site_data.bidders]
        floor = site_data.floor
        return Site(name, bidders, floor)
