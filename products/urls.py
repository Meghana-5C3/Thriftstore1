from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('gallery/', views.product_gallery, name='product_gallery'),
        path('add/', views.add_product, name='add_product'),  # ✅ make sure this exists

]
