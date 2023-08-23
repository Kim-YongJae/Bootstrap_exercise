from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1")
    return response