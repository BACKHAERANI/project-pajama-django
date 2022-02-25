from typing import Dict

from rest_framework import serializers

from payment.models import Payment_detail
from payment.serializers import Payment_detailSerializer
from review.models import Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


    def create(self, validated_data):
        _ = validated_data.pop('payment_detail_num')
        request = self.context.get("request")
        payment_detail_num= request.data.get("payment_detail_num")


        payment_detail = Payment_detail.objects.get(payment_detail_num__exact=payment_detail_num)
        review = Review.objects.create(payment_detail_num=payment_detail, **validated_data)

        return review


class ReviewSerializer(serializers.ModelSerializer):
    payment_detail_num = Payment_detailSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"
        depth = 1

    def to_representation(self, obj):
        """Move fields from profile to user representation."""
        representation = super().to_representation(obj)
        payment_detail_num_representation = representation.pop('payment_detail_num')
        for key in payment_detail_num_representation:
            representation[key] = payment_detail_num_representation[key]

        return representation

    def to_internal_value(self, data):
        """Move fields related to profile to their own profile dictionary."""
        payment_num_internal = {}
        for key in Payment_detailSerializer.Meta.fields:
            if key in data:
                payment_num_internal[key] = data.pop(key)

        internal = super().to_internal_value(data)
        internal['profile'] = payment_num_internal
        return internal
