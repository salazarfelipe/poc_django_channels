from django.contrib import admin

from .models import Coordinates

@admin.register(Coordinates)
class CoordinatesAdmin(admin.ModelAdmin):
    search_fields = ('provider',)
    list_display = ('provider','latitude','longitude','created_at',)