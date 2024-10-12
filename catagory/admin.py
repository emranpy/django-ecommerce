from django.contrib import admin
from .models import Catagory
# Register your models here.

@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'catagory_name']
    prepopulated_fields = {'slug':['catagory_name']}
    list_display_links = ['id', 'catagory_name']