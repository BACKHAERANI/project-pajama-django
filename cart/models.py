from django.db import models
from user.models import User
from clothes.models import Clothes


class Cart(models.Model):
    cart_num = models.AutoField(primary_key=True)
    payment_status = models.IntegerField(choices=[(0, 0), (1, 1)])
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    clothes_num = models.ForeignKey(Clothes, on_delete=models.CASCADE, db_column='clothes_num')

    def __int__(self) -> int:
        return self.cart_num

    class Meta:
        ordering = ["-cart_num"]


