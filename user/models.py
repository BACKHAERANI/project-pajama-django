from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, MaxLengthValidator


class User(models.Model):
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
        ],)
    user_pw = models.CharField(max_length=20,   validators=[
            MinLengthValidator(8),
            RegexValidator(regex='^[a-zA-Z0-9!@#$%^&*]*$', message="특수문자(!@#$%^&*)를 포함한 최소 8글자 이상의 문자를 입력해주세요."),
        ], )
    user_nickname = models.CharField(max_length=18, unique=True)
    user_tel = models.CharField(max_length=13, validators=[
            RegexValidator(r'^\d{3}-\d{3,4}-\d{4}$')
        ])
    user_birth = models.CharField(max_length=10, validators=[
            RegexValidator(r'^\d{4}-\d{2}-\d{2}$')
        ])
    user_genre = models.CharField(max_length=18, choices=GENRE)
    user_type = models.IntegerField(choices=[(0, 0), (1, 1)])
    user_auth = models.IntegerField(choices=[(0, 0), (1, 1)])
    user_signupdate = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user_id

    class Meta:
        ordering = ["-user_signupdate"]


