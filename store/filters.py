from django_filters.rest_framework import FilterSet, CharFilter
from .models import Product


class ProductFilter(FilterSet):
    collection_slug = CharFilter(field_name='collection__slug', lookup_expr='exact')
    subcollection_slug = CharFilter(field_name='subcollection__slug', lookup_expr='exact')

    class Meta:
        model = Product
        fields = ['slug', 'collection_slug', 'subcollection_slug']
