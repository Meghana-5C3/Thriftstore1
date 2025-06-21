from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Condition
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    conditions = Condition.objects.all()

    category_id = request.GET.get('category')
    condition_id = request.GET.get('condition')
    search_query=request.GET.get('search')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if category_id:
        products = products.filter(category_id=category_id)
    if condition_id:
        products = products.filter(condition_id=condition_id)
    if search_query:
        products = products.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Pagination
    paginator = Paginator(products, 12)  # 12 products per page
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {
        'products': products_page,
        'categories': categories,
        'conditions': conditions,
        'search_query': search_query,
        'min_price': min_price,
        'max_price': max_price,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

def product_gallery(request):
    products = Product.objects.all()
    return render(request, 'products/product_gallery.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  # ✅ assign the seller here
            product.save()
            return redirect('products:product_list')  # replace with your actual product list URL name
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})