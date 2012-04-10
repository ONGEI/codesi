# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Integrante, Reunion, Informe, Noticia, Evento
import datetime

def eventos(request, date_year = datetime.datetime.today().year):
    eventos_codesi = Evento.objects.filter(inicio__year = date_year).order_by('-pk')
    return render(request, 'actividad/eventos.html', {'eventos':Evento.get_eventos(),
                                                    'eventos_codesi':eventos_codesi,
                                                    'noticias' : Noticia.get_noticias(),
                                                    'app':'evento',
                                                    'informes':Informe.get_informes(),})

def noticias(request, date_year = datetime.datetime.today().year):
    noticias_codesi = Noticia.objects.filter(fecha__year = date_year).order_by('-pk')
    return render(request, 'actividad/noticias.html', {'eventos':Evento.get_eventos(),
                                                    'noticias_codesi':noticias_codesi,
                                                    'noticias' : Noticia.get_noticias(),
                                                    'app':'noticia',
                                                    'informes':Informe.get_informes(),})

def noticia(request, noticia):
    noticia = Noticia.objects.get(pk = noticia)
    return render(request, 'actividad/noticia.html', {'eventos':Evento.get_eventos(),
                                                    'noticia':noticia,
                                                    'noticias' : Noticia.get_noticias(),
                                                    'app':'noticia',
                                                    'informes':Informe.get_informes(),})

def informes(request, date_year = datetime.datetime.today().year):
    informes_codesi = Informe.objects.filter(ano = str(date_year)).order_by('-pk')
    return render(request, 'actividad/informes.html', {'eventos':Evento.get_eventos(),
                                                    'informes_codesi':informes_codesi,
                                                    'noticias':Noticia.get_noticias(),
                                                    'app':'informe',
                                                    'informes':Informe.get_informes(),})

def informe(request, informe):
    informe = Informe.objects.get(pk = informe)
    return render(request, 'actividad/informe.html', {'eventos':Evento.get_eventos(),
                                                    'informe':informe,
                                                    'noticias':Noticia.get_noticias(),
                                                    'app':'informe',
                                                    'informes':Informe.get_informes(),})
