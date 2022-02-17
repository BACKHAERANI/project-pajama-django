from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView as OriginTokenObtainPairView,
    TokenRefreshView as OriginTokenRefreshView,
)
from user.serializers import TokenObtainPairSerializer, UserCreationSerializer, UserSerializer, Cart_PaymentSerializer

User = get_user_model()


class UserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]


class TokenObtainPairView(OriginTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(OriginTokenRefreshView):
    pass

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Cart_PaymentList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = Cart_PaymentSerializer


class Cart_PaymentDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class =  Cart_PaymentSerializer
