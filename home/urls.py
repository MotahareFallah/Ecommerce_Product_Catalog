from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('information/', views.information_view),
    path('feature/', views.feature_view),
    path('about/', views.about_view),
    path('call/', views.call_view),
    path('social_media/', views.social_media_view),
    path('footer/', views.footer_view),
]
