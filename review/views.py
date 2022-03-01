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

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(payment_detail_num__clothes_num__clothes_num__iexact=query)

        return qs

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return ReviewCreateSerializer
        else:
            return ReviewSerializer
