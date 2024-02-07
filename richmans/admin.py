from django.contrib import admin
from .models import RichMans, Gender


@admin.register(RichMans)
class RichManAdmin(admin.ModelAdmin):
    list_display = ('name', 'money', 'country')


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    pass
