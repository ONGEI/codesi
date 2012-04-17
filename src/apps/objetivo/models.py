from django.db import models
from perfil.models import Perfil
from projectadmin.models import Peticion

class Objetivo(models.Model):
    responsable = models.ForeignKey(Perfil)
    peticion    = models.ForeignKey(Peticion)

    def proyecto(self):
        return u'%s' % self.peticion.proyecto.nombre

    def creado(self):
        return u'%s' % self.peticion.creado_fecha

    def terminado(self):
        return u'%s' % self.peticion.terminado_fecha

    def creado_por(self):
        return u'%s' % self.peticion.creado_por.get_full_name()

    def asignado_a(self):
        return u'%s' % self.peticion.asignado_a.get_full_name()

    def estado(self):
        return u'%s' % self.peticion.get_estado()

    def prioridad(self):
        return u'%s' % self.peticion.get_prioridad()
