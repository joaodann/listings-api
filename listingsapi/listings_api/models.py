import os
import requests
import json
import datetime

CACHED_LISTINGS_RESULT = None

class Location:
    lon: float
    lat: float


class GeoLocation:
    precision: str
    location: Location


class Address:
    city: str
    neighborhood: str
    geoLocation: GeoLocation


class PricingInfos:
    yearlyIptu: int
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

    def __init__(self, data):
        self.__dict__ = data

    @staticmethod
    def get_all():
        listings = []
        json_data = requests.get(os.environ['LISTINGS_URL']).text
        loaded_json = json.loads(json_data)
        for listing_json in loaded_json:
            listing = Listing(listing_json)
            listings.append(listing)

        return listings