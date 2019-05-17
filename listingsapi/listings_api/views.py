from listings_api.models import Listing
from listings_api.serializers import ListingsSerializer
from listings_api.pagination import ListingsPagination
from listings_api import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
       'listings': reverse('listings-view', request=request, format=format),
    })


class ListingsView(generics.ListAPIView):
    serializer_class = ListingsSerializer
    pagination_class = ListingsPagination

    def get_queryset(self):
        if cache.use_cache() is None:
            cache.create_cache(Listing.get_all())

        return cache.use_cache()