from django.db import models
from user.models import User


class Qna(models.Model):
    qna_num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    answer = models.TextField(blank=True)
    img = models.ImageField(upload_to="redanse/QNA/%Y/%m/%d/%H/%M/%S", blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-qna_num"]
