from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def login(request):
   template = loader.get_template('login.html')
   res=template.render()
   return HttpResponse(res)
# Create your views here.
