# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import force_unicode
import datetime

class Perfil(models.Model):
    user           = models.OneToOneField(User)
    dni            = models.CharField('D.N.I.', max_length = 8, blank = False, null =False, unique = True)
    entidad        = models.CharField('Entidad', max_length = 250, blank = False, null =False)
    cargo          = models.CharField('Cargo', max_length = 250, blank = False, null =False)
    acerca_de_mi   = models.TextField('Acerca de mi',blank = True, null =True)
    fecha_registro = models.DateTimeField('Fecha de Registro', default = datetime.datetime.today(), editable = False)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __unicode__(self):
        return u'%s, %s' % (
                        force_unicode(self.user.last_name, encoding='utf-8', strings_only=False, errors='strict'),
                        force_unicode(self.user.first_name, encoding='utf-8', strings_only=False, errors='strict')
                        )
