from django.db import models
from django_quill.fields import QuillField

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=255)
    seo_content = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)
    slug = models.SlugField(null=True, blank=True, unique=True, allow_unicode=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Subcollection(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, unique=True, allow_unicode=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=255)
    seo_content = models.CharField(max_length=255, default=None)
    description = QuillField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True, allow_unicode=True)
    last_update = models.DateTimeField(auto_now=True)
    subcollection = models.ForeignKey(Subcollection, on_delete=models.SET_NULL, null=True, related_name='products')
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, related_name='products')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='store/images')
    image_name = models.CharField(max_length=255, blank=True)
    main_image = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.image_name = self.image.name.split('/')[-1].split('.')[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.image_name





























