from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile

@login_required
def dashboard_redirect(request):
    if request.user.profile.is_seller:
        return redirect('dashboard:seller')
    else:
        return redirect('dashboard:buyer')

@login_required
def buyer_dashboard(request):
    return render(request, 'dashboard/buyer_dashboard.html')

@login_required
def seller_dashboard(request):
    return render(request, 'dashboard/seller_dashboard.html')
