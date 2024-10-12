from django.shortcuts import render, get_object_or_404
from store.models import Product
from catagory.models import Catagory  # Corrected typo

# Create your views here.
def store(request, category_slug=None):
    products = None
    total = 0

    if category_slug is not None:
        category = get_object_or_404(Catagory, slug=category_slug)  # Corrected variable name
        products = Product.objects.filter(catagory=category, is_available=True)  # Corrected to use 'category'
        total = products.count()
    else:
        products = Product.objects.filter(is_available=True)
        total = products.count()

    context = {'products': products, 'total': total}
    return render(request, 'store.html', context)

