import django_filters
from django import forms
from .models import Product, Category, Condition


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Search',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search by title...'
        })
    )

    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label='Category',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    condition = django_filters.ModelChoiceFilter(
        queryset=Condition.objects.all(),
        label='Condition',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        label='Min Price',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        label='Max Price',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Product
        fields = ['title', 'category', 'condition', 'min_price', 'max_price']
