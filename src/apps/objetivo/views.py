# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from models import Objetivo, Comentario
from forms import ComentarioForm
from actividad.models import Evento, Noticia, Informe

def describir(request, objetivo):
    comentarioform = ComentarioForm()
    if request.method == 'POST':
        comentarioform = ComentarioForm(request.POST)
        if comentarioform.is_valid():
            comentarioform.save()
            return redirect('objetivo.views.describir',objetivo=objetivo)
    objetivo = Objetivo.objects.get(pk = objetivo)
    comentarios = objetivo.comentario_set.filter(aprovado=True)
    return render(
                request,
                'objetivo/objetivo.html',
                {
                    'objetivo': objetivo,
                    'comentarios':comentarios,
                    'comentarioform' : comentarioform,
                    'eventos' : Evento.get_eventos(),
                    'noticias' : Noticia.get_noticias(),
                    'informes': Informe.get_informes(),
                }
                )
