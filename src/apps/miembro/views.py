# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Q
from models import Miembro
from actividad.models import Evento, Noticia, Informe

def listar(request):
    miembros_permanentes = Miembro.objects.filter(Q(activo = True), Q(permanente = True)).order_by('iniciales')
    miembros_invitados = Miembro.objects.filter(Q(activo = True), Q(permanente = False)).order_by('iniciales')
    return render(request, 'miembro/lista.html', {'miembros_permanentes':miembros_permanentes,
                                                'miembros_invitados':miembros_invitados,
                                                'app':'miembro',
                                                'eventos' : Evento.get_eventos(),
                                                'noticias' : Noticia.get_noticias(),
                                                'informes':Informe.get_informes(),})
