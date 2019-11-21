from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print("control came to views.py")
    return HttpResponse("<h1>welcome to pyspiders</h1>")

def home(request):
    return HttpResponse("<h1>welcome</h1>")

def suhas(request):
    return render(request,'sam.html')