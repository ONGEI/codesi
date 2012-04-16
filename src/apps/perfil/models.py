# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import force_unicode
#from equipo.models import Equipo
from miembro.models import Miembro
import datetime

#STATUS = (
#    (0,'Participante'),
#    (1,'Coordinador'),
#    )

class Perfil(models.Model):
    entidad        = models.ForeignKey(Miembro)
    user           = models.OneToOneField(User)
    dni            = models.CharField('D.N.I.', max_length = 8, blank = False, null = False)
    cargo          = models.CharField('Cargo', max_length = 250, blank = False, null =False)
    telefono       = models.CharField('Teléfono', max_length = 25, blank = True, null =True)
    acerca_de_mi   = models.TextField('Acerca de mi',blank = True, null =True)
    fecha_registro = models.DateTimeField('Fecha de Registro', default = datetime.datetime.today(), editable = False)

    #grupo          = models.ForeignKey(Grupo, blank = True, null = True)
    #contacto       = models.CharField('Apellido y Nombres', max_length = 250, blank = True, null = True)
#    entidad   = models.CharField('Entidad/Empresa', max_length = 250, blank = False, null =False)
#    contacto  = models.CharField('Contacto', max_length = 250, blank = False, null =False)
#    cargo     = models.CharField('Cargo', max_length = 250, blank = False, null =False)
#    direccion = models.CharField('Dirección', max_length = 250)
#    telefono  = models.CharField('Teléfono', max_length = 25)
#    email     = models.EmailField('E-Mail', blank = False, null = False)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __unicode__(self):
        return u'%s, %s' % (
                        force_unicode(self.user.last_name, encoding='utf-8', strings_only=False, errors='strict'),
                        force_unicode(self.user.first_name, encoding='utf-8', strings_only=False, errors='strict')
                        )

    #def mi_grupo(self):
    #    if self.grupo:
    #        return u'%s' % self.grupo
    #    return u'CODESI Admin'
