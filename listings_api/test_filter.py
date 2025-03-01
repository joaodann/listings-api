from django.test import TestCase
from listings_api import models
from listings_api import filters


def create_object_Listing_for_rental_with_price_5000():
    listing = models.Listing()
    listing.pricingInfos.price = 5000
    listing.id = "uk1"
    listing.pricingInfos.businessType = "RENTAL"
    listing.pricingInfos.monthlyCondoFee = 0
    listing.address.geoLocation.location.lat = 0.445532
    listing.address.geoLocation.location.lon = 0.3233546
    return listing


def create_object_Listing_for_rental_with_price_2500():
    listing = models.Listing()
    listing.pricingInfos.price = 2500
    listing.pricingInfos.businessType = "RENTAL"
    listing.pricingInfos.monthlyCondoFee = 0
    listing.id = "uk2"
    listing.address.geoLocation.location.lat = 0.445532
    listing.address.geoLocation.location.lon = 0.3233546
    return listing


def create_object_Listing_for_rental_with_price_1000_and_condo_fee_300():
    listing = models.Listing()
    listing.pricingInfos.price = 1000
    listing.pricingInfos.businessType = "RENTAL"
    listing.pricingInfos.monthlyCondoFee = 300
    listing.id = "uk3"
    listing.address.geoLocation.location.lat = 0.445532
    listing.address.geoLocation.location.lon = 0.3233546
    return listing


def create_object_Listing_for_sale_with_price_800000():
    listing = models.Listing()
    listing.usableAreas = 100
    listing.pricingInfos.price = 800000
    listing.id = "uk4"
    listing.pricingInfos.businessType = "SALE"
    listing.address.geoLocation.location.lat = 0.445532
    listing.address.geoLocation.location.lon = 0.3233546
    return listing


def create_object_Listing_for_sale_with_price_550000_inside_zap_area():
    listing = models.Listing()
    listing.usableAreas = 100
    listing.pricingInfos.price = 550000
    listing.id = "uk5"
    listing.pricingInfos.businessType = "SALE"
    listing.address.geoLocation.location.lat = -23.566583
    listing.address.geoLocation.location.lon = -46.689920
    return listing


def create_object_Listing_for_sale_with_price_400000():
    listing = models.Listing()
    listing.usableAreas = 200
    listing.pricingInfos.price = 400000
    listing.pricingInfos.businessType = "SALE"
    listing.id = "uk6"
    listing.address.geoLocation.location.lat = 0.445532
    listing.address.geoLocation.location.lon = 0.3233546
    return listing


def create_object_Listing_for_rental_with_price_5000_inside_zap_area():
    listing = models.Listing()
    listing.usableAreas = 100
    listing.pricingInfos.price = 5000
    listing.id = "uk7"
    listing.pricingInfos.businessType = "RENTAL"
    listing.address.geoLocation.location.lat = -23.566583
    listing.address.geoLocation.location.lon = -46.689920
    return listing


class FilterTest(TestCase):

    # RENTAL PRICE
    def test_filter_zap_rental_price_greater_than_3500(self):
        listing = create_object_Listing_for_rental_with_price_5000()
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_zap_rental_price_lower_than_3500(self):
        listing = create_object_Listing_for_rental_with_price_2500()
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)

    def test_filter_vivareal_rental_price_lower_than_4000(self):
        listing = create_object_Listing_for_rental_with_price_2500()
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_vivareal_rental_price_greater_than_4000(self):
        listing = create_object_Listing_for_rental_with_price_5000()
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)

    # SALE PRICE
    def test_filter_zap_sale_price_greater_than_600000(self):
        listing = create_object_Listing_for_sale_with_price_800000()
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_zap_sale_price_lower_than_600000(self):
        listing = create_object_Listing_for_sale_with_price_400000()
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)

    def test_filter_vivareal_sale_price_lower_than_700000(self):
        listing = create_object_Listing_for_sale_with_price_400000()
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_vivareal_sale_price_greater_than_700000(self):
        listing = create_object_Listing_for_sale_with_price_800000()
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)

    def test_filter_vivareal_sale_price_lower_than_700000_with_invalid_location(
        self
    ):
        listing = create_object_Listing_for_sale_with_price_400000()
        listing.address.geoLocation.location.lat = 0
        listing.address.geoLocation.location.lon = 0
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)

    # new rules
    # listing without location
    def test_filter_any_portal_remove_listings_without_location(self):
        listing = models.Listing()
        listing.address.geoLocation.location.lat = 0
        listing.address.geoLocation.location.lon = 0
        listings = [listing]
        zap_filtered_listings = filters.remove_listings_without_location_filter(
            listings
        )

        self.assert_(len(zap_filtered_listings) == 0)

    def test_filter_any_portal_remove_listings_without_location_latitude(self):
        listing = models.Listing()
        listing.address.geoLocation.location.lat = 0
        listing.address.geoLocation.location.lon = 0.3233546
        listings = [listing]
        zap_filtered_listings = filters.remove_listings_without_location_filter(
            listings
        )

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_any_portal_remove_listings_complete_location(self):
        listing = models.Listing()
        listing.address.geoLocation.location.lat = 0.445532
        listing.address.geoLocation.location.lon = 0.3233546
        listings = [listing]
        zap_filtered_listings = filters.remove_listings_without_location_filter(
            listings
        )

        self.assert_(len(zap_filtered_listings) == 1)

    # zap squareMeterPrice validation
    def test_filter_zap_squareMeter_without_usableAreas(self):
        listing = create_object_Listing_for_sale_with_price_800000()
        listing.usableAreas = 0
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_zap_squareMeter_with_square_meter_price_greater_than_3500(
        self
    ):
        listing = create_object_Listing_for_sale_with_price_800000()
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_zap_squareMeter_with_square_meter_price_lower_than_3500(
        self
    ):
        listing = create_object_Listing_for_sale_with_price_400000()
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)

    # zap inside zap area
    def test_filter_inside_zap_area_with_price_greater_than_540000(self):
        listing = (
            create_object_Listing_for_sale_with_price_550000_inside_zap_area()
        )
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_outside_zap_area_with_price_greater_than_540000(self):
        listing = (
            create_object_Listing_for_sale_with_price_550000_inside_zap_area()
        )
        listing.address.geoLocation.location.lat = -23.628169
        listing.address.geoLocation.location.lon = -46.864586
        listings = [listing]
        zap_filtered_listings = filters.listings_zap_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)

    # vivareal condo fee
    def test_filter_rental_with_condo_fee_equals_30_percent(self):
        listing = (
            create_object_Listing_for_rental_with_price_1000_and_condo_fee_300()
        )
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)

    def test_filter_rental_with_condo_fee_equals_29_percent(self):
        listing = (
            create_object_Listing_for_rental_with_price_1000_and_condo_fee_300()
        )
        listing.pricingInfos.monthlyCondoFee = 290
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    # vivareal inside zap area
    def test_filter_vivareal_inside_zap_area_with_price_greater_than_540000(
        self
    ):
        listing = (
            create_object_Listing_for_rental_with_price_5000_inside_zap_area()
        )
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 1)

    def test_filter_vivareal_outside_zap_area_with_price_greater_than_540000(
        self
    ):
        listing = (
            create_object_Listing_for_rental_with_price_5000_inside_zap_area()
        )
        listing.address.geoLocation.location.lat = -23.628169
        listing.address.geoLocation.location.lon = -46.864586
        listings = [listing]
        zap_filtered_listings = filters.listings_vivareal_filter(listings)

        self.assert_(len(zap_filtered_listings) == 0)
