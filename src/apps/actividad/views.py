# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Integrante, Reunion, Informe, Noticia, Evento

def eventos(request):
    eventos_codesi = Evento.objects.all().order_by('-pk')
    return render(request, 'actividad/eventos.html', {'eventos':Evento.get_eventos(),'eventos_codesi':eventos_codesi,'notas' : Noticia.get_noticias(),})

def notas(request):
    notas_codesi = Nota.objects.all().order_by('-pk')
    return render(request, 'actividad/noticias.html', {'eventos':Evento.get_eventos(),'notas_codesi':notas_codesi,'notas' : Noticia.get_noticias(),})

def nota(request, nota):
    nota = Nota.objects.get(pk = nota)
    return render(request, 'actividad/noticia.html', {'eventos':Evento.get_eventos(),'nota':nota,'notas' : Noticia.get_noticias(),})
