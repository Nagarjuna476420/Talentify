from django.urls import path
from .views import create_jobseeker_view

urlpatterns = [
    path('create/', create_jobseeker_view, name='create_jobseeker'),
]
