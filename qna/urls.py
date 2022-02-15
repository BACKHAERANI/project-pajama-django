from django.urls import path, include
from rest_framework.routers import DefaultRouter

from qna import views
from qna.views import QnaViewSet

app_name = "qna"

router = DefaultRouter()
router.register("qna", QnaViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
