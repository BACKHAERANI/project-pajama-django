from django.urls import path, include
from rest_framework.routers import DefaultRouter

from payment.views import PaymentViewSet, Payment_detailViewSet

app_name = "payment"

router = DefaultRouter()
router.register("payment", PaymentViewSet)
router.register("payment_detail", Payment_detailViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
