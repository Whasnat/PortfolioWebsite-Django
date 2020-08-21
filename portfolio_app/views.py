from django.shortcuts import render
from .models import Projects

def home(request):
    projects = Projects.objects.all()
    return render(request, 'portfolio_app/home.html', {'projects': projects}) 