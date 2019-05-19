import requests
import json
import datetime
from django.conf import settings
from shapely.geometry import box
from shapely.geometry import Point


class Location:
    lon: float
    lat: float

    @property
    def isInsideZapGroupArea(self):
        isInside = False
        zapBoundingBox = box(float(settings.ZAP_BBOX_MIN_LATITUDE), float(settings.ZAP_BBOX_MIN_LONGITUDE), float(settings.ZAP_BBOX_MAX_LATITUDE), float(settings.ZAP_BBOX_MAX_LONGITUDE))
        if (self.lat != 0 and self.lon != 0):
            isInside = zapBoundingBox.contains(Point(self.lat, self.lon))

        return isInside


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


class Listing():
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
        if (self.usableAreas > 0):
            price = self.pricingInfos.price / self.usableAreas

        return price

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
        json_data = requests.get(settings.LISTINGS_URL).text
        loaded_json = json.loads(json_data, object_hook=Listing.from_dict)
        for listing_json in loaded_json:

            listings.append(listing_json)

        return listings