from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def agendamento(request):
    return render(request, 'agendamento.html')
 