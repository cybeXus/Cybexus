from django.shortcuts import render
from .models import Formation

def home(request):
    formations = Formation.objects.all() 
    return render(request, 'home/index.html', {'formations': formations})
