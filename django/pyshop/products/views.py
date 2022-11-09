from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#need to map the url to this function
def index(request):
    return HttpResponse('Hello World')
