from django.shortcuts import render
from store.models import Product

# Create your views here.

def store(request):
    products = Product.objects.all().filter(is_available = True)
    total = products.count()
    context = {'products':products, 'total':total}
    return render(request, 'store.html',context)