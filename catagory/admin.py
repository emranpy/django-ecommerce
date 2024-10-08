from django.contrib import admin
from .models import Catagory
# Register your models here.

@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'catagory_name']