from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print('control came to views.py')
    return HttpResponse("<h1>welcome to pyspiders</h1>")

def ht(request):
    return render(request,"sam1.html")

def ht1(request):
    return render(request,"sample1.html")