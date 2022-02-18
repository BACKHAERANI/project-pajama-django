from rest_framework import serializers

from clothes.models import Clothes


class ClothesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = "__all__"


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = "__all__"
        depth = 1
