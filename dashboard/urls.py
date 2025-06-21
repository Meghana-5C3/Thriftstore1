from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_redirect, name='dashboard_redirect'),
    path('buyer/', views.buyer_dashboard, name='buyer'),
    path('seller/', views.seller_dashboard, name='seller'),
]
