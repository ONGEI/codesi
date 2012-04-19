# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render
from models import Equipo, Integrante
from objetivo.models import Objetivo
from actividad.models import Evento, Noticia, Informe

def listar(request, equipo):
    equipo = Equipo.objects.get(pk = equipo)
    objetivos = equipo.objetivo_set.all()
    integrantes = Integrante.objects.filter(Q(equipo=equipo),Q(activo=True)).order_by('perfil__entidad__entidad')
    coordinador = integrantes.get(coordinador=True)
    return render(
                    request,
                    'equipo/equipo.html',
                    {
                        'equipo':equipo,
                        'objetivos':objetivos,
                        'integrantes':integrantes,
                        'coordinador':coordinador,
                        'eventos' : Evento.get_eventos(),
                        'noticias' : Noticia.get_noticias(),
                        'informes':Informe.get_informes(),
                    }
                )
