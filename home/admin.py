from django.contrib import admin
from solo.admin import SingletonModelAdmin
from . import models

# Register your models here.


@admin.register(models.Call)
class CallAdmin(SingletonModelAdmin):
    list_display = ['title']


@admin.register(models.Feature)
class FeatureAdmin(SingletonModelAdmin):
    list_display = ['title', 'description']
    list_editable = ['description']


@admin.register(models.Information)
class InformationAdmin(SingletonModelAdmin):
    list_display = ['title', 'slogan', 'description']
    list_editable = ['slogan', 'description']


@admin.register(models.About)
class AboutAdmin(SingletonModelAdmin):
    list_display = ['title', 'content']
    list_editable = ['content']


@admin.register(models.SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon_image', 'url']
    list_editable = ['url']


@admin.register(models.Footer)
class FooterAdmin(SingletonModelAdmin):
    list_display = ['title', 'email', 'phone']
    list_editable = ['email', 'phone']


