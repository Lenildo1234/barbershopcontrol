from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def agenda(request):
    return HttpResponse("Página de agendamentos")
    