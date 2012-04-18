# -*- coding: utf-8 -*-
from django.db import models
from projectadmin.models import Proyecto
from django.contrib.auth.models import Group
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

    #def get_integrantes(self):
    #    return self.integrante_set.filter()
    def get_coordinador(self):
        return self.integrante_set.get(coordinador=True)

class Integrante(models.Model):
    #publicado   = models.ForeignKey(Perfil, editable = False)
    perfil      = models.ForeignKey(Perfil)
    equipo      = models.ForeignKey(Equipo)
    grupo       = models.ForeignKey(Group)
    coordinador = models.BooleanField('¿Es Coordinador?',default = False)
    activo      = models.BooleanField('¿Activo?',default = True)

    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'

    def __unicode__(self):
        return u'%s' % (self.perfil)
