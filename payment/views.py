from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from payment.models import Payment, Payment_detail
from payment.serializers import PaymentSerializer, Payment_detailSerializer, Payment_detailCreateSerializer, \
    PaymentCreateSerializer, Payment_DetailReviewSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return PaymentCreateSerializer
        else:
            return PaymentSerializer


class Payment_detailViewSet(viewsets.ModelViewSet):
    queryset = Payment_detail.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return Payment_detailCreateSerializer
        else:
            return Payment_detailSerializer



