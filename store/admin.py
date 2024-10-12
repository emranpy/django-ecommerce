
from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name', 'price', 'stock', 'is_available', 'modified_date']
    prepopulated_fields = {'slug':('product_name',)}
    list_display_links = ['id', 'product_name', 'price', 'stock']