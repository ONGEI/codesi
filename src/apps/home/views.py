# -*- coding: utf-8 -*-
from django.shortcuts import render
from grupo.models import Evento, Nota

def index(request):
    return render(request,'home/index.html',{'eventos' : Evento.get_eventos()})
