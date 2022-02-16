from django.urls import path, include
from rest_framework.routers import DefaultRouter

from review import views

app_name = "review"


router = DefaultRouter()
router.register("review_detail", views.ReviewViewSet)

urlpatterns = [path("api/", include(router.urls)),
               ]