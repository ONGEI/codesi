# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Integrante, Reunion, Documento, Nota, Evento

def eventos(request):
    eventos_codesi = Evento.objects.all().order_by('-pk')
    return render(request, 'actividad/eventos.html', {'eventos':Evento.get_eventos(),'eventos_codesi':eventos_codesi,})

def notas(request):
    notas = Nota.objects.all().order_by('-pk')
    return render(request, 'actividad/notas.html')
