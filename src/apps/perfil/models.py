# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime

class Perfil(models.Model):
    usuario              = models.OneToOneField(User)
    acerca_de_mi    = models.TextField('Acerca de mi')
    fecha_registro  = models.DateTimeField('Fecha de Registro', default = datetime.datetime.today(), editable = False)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'