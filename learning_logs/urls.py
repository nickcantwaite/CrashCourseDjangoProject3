"""Defines URL patterns for learning_logs."""

### LEARNING LOGSSSSS URLS

from . import views
from django.urls import path

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('groups/', views.groups, name='groups'),
]
