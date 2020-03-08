from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Agenda

# Create your views here.

def agenda(request):
    agendas = Agenda.objects.order_by('data')
    return render(request,'agenda/index.html', {'agendas': agendas})
    