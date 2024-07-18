from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Recruiter

def create_recruiter(email, password, company_name, phone_number=None, address=None):
    user = User.objects.create_user(username=email, email=email, password=make_password(password))
    recruiter = Recruiter.objects.create(user=user, company_name=company_name, phone_number=phone_number, address=address)
    return recruiter
