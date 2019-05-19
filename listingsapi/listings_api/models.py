import os
import requests
import json
from collections import namedtuple
import datetime
from django.conf import settings


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