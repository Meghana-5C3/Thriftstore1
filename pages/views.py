from django.shortcuts import render

# Create your views here.
# pages/views.py
from products.models import Product


def home(request):
    products=Product.objects.all()
    return render(request, 'pages/home.html',{'products':products})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def terms(request):
    return render(request, 'pages/terms.html')

def privacy(request):
    return render(request, 'pages/privacy.html')
