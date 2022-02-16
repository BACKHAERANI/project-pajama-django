from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from review.models import Review
from review.serializers import ReviewSerializer, ReviewCreateSerializer


class ReviewPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return ReviewCreateSerializer
        else:
            return ReviewSerializer
