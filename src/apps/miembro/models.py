# -*- coding: utf-8 -*-
from django.db import models

class Miembro(models.Model):
    iniciales   = models.CharField('Iniciales', max_length = 10, blank = False, null =  False)
    entidad     = models.CharField('Entidad', max_length = 200, blank = False, null =  False)
    portal      = models.URLField('Portal Institucional',blank = True, null =  True)
    permanente  = models.BooleanField('Permanente', default = False)
    activo      = models.BooleanField('Activo', default = True)

    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'

    def __unicode__(self):
        return u'%s' % (self.iniciales)
