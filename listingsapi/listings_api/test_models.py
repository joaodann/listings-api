from django.test import TestCase
from listings_api import models

def create_object_Listing_for_sale_with_price_500000():
    listing = models.Listing()
    listing.pricingInfos.price = 500000
    listing.pricingInfos.businessType = "SALE"
    listing.usableAreas = 80
    listing.address.geoLocation.location.lat = -23.566583
    listing.address.geoLocation.location.lon = -46.689920
    return listing

def create_object_Listing_for_rental_with_price_1000():
    listing = models.Listing()
    listing.pricingInfos.price = 1000
    listing.pricingInfos.businessType = "RENTAL"
    listing.usableAreas = 80
    listing.address.geoLocation.location.lat = -23.566583
    listing.address.geoLocation.location.lon = -46.689920
    listing.pricingInfos.monthlyCondoFee = 300
    return listing


class ModelTest(TestCase):
    #square meter test
    def test_square_meter_price_with_usable_area(self):
        listing = create_object_Listing_for_sale_with_price_500000()
        self.assert_(listing.squareMeterPrice == 6250)

    def test_square_meter_price_without_usable_area(self):
        listing = create_object_Listing_for_sale_with_price_500000()
        listing.usableAreas = 0
        self.assert_(listing.squareMeterPrice == 0)

    #location inside grupo zap area
    def test_location_inside_zap_group_area(self):
        listing = create_object_Listing_for_sale_with_price_500000()
        self.assert_(listing.address.geoLocation.location.isInsideZapGroupArea)

    def test_location_outside_zap_group_area(self):
        listing = create_object_Listing_for_sale_with_price_500000()
        listing.address.geoLocation.location.lat = -23.628169
        listing.address.geoLocation.location.lon = -46.864586
        self.assert_(not listing.address.geoLocation.location.isInsideZapGroupArea)

    #viva real - condo fee rental percentage
    def test_condo_fee_percentage_equals_30(self):
        listing = create_object_Listing_for_rental_with_price_1000()
        self.assert_(listing.pricingInfos.monthlyCondoFeeRentalPercentage == 30)

    def test_condo_fee_percentage_equals_40(self):
        listing = create_object_Listing_for_rental_with_price_1000()
        listing.pricingInfos.monthlyCondoFee = 400
        self.assert_(listing.pricingInfos.monthlyCondoFeeRentalPercentage == 40)

    def test_condo_fee_percentage_equals_0(self):
        listing = create_object_Listing_for_sale_with_price_500000()
        listing.pricingInfos.monthlyCondoFee = 400
        self.assert_(listing.pricingInfos.monthlyCondoFeeRentalPercentage == 0)