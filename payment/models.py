from django.db import models

from clothes.models import Clothes
from user.models import User


class Payment(models.Model):
    payment_num = models.AutoField(primary_key=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.IntegerField()
    payment_method = models.CharField(max_length=18, choices=[
        ("카드", "카드"), ("현금", "만나서 현금결제")])
    total_price = models.IntegerField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, db_column='user_id')

    def __int__(self) -> int:
        return self.payment_num

    class Meta:
        ordering = ["-payment_num"]


class Payment_detail(models.Model):
    payment_detail_num = models.AutoField(primary_key=True)
    payment_num = models.ForeignKey(Payment, on_delete=models.CASCADE)
    clothes_num = models.ForeignKey(Clothes, on_delete=models.CASCADE)

    def __int__(self) -> int:
        return self.payment_num

    class Meta:
        ordering = ["-payment_detail_num"]


