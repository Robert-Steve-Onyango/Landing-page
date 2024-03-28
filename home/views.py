from django.shortcuts import render
from django.http import HttpResponse

def curso(request):
    return render(request, 'land.html')
    
