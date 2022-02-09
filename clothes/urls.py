from django.urls import path, include
from rest_framework.routers import DefaultRouter

from clothes import views

app_name = "clothes"


router = DefaultRouter()
router.register("clothes", views.ClothesViewSet)
urlpatterns = [path("api/", include(router.urls)),
               ]
