from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .services import create_recruiter

def create_recruiter_view(request):
    if request.method == 'POST':
        data = request.POST
        recruiter = create_recruiter(data['email'], data['password'], data['company_name'], data['phone_number'], data['address'])
        return JsonResponse({'user_id': recruiter.user_id})
    return render(request, 'recruiter/Login.html')
