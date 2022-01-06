"""
1 - Importing render shortcut to render templates inside views.
"""
from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view to show all products, cluding sorting and searching."""

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
