from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cart.views import CartViewSet

app_name = "cart"

router = DefaultRouter()
router.register("cart", CartViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
