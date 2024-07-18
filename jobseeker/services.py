from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import JobSeeker

def create_jobseeker(email, password, resume, skills=None, experience=None):
    user = User.objects.create_user(username=email, email=email, password=make_password(password))
    jobseeker = JobSeeker.objects.create(user=user, resume=resume, skills=skills, experience=experience)
    return jobseeker
