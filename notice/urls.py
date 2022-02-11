from rest_framework.routers import DefaultRouter
from django.urls import path, include
from notice.views import NoticeCreateViewSet, NoticeViewSet

app_name = "notice"

router = DefaultRouter()
router.register("notice", NoticeViewSet)
router.register("newnotice", NoticeCreateViewSet)

urlpatterns = [path("api/", include(router.urls)),]