from listings_api.models import Listing
from listings_api.serializers import ListingsSerializer
from listings_api.pagination import ListingsPagination
from listings_api import cache
from listings_api import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework import generics
from rest_framework.exceptions import APIException


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {"listings": reverse("listings-view", request=request, format=format)}
    )


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'
    headers = {'Retry-Later', '120'}


class ListingsView(generics.ListAPIView):
    serializer_class = ListingsSerializer
    pagination_class = ListingsPagination

    def get_queryset(self):
        if (not cache.is_file_complete()):
            raise ServiceUnavailable()

        listings = Listing.get_all()
        portal = self.request.query_params.get("portal", None)
        if portal == "zap":
            listings = filters.listings_zap_filter(listings)
        if portal == "vivareal":
            listings = filters.listings_vivareal_filter(listings)

        return listings
