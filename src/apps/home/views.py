# -*- coding: utf-8 -*-
from django.shortcuts import render
from actividad.models import Evento, Noticia, Informe

def index(request):
    return render(request,'home/index.html',{'eventos' : Evento.get_eventos(),
                                            'noticias' : Noticia.get_noticias(),
                                            'informes':Informe.get_informes(),})
