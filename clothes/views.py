from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from clothes.models import Clothes
from clothes.serializers import ClothesSerializer


class ClothesViewSet(ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
