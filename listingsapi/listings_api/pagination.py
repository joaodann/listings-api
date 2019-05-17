from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ListingsPagination(PageNumberPagination):
    page_size = 20
    def get_paginated_response(self, data):
        return Response({
            'pageNumber': self.page.number,
            'pageSize': self.page.paginator.per_page,
            'totalCount': self.page.paginator.count,
            'listings': data
        })