
from django.db import models
from catagory.models import Catagory

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='photos/products')
    stock = models.SmallIntegerField()
    is_available = models.BooleanField(default=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.product_name
    
    class Meta:
        ordering = ['id']