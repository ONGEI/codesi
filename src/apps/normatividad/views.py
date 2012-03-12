# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Q
from models import Nomatividad

def listar(request, categoria):
    normas = Nomatividad.objects.filter(Q(categoria = categoria), Q(autorizado = True)).order_by('-pk')
    return render(request, 'normatividad/normas.html', {'normas' : normas,'categoria' : categoria,'app' : 'normatividad',})

def datelle(request, categoria, norma):
    norma = Nomatividad.objects.get(Q(pk = norma), Q(autorizado = True))
    return render(request, 'normatividad/norma.html', {'norma' : norma,'categoria' : categoria,'app' : 'normatividad',})
