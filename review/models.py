from django.core.validators import MaxValueValidator
from django.db import models
from payment.models import Payment_detail


class Review(models.Model):
    payment_detail_num = models.ForeignKey(Payment_detail, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(10),
        ])
    title = models.CharField(max_length=50)
    content = models.TextField()
    img1 = models.ImageField(upload_to="redanse/review/%Y/%m/%d/%H/%M/%S", blank=True)
    img2 = models.ImageField(upload_to="redanse/review/%Y/%m/%d/%H/%M/%S", blank=True)
    img3 = models.ImageField(upload_to="redanse/review/%Y/%m/%d/%H/%M/%S", blank=True)
    img4 = models.ImageField(upload_to="redanse/review/%Y/%m/%d/%H/%M/%S", blank=True)
    img5 = models.ImageField(upload_to="redanse/review/%Y/%m/%d/%H/%M/%S", blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-clothes_num"]