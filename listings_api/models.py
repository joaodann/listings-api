import datetime
import json

import requests
from django.conf import settings
from shapely.geometry import Point
from shapely.geometry import box


class Location:
    lon: float
    lat: float


class GeoLocation:
    precision: str
    location: Location

    def __init__(self):
        self.location = Location()


class Address:
    city: str
    neighborhood: str
    geoLocation: GeoLocation

    def __init__(self):
        self.geoLocation = GeoLocation()


class PricingInfos:
    yearlyIptu: str
    price: int
    businessType: str
    monthlyCondoFee: int


class Listing:
    usableAreas: int
    listingType: str
    createdAt: datetime
    listingStatus: str
    id: str
    parkingSpaces: int
    updatedAt: datetime
    owner: bool
    images: []
    address: Address
    bathrooms: int
    bedrooms: int
    pricingInfos: PricingInfos

    @property
    def squareMeterPrice(self):
        price = 0
        if self.usableAreas > 0:
            price = int(self.pricingInfos.price) / int(self.usableAreas)

        return price

    @property
    def monthlyCondoFeeRentalPercentage(self):
        percentage = 0
        if (
            int(self.pricingInfos.monthlyCondoFee) > 0
            and self.pricingInfos.businessType == "RENTAL"
        ):
            percentage = (
                int(self.pricingInfos.monthlyCondoFee)
                * 100
                / int(self.pricingInfos.price)
            )

        return percentage

    @property
    def isInsideZapGroupArea(self):
        isInside = False
        zapBoundingBox = box(
            float(settings.ZAP_BBOX_MIN_LATITUDE),
            float(settings.ZAP_BBOX_MIN_LONGITUDE),
            float(settings.ZAP_BBOX_MAX_LATITUDE),
            float(settings.ZAP_BBOX_MAX_LONGITUDE),
        )
        if (
            self.address.geoLocation.location.lat != 0
            and self.address.geoLocation.location.lon != 0
        ):
            isInside = zapBoundingBox.contains(
                Point(
                    self.address.geoLocation.location.lat,
                    self.address.geoLocation.location.lon,
                )
            )

        return isInside

    def __init__(self):
        self.pricingInfos = PricingInfos()
        self.address = Address()

    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj

    @staticmethod
    def get_all():
        listings = []
        decodedJson = ""
        json_data = requests.get(settings.LISTINGS_URL, verify=False, timeout=30, stream=True)
        for line in json_data.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                decodedJson += decoded_line


        loaded_json = json.loads(decodedJson, object_hook=Listing.from_dict)
        for listing_json in loaded_json:
            listings.append(listing_json)

        return listings
