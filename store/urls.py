from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('subcollections', views.SubcollectionViewSet)


products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('images', views.ProductImageViewSet, basename='product-images')


urlpatterns = router.urls + products_router.urls
