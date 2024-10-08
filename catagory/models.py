from django.db import models

# Create your models here.

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    catagory_image = models.ImageField(upload_to='photos/catagories', blank=True)
    
    def __str__(self):
        return self.catagory_name

    
    class Meta:
        verbose_name = "catagory"
        verbose_name_plural = "catagories"
    