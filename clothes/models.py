from django.db import models


class Clothes(models.Model):
    clothes_num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    category = models.IntegerField(choices=[(0, "상의"), (1, "하의"), (2, "악세서리"), (3, "신발")])
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