from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def about(request):
    return HttpResponse("<h1>This is my about page.</h1>")


def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")


def sum(request, num1, num2):
    return HttpResponse(f"Sum of {num1} and {num2} are {num1+num2}")
