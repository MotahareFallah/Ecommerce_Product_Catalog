from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from store.models import Product, Collection, Subcollection, ProductImage


class CollectionSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        show_description = kwargs.pop('show_description', True)
        super().__init__(*args, **kwargs)

        if show_description is False:
            del self.fields['description']
            del self.fields['seo_content']

    class Meta:
        model = Collection
        fields = ['id', 'title', 'slug', 'description', 'products_count', 'seo_content']

    products_count = serializers.IntegerField(read_only=True)
    lookup_field = 'slug'


class SubcollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcollection
        fields = ['id', 'title', 'slug', 'products_count']

    products_count = serializers.IntegerField(read_only=True)
    lookup_field = 'slug'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    collection = CollectionSerializer()
    subcollection = SubcollectionSerializer()
    description_html = SerializerMethodField()
    lookup_field = 'slug'

    def get_description_html(self, instance):
        return str(instance.description.html)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description_html', 'slug', 'collection', 'subcollection', 'images', 'seo_content']


class ProductListSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer(show_description=False)
    subcollection = SubcollectionSerializer()
    main_image = serializers.SerializerMethodField()

    def get_main_image(self, obj):
        image = obj.images.filter(main_image=True).first()
        return ProductImageSerializer(image).data if image is not None else None

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'collection', 'subcollection', 'main_image']











