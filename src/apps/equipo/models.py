# -*- coding: utf-8 -*-
from django.db import models
from projectadmin.models import Proyecto
from perfil.models import Perfil

class Equipo(models.Model):
    numero   = models.CharField('Número de Grupo',max_length = 20, blank = False, null =False, default = 'Grupo N°', unique = True)
    nombre   = models.CharField('Nombre del Grupo', max_length = 180, blank = False, null =False)
    proyecto = models.ForeignKey(Proyecto)
    alcances = models.TextField('Alcances', blank = False, null =False)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __unicode__(self):
        return u'%s - %s' % (self.numero, self.nombre)

class Integrante(models.Model):
    #publicado   = models.ForeignKey(Perfil, editable = False)
    perfil      = models.ForeignKey(Perfil)
    equipo      = models.ForeignKey(Equipo)
    coordinador = models.BooleanField('¿Es Coordinador?',default = False)

    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'
