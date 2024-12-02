from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def auto(request):
    return HttpResponse('<h1>badget friendly auto ride</h1>')
def car(request):
    return render(request,'car.html')
