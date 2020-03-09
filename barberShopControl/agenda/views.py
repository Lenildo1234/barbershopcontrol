from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Agenda

def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def agendamento(request):
    return render(request, 'agendamento.html')
    

def agenda(request):
    agendas = Agenda.objects.order_by('data')
    return render(request,'agenda/index.html', {'agendas': agendas})
    
