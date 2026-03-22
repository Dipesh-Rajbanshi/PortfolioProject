from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('gallery/', views.GalleryView, name='gallery'),
    path('contact/', views.Contact, name='contact'),
]
