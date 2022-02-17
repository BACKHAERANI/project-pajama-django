from rest_framework import serializers

from community.models import Community


class CommunityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = "__all__"


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = "__all__"
        depth = 1
