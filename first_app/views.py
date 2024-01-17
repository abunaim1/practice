from django.shortcuts import render
from django.http import HttpResponse
import datetime 
# Create your views here.

def home(request):
    d = {
        'name' : 'abu naim abdullah',
        'age' : 20,
        'courses' : ['python', 'JS', 'C', 'C++', 'C#'],
        'enroll_date' : datetime.datetime.now(),
        'empty' : '',
    }
    return render(request, 'first_app/home.html',context=d)

def about(request):
    return render(request, 'first_app/about.html')

def service(request):
    return render(request, 'first_app/service.html')