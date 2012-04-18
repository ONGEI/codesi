# -*- coding: utf-8 -*-
from django.db import models
from equipo.models import Equipo
from projectadmin.models import Peticion

class Objetivo(models.Model):
    peticion = models.ForeignKey(Peticion)
    grupo    = models.ForeignKey(Equipo)

    def __unicode__(self):
        return u'Objetivo: %s' % self.peticion.asunto

    def proyecto(self):
        return u'%s' % self.peticion.proyecto.nombre

    def creado(self):
        return u'%s' % self.peticion.creado_fecha

    def terminado(self):
        return u'%s' % self.peticion.terminado_fecha

    def creado_por(self):
        return u'%s' % self.peticion.creado_por.get_full_name()

    def asignado_a(self):
        return u'%s' % self.peticion.asignado_a.get_full_name()

    def estado(self):
        return u'%s' % self.peticion.get_estado()

    def prioridad(self):
        return u'%s' % self.peticion.get_prioridad()

class Comentario(models.Model):
    objetivo   = models.ForeignKey(Objetivo)
    comentario = models.CharField('Comentario', max_length=140, null=False, blank=False)
    respuetsa  = models.ForeignKey('self', related_name='+', blank = True, null = True)
    aprovado   = models.BooleanField('¿Aprovado?', default=False)

    def __unicode__(self):
        return u'%s' % self.objetivo
