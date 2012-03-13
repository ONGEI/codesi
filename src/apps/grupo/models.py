# -*- coding: utf-8 -*-
from django.db import models

class Grupo(models.Model):
    numero      = models.CharField('Número de Grupo',max_length = 20, blank = False, null =False, default = 'Grupo N°', unique = True)
    nombre      = models.CharField('Nombre del Grupo', max_length = 180, blank = False, null =False)
    alcances    = models.TextField('Alcances', blank = False, null =False)

    class Meta:
        verbose_name = 'Grupo de Trabajo'
        verbose_name_plural = 'Grupos de Trabajo'

    def __unicode__(self):
        return u'%s - %s' % (self.numero, self.nombre)
