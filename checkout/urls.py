from django.urls import path
from . import views

app_name='checkout'

urlpatterns = [
    path('', views.checkout_view, name='checkout'),
    path('place/', views.place_order, name='place_order'),  # ✅ Add this line

    path('success/', views.checkout_success_view, name='checkout_success'),
]
