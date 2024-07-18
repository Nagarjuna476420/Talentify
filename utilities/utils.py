import random
import string
from recruiter.models import Recruiter
from jobseeker.models import JobSeeker

def generate_unique_id(prefix):
    while True:
        unique_id = f"{prefix}-{''.join(random.choices(string.digits, k=6))}"
        if not Recruiter.objects.filter(user_id=unique_id).exists() and not JobSeeker.objects.filter(user_id=unique_id).exists():
            return unique_id
