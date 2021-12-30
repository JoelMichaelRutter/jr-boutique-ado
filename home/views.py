"""
1 - Importing render shortcut to render templates inside views.
"""
from django.shortcuts import render


def index(request):
    """ A view to render the index page"""
    return render(request, 'home/index.html')
