# -*- coding: utf-8 -*-
from django.shortcuts import render
from actividad.models import Evento, Nota

def index(request):
    return render(request,'home/index.html',{'eventos' : Evento.get_eventos(),'notas' : Nota.get_notas(),})
