from typing import Dict
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OriginTokenObtainPairSerializer,
    TokenRefreshSerializer as OriginTokenRefreshSerializer,
)

from cart.serializers import CartSerializer
from notice.serializers import NoticeSerializer
from payment.serializers import PaymentSerializer

User = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["user_id", "password", "password2",  "username",
                  "user_nickname", "user_tel", "user_birth", "user_genre",
                  "user_auth", "user_type"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("Difference between passwords")
        return attrs

    def create(self, validated_data):
        user_id = validated_data["user_id"]
        username = validated_data["username"]
        password = validated_data["password"]
        user_nickname = validated_data.get("user_nickname", "")
        user_birth = validated_data["user_birth"]
        user_tel = validated_data["user_tel"]
        user_genre = validated_data.get("user_genre", "")


        new_user = User(user_id=user_id, username=username, user_nickname=user_nickname, user_tel=user_tel, user_birth=user_birth,
                        user_genre=user_genre)
        new_user.set_password(password)
        new_user.save()
        return new_user


class TokenObtainPairSerializer(OriginTokenObtainPairSerializer):
    def validate(self, attrs):
        data: Dict = super().validate(attrs)
        data["user_id"] = self.user.user_id
        data["username"] = self.user.username
        data["user_nickname"] = self.user.user_nickname
        data["is_staff"] = self.user.is_staff
        data["is_superuser"] = self.user.is_superuser
        return data


class TokenRefreshSerializer(OriginTokenRefreshSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    notice_set = NoticeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["user_id", "is_superuser","is_staff", "username","user_nickname",
                  "user_birth","user_tel", "user_genre","notice_set", "is_active"]


class Cart_PaymentSerializer(serializers.ModelSerializer):
    cart_set = CartSerializer(many=True, read_only=True)
    payment_set = PaymentSerializer(many=True, read_only=True)


    class Meta:
        model = User
        fields = ["user_id", "is_superuser",
                  "is_staff", "username", "cart_set","payment_set"]