from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_editable = ['description']


@admin.register(models.Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ['title', 'slogan', 'description']
    list_editable = ['slogan', 'description']


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    list_editable = ['content']


@admin.register(models.SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon_image', 'url']
    list_editable = ['url']


@admin.register(models.Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'phone']
    list_editable = ['email', 'phone']


