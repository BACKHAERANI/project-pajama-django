from django.contrib import admin
from clothes.models import Clothes


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    pass