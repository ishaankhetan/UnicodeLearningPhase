from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def home(request):
    return HttpResponse('PERSONAL MANAGEMENT')
