from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def agenda(request):
    return render(request,'agenda/index.html')
    