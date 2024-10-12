from django.shortcuts import render, get_object_or_404
from store.models import Product

def home(request):
    products = Product.objects.filter(is_available=True)  # You can chain filter directly
    context = {'products': products}
    return render(request, 'home.html', context)

