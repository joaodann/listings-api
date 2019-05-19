from django.test import TestCase
from listings_api import models
from listings_api import filters


class FilterTest(TestCase):

    ##RENTAL PRICE
    def test_filter_zap_rental_price_greater_than_3500(self):
        listing = models.Listing()
        listing.pricingInfos.price = 5000
        listing.id = "uk1"
        listing.pricingInfos.businessType = "RENTAL"
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_zap_rental_price_lower_than_3500(self):
        listing = models.Listing()
        listing.pricingInfos.price = 2500
        listing.pricingInfos.businessType = "RENTAL"
        listing.id = "uk2"
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)

    def test_filter_vivareal_rental_price_lower_than_4000(self):
        listing = models.Listing()
        listing.pricingInfos.price = 2500
        listing.pricingInfos.businessType = "RENTAL"
        listing.id = "uk2"
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_vivareal_rental_price_greater_than_4000(self):
        listing = models.Listing()
        listing.pricingInfos.price = 5000
        listing.id = "uk1"
        listing.pricingInfos.businessType = "RENTAL"
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)

    ##SALE PRICE
    def test_filter_zap_sale_price_greater_than_600000(self):
        listing = models.Listing()
        listing.pricingInfos.price = 800000
        listing.id = "uk1"
        listing.pricingInfos.businessType = "SALE"
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_zap_sale_price_lower_than_600000(self):
        listing = models.Listing()
        listing.pricingInfos.price = 400000
        listing.pricingInfos.businessType = "SALE"
        listing.id = "uk2"
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)

    def test_filter_vivareal_sale_price_lower_than_700000(self):
        listing = models.Listing()
        listing.pricingInfos.price = 400000
        listing.pricingInfos.businessType = "SALE"
        listing.id = "uk2"
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_vivareal_sale_price_greater_than_700000(self):
        listing = models.Listing()
        listing.pricingInfos.price = 800000
        listing.id = "uk1"
        listing.pricingInfos.businessType = "SALE"
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)