from django.shortcuts import render

# Create your views here.

def index(request):
    d = {'name' : 'abu', 'age': 10}
    return render(request,'first_app/index.html', context=d) 