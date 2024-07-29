from django.urls import path
from .views import create_recruiter_view,login_account

urlpatterns = [
    path('create/', create_recruiter_view, name='create_recruiter'),
    path('login/', login_account, name='loginform'),
]
