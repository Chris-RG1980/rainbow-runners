from django.shortcuts import render

# Create your views here.


def index(request):
    """Return the index page."""
    return render(request, 'home/index.html')


def about(request):
    """Return the about us page """
    return render(request, 'home/about.html')


def resources(request):
    """Return the resources page"""
    return render(request, 'home/resources.html')
