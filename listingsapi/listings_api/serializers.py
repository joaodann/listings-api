from listings_api.models import Listing
from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    lon = serializers.FloatField()
    lat = serializers.FloatField()


class GeoLocationSerializer(serializers.Serializer):
    precision = serializers.CharField()
    location = LocationSerializer()


class AddressSerializer(serializers.Serializer):
    city = serializers.CharField()
    neighborhood = serializers.CharField()
    geoLocation = GeoLocationSerializer()


class PricingInfosSerializer(serializers.Serializer):
    yearlyIptu = serializers.CharField(required=False)
    price = serializers.IntegerField()
    businessType = serializers.CharField()
    monthlyCondoFee = serializers.CharField(required=False)


class ListingsSerializer(serializers.Serializer):
    id = serializers.CharField()
    usableAreas = serializers.IntegerField()
    images = serializers.ListField()
    listingType = serializers.CharField()
    createdAt = serializers.DateTimeField()
    listingStatus = serializers.CharField()
    parkingSpaces = serializers.IntegerField(required=False)
    updatedAt = serializers.DateTimeField()
    owner = serializers.BooleanField()
    address = AddressSerializer()
    bathrooms = serializers.IntegerField()
    bedrooms = serializers.IntegerField()
    pricingInfos = PricingInfosSerializer()