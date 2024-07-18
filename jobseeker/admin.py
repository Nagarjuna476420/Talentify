from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import JobSeeker,Application

admin.site.register(JobSeeker)
admin.site.register(Application)