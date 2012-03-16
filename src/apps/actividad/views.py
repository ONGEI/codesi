# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Integrante, Reunion, Informe, Noticia, Evento
import datetime

def eventos(request):
    eventos_codesi = Evento.objects.filter(inicio__year = datetime.datetime.today().year).order_by('-pk')
    return render(request, 'actividad/eventos.html', {'eventos':Evento.get_eventos(),'eventos_codesi':eventos_codesi,'notas' : Noticia.get_noticias(),'app':'evento',})

def notas(request):
    notas_codesi = Noticia.objects.all().order_by('-pk')
    return render(request, 'actividad/noticias.html', {'eventos':Evento.get_eventos(),'notas_codesi':notas_codesi,'notas' : Noticia.get_noticias(),'app':'noticia',})

def nota(request, nota):
    nota = Nota.objects.get(pk = nota)
    return render(request, 'actividad/noticia.html', {'eventos':Evento.get_eventos(),'nota':nota,'notas' : Noticia.get_noticias(),'app':'noticia',})

def informes(request):
    informes_codesi = Informe.objects.filter(ano = str(datetime.datetime.today().year))
    return render(request, 'actividad/informes.html', {'eventos':Evento.get_eventos(),'informes':informes_codesi,'notas' : Noticia.get_noticias(),'app':'informe',})
