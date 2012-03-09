# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import force_unicode
from perfil.models import Perfil 

CATEGORIA = (
             (0,'Oficial'),
             (1,'Relacionados Nacionales'),
             (2,'Relacionados Internacionales'),
             (3,'Acuerdos y Reuniones'),
             (4,'Presentaciones'),
             )

class Nomatividad(models.Model):
    publicado    = models.ForeignKey(Perfil, editable = False, default = 0)
    categoria    = models.IntegerField('Categoría', choices = CATEGORIA)
    titulo       = models.CharField('Título', max_length = 200, blank = False, null = False)
    descripcion  = models.TextField('Descripción', blank = True, null = True)
    presentacion = models.TextField('Presentación', blank = False, null = False)
    autorizado   = models.BooleanField('Autorizado', default = False)

    class Meta:
        verbose_name = 'Normatividad'
        verbose_name_plural = 'Normatividades'

    def __unicode__(self):
        return u'%s' % (
                        force_unicode(self.titulo, encoding='utf-8', strings_only=False, errors='strict'),
                        )

    def get_categoria(self):
        return u'%s' % categoria[self.categoria][1]
