from django.core.validators import MaxValueValidator
from django.db import models
from payment.models import Payment_detail


class Review(models.Model):
    payment_detail_num = models.ForeignKey(Payment_detail, primary_key=True, on_delete=models.CASCADE,
                                           db_column='payment_detail_num',related_name="review")
    score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(10),
        ])
    title = models.CharField(max_length=200)
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
        ordering = ["-payment_detail_num"]