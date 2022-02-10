from rest_framework.routers import DefaultRouter
from django.urls import path, include
from notice.views import NoticeViewSet

app_name = "notice"

router = DefaultRouter()
router.register("Notice", NoticeViewSet)

urlpatterns = [path("api/", include(router.urls)),]