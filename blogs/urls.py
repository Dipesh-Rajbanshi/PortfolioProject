from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogView, name='blogs'),
    path('blogs/<slug:slug>/', views.BlogDetails, name='blog-details'),
]
