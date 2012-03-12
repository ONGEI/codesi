# -*- coding: utf-8 -*-
from django.db import models
from perfil.models import Perfil
import datetime

class Grupo(models.Model):
    funcionario = models.ForeignKey(Perfil)
    numero      = models.CharField('Número de Grupo',max_length = 20, blank = False, null =False, default = 'Grupo N°', unique = True)
    nombre      = models.CharField('Nombre del Grupo', max_length = 180, blank = False, null =False)
    alcances    = models.TextField('Alcances', blank = False, null =False)

    class Meta:
        verbose_name = 'Grupo de Trabajo'
        verbose_name_plural = 'Grupos de Trabajo'

    #def __unicode__(self):
    #    return u'%s' % (self.iniciales)

class Integrante(models.Model):
    grupo     = models.ForeignKey(Grupo)
    publicado = models.ForeignKey(Perfil, editable = False)
    entidad   = models.CharField('Entidad/Empresa', max_length = 250, blank = False, null =False)
    contacto  = models.CharField('Contacto', max_length = 250, blank = False, null =False)
    cargo     = models.CharField('Cargo', max_length = 250, blank = False, null =False)
    direccion = models.CharField('Dirección', max_length = 250)
    telefono  = models.CharField('Teléfono', max_length = 25)
    email     = models.EmailField('E-Mail', blank = False, null = False)

    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'

class Reunion(models.Model):
    grupo       = models.ForeignKey(Grupo)
    publicado   = models.ForeignKey(Perfil, editable = False)
    titulo      = models.CharField('Reunión', max_length = 250, blank = False, null =False)
    fecha       = models.DateField('Fecha', blank = False, null =False)
    asistente   = models.TextField('Asistentes')
    descripcion = models.TextField('Descripción')

    class Meta:
        verbose_name = 'Reunión'
        verbose_name_plural = 'Reuniones'

    def __unicode__(self):
        return u'%s' % (self.titulo)

class Documento(models.Model):
    grupo       = models.ForeignKey(Grupo)
    publicado   = models.ForeignKey(Perfil, editable = False)
    titulo      = models.CharField('Reunión', max_length = 250, blank = False, null =False)
    documento   = models.TextField('Documento', blank = False, null =False)
    fecha       = models.DateField('Fecha de publicación', default = datetime.date.today(), editable = False)
    descripcion = models.TextField('Descripción')

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __unicode__(self):
        return u'%s' % (self.titulo)

class Nota(models.Model):
    grupo     = models.ForeignKey(Grupo, blank = True, null = True)
    publicado = models.ForeignKey(Perfil, editable = False)
    titulo    = models.CharField('Título', max_length = 250, blank = False, null =False)
    cuerpo    = models.TextField('Nota', blank = False, null =False)
    fecha     = models.DateField('Fecha de publicación', default = datetime.date.today(), editable = False)
    foto      = models.ImageField(upload_to = 'fotos/')
    fuente    = models.CharField('Fuente', max_length = 20, blank = False, null =False)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

    def __unicode__(self):
        return u'%s' % (self.titulo)

    @staticmethod
    def get_notas():
        return Nota.objects.all().order_by('-pk')[:3]

class Evento(models.Model):
    grupo       = models.ForeignKey(Grupo, blank = True, null = True)
    titulo      = models.CharField('Título', max_length = 250, blank = False, null =False)
    inicio      = models.DateTimeField('Fecha de inicio', default = datetime.datetime.today())
    fin         = models.DateTimeField('Fecha de culminación', default = datetime.datetime.today())
    descripcion = models.TextField('Descripción', blank = False, null = False)
    foto        = models.ImageField(upload_to = 'fotos/', blank = True, null = True)
    publicacion = models.DateTimeField('Fecha de publicación', default = datetime.datetime.today(), editable = False)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __unicode__(self):
        return u'%s' % (self.titulo)

    @staticmethod
    def get_eventos():
        return Evento.objects.all().order_by('-pk')[:2]

