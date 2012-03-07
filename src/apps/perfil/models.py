# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime

class Perfil(models.Model):
    usuario           = models.OneToOneField(User)
    dni                  = models.CharField('D.N.I.', max_length = 8, blank = False, null =False, unique = True)
    entidad           = models.CharField('Entidad', max_length = 250, blank = False, null =False)
    cargo              = models.CharField('Coordinador', max_length = 250, blank = False, null =False)
    acerca_de_mi = models.TextField('Acerca de mi')
    fecha_registro = models.DateTimeField('Fecha de Registro', default = datetime.datetime.today(), editable = False)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'