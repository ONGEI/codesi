# -*- coding: utf-8 -*-
from django.db import models
from perfil.models import Perfil 

CATEGORIA = (
             (0,'Ofiacial',)
             (1,'Relacionados Nacionales'),
             (2,'Relacionados Internacionales'),
             (3,'Acuerdos y Reuniones'),
             (4,'Presentaciones'),
             )

class Nomatividad(models.Model):
    publicado         = models.ForeignKey(Perfil)
    categoria          = models.IntegerField('Categoría', choices = CATEGORIA)
    titulo                  = models.CharField('Título', max_length = 200, blank = False, null = False)
    descripcion      = models.TextField('Descripción')
    presentacion  = models.TextField('Presentación', blank = False, null = False)
    autorizado       = models.BooleanField('Autorizado', default = False)

    class Meta:
        verbose_name = 'Normatividad'
        verbose_name_plural = 'Normatividades'