# -*- coding: utf-8 -*-
from django.db import models

class Miembro(models.Model):
    iniciales = models.CharField('Iniciales', max_length = 5, blank = False, null =  False)
    entidad   = models.CharField('Entidad', max_length = 200, blank = False, null =  False)
    invitado  = models.BooleanField('Invitado', default = False)

    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'
