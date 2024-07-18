from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .services import create_jobseeker

def create_jobseeker_view(request):
    if request.method == 'POST':
        data = request.POST
        jobseeker = create_jobseeker(data['email'], data['password'], data['resume'], data['skills'], data['experience'])
        return JsonResponse({'user_id': jobseeker.user_id})
    return render(request, 'jobseeker/create.html')
