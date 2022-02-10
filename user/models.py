from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not user_id:
            raise ValueError('Users must have an user_id')

        user = self.model(
            user_id=user_id,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.create_user(
            user_id,
            password=password,
            **extra_fields
        )

        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    first_name = None
    last_name = None
    date_joined = None
    email = None

    GENRE = (
        ("팝핀", "팝핀"),
        ("브레이킹", "브레이킹"),
        ("락킹", "락킹"),
        ("왁킹", "왁킹"),
        ("힙합", "힙합"),
        ("하우스", "하우스"),
        ("크럼프", "크럼프"),
        ("기타", "기타"),
    )

    user_id = models.CharField(max_length=18, primary_key=True, validators=[
        MinLengthValidator(6),
        RegexValidator(regex='^[a-zA-Z0-9]*$'),
    ], )
    username = models.CharField(max_length=20)
    user_nickname = models.CharField(max_length=50, unique=True)
    user_tel = models.CharField(max_length=13, validators=[
        RegexValidator(r'^\d{3}-\d{3,4}-\d{4}$', message="오류"),
    ], help_text="입력예) 010-1234-1234")
    user_birth = models.CharField(max_length=10, validators=[
        RegexValidator(r'^\d{4}-\d{2}-\d{2}$')
    ])
    user_genre = models.CharField(max_length=18, choices=GENRE, blank=True)
    user_type = models.IntegerField(default=0, choices=[(0, 0), (1, 1)])
    user_auth = models.IntegerField(default=0, choices=[(0, 0), (1, 1)])
    user_signupdate = models.DateTimeField(auto_now_add=True, null=True)

    objects = CustomUserManager()





