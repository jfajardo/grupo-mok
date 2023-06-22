from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginationClass(PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'number': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
