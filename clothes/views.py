from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from clothes.models import Clothes
from clothes.serializers import ClothesSerializer


class ClothesViewSet(ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query)

        return qs
