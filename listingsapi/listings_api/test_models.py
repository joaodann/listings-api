from django.test import TestCase
from listings_api import models

def create_object_Listing_for_rental_with_price_500000():
    listing = models.Listing()
    listing.pricingInfos.price = 500000
    listing.pricingInfos.businessType = "SALE"
    listing.usableAreas = 80
    listing.address.geoLocation.location.lat = 0.445532
    listing.address.geoLocation.location.lon = 0.3233546
    return listing


class FilterTest(TestCase):

    def test_square_meter_price_with_usable_area(self):
        listing = create_object_Listing_for_rental_with_price_500000()
        self.assert_(listing.squareMeterPrice == 6250)

    def test_square_meter_price_without_usable_area(self):
        listing = create_object_Listing_for_rental_with_price_500000()
        listing.usableAreas = 0
        self.assert_(listing.squareMeterPrice == 0)
