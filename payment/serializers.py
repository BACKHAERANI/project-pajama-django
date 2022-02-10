from rest_framework import serializers
from payment.models import Payment, Payment_detail


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class Payment_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_detail
        fields = "__all__"