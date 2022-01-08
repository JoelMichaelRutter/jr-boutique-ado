"""
1 - Importing render shortcut to render templates inside views.
"""
from django.shortcuts import render


def view_bag(request):
    """ A view to render the bag.html page"""
    return render(request, 'bag/bag.html')
