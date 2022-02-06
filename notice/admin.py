from django.contrib import admin
from notice.models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    pass
