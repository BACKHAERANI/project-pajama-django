from rest_framework import viewsets
from payment.models import Payment, Payment_detail
from payment.serializers import PaymentSerializer, Payment_detailSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class Payment_detailViewSet(viewsets.ModelViewSet):
    queryset = Payment_detail.objects.all()
    serializer_class = Payment_detailSerializer
