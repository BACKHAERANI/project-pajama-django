from django.contrib import admin
from community.models import Community


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    pass