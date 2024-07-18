from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from utilities.generators import generate_unique_id

class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_seeker_id = models.CharField(max_length=10, unique=True, default=generate_unique_id('j'))
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.job_seeker_id:
            self.job_seeker_id = generate_unique_id('j')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

class Application(models.Model):
    job = models.ForeignKey('recruiter.Job', on_delete=models.CASCADE)  # Reference to Job model from recruiter app
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    cover_letter = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(default=timezone.now)
    status_choices = [
        ('applied', 'Applied'),
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='applied')

    def __str__(self):
        return f"{self.jobseeker.user.username} applied for {self.job.title}"
