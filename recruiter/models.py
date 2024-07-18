from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from utilities.generators import generate_unique_id

class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recruiter_id = models.CharField(max_length=10, unique=True, default=generate_unique_id('r'))
    company_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.recruiter_id:
            self.recruiter_id = generate_unique_id('r')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} ({self.company_name})"

class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    posted_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
