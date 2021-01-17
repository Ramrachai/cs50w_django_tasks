from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def home(req): 
    return HttpResponse("<h1> hello blog </h1>")


def greet(req, kk ):
    return render(req, 'hello/greet.html' , {
        "yoyo" : kk.capitalize()
    } )
