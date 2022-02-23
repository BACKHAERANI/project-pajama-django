from rest_framework import serializers

from clothes.serializers import ClothesSerializer
from payment.models import Payment, Payment_detail
from review.models import Review


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        depth = 1


class Payment_detailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_detail
        fields = "__all__"


class Payment_detailSerializer(serializers.ModelSerializer):
    clothes_num = ClothesSerializer(read_only=True)
    payment_num = PaymentSerializer(read_only=True)

    class Meta:
        model = Payment_detail
        fields = ["clothes_num", "payment_num"]
        depth = 1

    def to_representation(self, obj):
        """Move fields from profile to user representation."""
        representation = super().to_representation(obj)
        clothes_num_representation = representation.pop('clothes_num')
        for key in clothes_num_representation:
            if key == "clothes_num":
                representation[key] = clothes_num_representation[key]

        return representation

    def to_internal_value(self, data):
        """Move fields related to profile to their own profile dictionary."""
        payment_num_internal = {}
        for key in PaymentSerializer.Meta.fields:
            if key in data:
                payment_num_internal[key] = data.pop(key)

        internal = super().to_internal_value(data)
        internal['profile'] = payment_num_internal
        return internal


class Payment_DetailReviewSerializer(serializers.ModelSerializer):
    payment_detail_num = Payment_detailSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = "__all__"
        depth = 2
