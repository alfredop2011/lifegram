
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def hello_World(request):
    return HttpResponse('Hello, World')

urlpatterns = [
    path('hello-world/', hello_World),
 
]
