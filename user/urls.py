from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserAPIView, TokenObtainPairView, TokenRefreshView, UserList, UserDetail, UserViewSet

app_name = "user"

urlpatterns = []

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns += [path('api/user/', UserAPIView.as_view(), name='user'),
                path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                path("api/users/", UserList.as_view(), name="user_view"),
                path('api/users/<str:pk>/', UserDetail.as_view()),
                path("api/", include(router.urls)),
                ]