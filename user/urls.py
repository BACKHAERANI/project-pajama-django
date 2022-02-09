from django.urls import path
from user.views import UserAPIView, TokenObtainPairView, TokenRefreshView

app_name = "user"

urlpatterns = []

urlpatterns += [path('api/user/', UserAPIView.as_view(), name='user'),
                path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                ]