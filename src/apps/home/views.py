# -*- coding: utf-8 -*-
from django.shortcuts import render
from actividad.models import Evento, Noticia, Informe, Slide
import datetime

def index(request):
    slides = Slide.objects.all().order_by('-id')[:3]
    return render(request,'home/index.html',{'eventos' : Evento.get_eventos(),
                                            'noticias' : Noticia.get_noticias(),
                                            'informes': Informe.get_informes(),
                                            'slides' : slides})
