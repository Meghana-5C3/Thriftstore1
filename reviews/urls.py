from django.urls import path
from .views import add_review

app_name = 'reviews'

urlpatterns = [
    path('add/<int:product_id>/', add_review, name='add_review'),
]
