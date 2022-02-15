from rest_framework import serializers

from qna.models import Qna


class QnaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qna
        fields = "__all__"


class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qna
        fields = "__all__"
        depth = 1
