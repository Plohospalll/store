
from django.shortcuts import render
from products.models import Product, ProductCotegory



def index(request):
    context = {'title': 'store max',
               'is_promotion': True}
    return render(request, 'index.html', context)


def products(request):
    content = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCotegory.objects.all(),
    }
    return render(request, 'products.html', content)
