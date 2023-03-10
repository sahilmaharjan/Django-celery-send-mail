from django.shortcuts import render, HttpResponse

# Create your views here.
def home():
    a = 10/0
    return HttpResponse("Hello")