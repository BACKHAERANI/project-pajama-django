from django.contrib import admin
from qna.models import Qna


@admin.register(Qna)
class QnaAdmin(admin.ModelAdmin):
    pass
