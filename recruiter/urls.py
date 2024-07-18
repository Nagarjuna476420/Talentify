from django.urls import path
from .views import create_recruiter_view

urlpatterns = [
    path('create/', create_recruiter_view, name='create_recruiter'),
]
