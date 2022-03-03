from rest_framework import serializers
from clothes.models import Clothes
from clothes.serializers import ClothesSerializer
from payment.models import Payment, Payment_detail
from review.models import Review






class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        depth = 1


class Payment_detailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_detail
        fields = "__all__"

class Review_Payment_DetailField(serializers.RelatedField):
    def to_representation(self, value):
        payment_detail_num = value.payment_detial_num

        return {"review_num": payment_detail_num}


class Payment_detailSerializer(serializers.ModelSerializer):
    clothes_num = ClothesSerializer(read_only=True)
    payment_num = PaymentSerializer(read_only=True)


    class Meta:
        model = Payment_detail
        fields = ["payment_detail_num","clothes_num", "payment_num", "review"]
        depth = 1

    # def to_representation(self, obj):
    #     """Move fields from profile to user representation."""
    #     representation = super().to_representation(obj)
    #     clothes_num_representation = representation.pop('clothes_num')
    #     for key in clothes_num_representation:
    #         if key == "clothes_num":
    #             representation[key] = clothes_num_representation[key]
    #
    #     return representation
    #
    # def to_internal_value(self, data):
    #     """Move fields related to profile to their own profile dictionary."""
    #     payment_num_internal = {}
    #     for key in PaymentSerializer.Meta.fields:
    #         if key in data:
    #             payment_num_internal[key] = data.pop(key)
    #
    #     internal = super().to_internal_value(data)
    #     internal['profile'] = payment_num_internal
    #     return internal



class Payment_DetailReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
        depth = 2


class PaymentCreateSerializer(serializers.ModelSerializer):
    payment_detail_set = Payment_detailSerializer(many=True)

    class Meta:
        model = Payment
        fields = "__all__"

    def create(self, validated_data):
        _ = validated_data.pop('payment_detail_set')
        payment = Payment.objects.create(**validated_data)

        request = self.context.get("request")
        payment_detail_datas = request.data.get("payment_detail_set")

        for payment_detail_data in payment_detail_datas:
            for key, value in payment_detail_data.items():
                clothes = Clothes.objects.get(clothes_num__exact=value)
                Payment_detail.objects.create(payment_num=payment, clothes_num=clothes)

        return payment






