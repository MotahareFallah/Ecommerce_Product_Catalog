from django.contrib import admin
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models


# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['subcollection', 'collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    inlines = [ProductImageInline]
    list_display = ['title', 'subcollection', 'collection']
    list_editable = ['subcollection', 'collection']
    list_per_page = 10
    search_fields = ['title', 'description', 'subcollection', 'collection']
    list_filter = ['last_update', 'subcollection', 'collection']
    list_select_related = ['subcollection', 'collection']

    class Media:
        css = {
            'all': ['store/styles.css']
        }



@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ['title', 'products_count']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}">{} Products</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )


@admin.register(models.Subcollection)
class SubcollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ['title', 'products_count']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, subcollection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'subcollection__id': str(subcollection.id)
            }))
        return format_html('<a href="{}">{} Products</a>', url, subcollection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )
    class Meta:
        verbose_name = 'زیرمجموعه'
        verbose_name_plural = 'زیرمجموعه‌ها'























