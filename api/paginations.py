from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'  # Allow client to set the page size
    page_query_param = 'page-num' # Custom query parameter for page number
    max_page_size = 1  # Maximum limit for page size

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_size': self.page.paginator.per_page,
            'results': data
        })