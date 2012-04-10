# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Q
from models import Nomatividad
from actividad.models import Evento, Noticia, Informe

def listar(request, categoria):
    normas = Nomatividad.objects.filter(Q(categoria = categoria), Q(autorizado = True)).order_by('-pk')
    return render(request, 'normatividad/normas.html', {'normas' : normas,
                                                        'categoria' : categoria,
                                                        'app' : 'normatividad',
                                                        'eventos' : Evento.get_eventos(),
                                                        'noticias' : Noticia.get_noticias(),
                                                        'informes':Informe.get_informes(),})

def datelle(request, categoria, norma):
    norma = Nomatividad.objects.get(Q(pk = norma), Q(autorizado = True))
    return render(request, 'normatividad/norma.html', {'norma' : norma,
                                                        'categoria' : categoria,
                                                        'app' : 'normatividad',
                                                        'eventos' : Evento.get_eventos(),
                                                        'noticias' : Noticia.get_noticias(),
                                                        'informes':Informe.get_informes(),})
