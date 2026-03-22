from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectView, name='projects'),
    path('projects/<slug:slug>/', views.ProjectDetails, name='project-details'),
]
