from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    """Home page"""
    return HttpResponse('<html><title>To-Do</title></html>')
