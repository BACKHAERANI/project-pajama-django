from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from clothes.models import Clothes
from clothes.serializers import ClothesSerializer, ClothesCreateSerializer


class ClothesPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 1


class ClothesViewSet(ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
    pagination_class = ClothesPagination

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query)

        category = self.request.query_params.get("category", "")
        if category:
            qs = qs.filter(category__icontains=category)

        return qs

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return ClothesCreateSerializer
        else:
            return ClothesSerializer
