from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    message='salut tout le monde'
    return HttpResponse (message)
     #render ('request',('store/index.html')),