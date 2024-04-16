from django.db.models import Count
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import ProductFilter
from .pagination import DefaultPagination
from .models import Product, ProductImage, Collection, Subcollection
from .serializers import ProductSerializer, ProductListSerializer, ProductImageSerializer, CollectionSerializer, SubcollectionSerializer


# Create your views here

class ProductViewSet(ReadOnlyModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        if self.action == 'retrieve':
            return ProductSerializer
    queryset = Product.objects.prefetch_related('images').all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'description']
    ordering_fields = ['last_update']
    lookup_field = 'slug'


class CollectionViewSet(ReadOnlyModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    lookup_field = 'slug'


class SubcollectionViewSet(ReadOnlyModelViewSet):
    queryset = Subcollection.objects.annotate(products_count=Count('products')).all()
    serializer_class = SubcollectionSerializer
    lookup_field = 'slug'


class ProductImageViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])

























