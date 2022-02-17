from django.urls import path, include
from rest_framework.routers import DefaultRouter

from community import views
from community.views import CommunityViewSet

app_name = "community"

router = DefaultRouter()
router.register("community", CommunityViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
