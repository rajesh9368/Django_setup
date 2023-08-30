from django.shortcuts import render
from django.http import HttpResponse
def register(request):
    s='<h1>Register Page</h1>'
    return HttpResponse(s)
# Create your views here.
