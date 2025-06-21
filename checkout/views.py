from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from orders.models import Order, OrderItem
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart,CartItem

@login_required
def checkout_view(request):
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
    items = OrderItem.objects.filter(order=order)

    if request.method == "POST":
        order.is_ordered = True
        order.save()
        return redirect('checkout:checkout_success')

    return render(request, 'checkout/checkout.html', {'order': order, 'items': items})

@login_required
def checkout_success_view(request):
    return render(request, 'checkout/success.html')


@login_required
def place_order(request):
    if request.method == 'POST':
        # Get the user's cart
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            messages.error(request, "Your cart is empty.")
            return redirect('cart:view_cart')

        if not cart.items.exists():
            messages.error(request, "Your cart has no items.")
            return redirect('cart:view_cart')

        # Create order
        order = Order.objects.create(user=request.user)

        # Move items from cart to order
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Optionally clear cart
        cart.items.all().delete()

        messages.success(request, "Order placed successfully.")
        return redirect('checkout:checkout_success')

    return redirect('checkout:checkout')
