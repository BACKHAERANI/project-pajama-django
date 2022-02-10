from django.db import models


class Clothes(models.Model):
    clothes_num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=18, choices=[
        ("TOP", "TOP"),
        ("BLOUSE & SHIRT", "BLOUSE & SHIRT"),
        ("DRESS", "DRESS"),
        ("PANTS", "PANTS"),
        ("SKIRT", "SKIRT"),
        ("OUTER", "OUTER"),
        ("ACC & CAP", "ACC & CAP")],
                                blank=True)
    price = models.IntegerField()
    region = models.CharField(max_length=30)
    content = models.TextField()
    img1 = models.ImageField(upload_to="redanse/clothes/%Y/%m/%d/%H/%M/%S", blank=True)
    img2 = models.ImageField(upload_to="redanse/clothes/%Y/%m/%d/%H/%M/%S", blank=True)
    img3 = models.ImageField(upload_to="redanse/clothes/%Y/%m/%d/%H/%M/%S", blank=True)
    img4 = models.ImageField(upload_to="redanse/clothes/%Y/%m/%d/%H/%M/%S", blank=True)
    img5 = models.ImageField(upload_to="redanse/clothes/%Y/%m/%d/%H/%M/%S", blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-clothes_num"]