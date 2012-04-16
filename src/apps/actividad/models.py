# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import force_unicode
#from sorl.thumbnail import ImageField
from perfil.models import Perfil
import datetime

class Reunion(models.Model):
    publicado   = models.ForeignKey(Perfil, editable = False)
    titulo      = models.CharField('Reunión', max_length = 250, blank = False, null =False)
    fecha       = models.DateField('Fecha', blank = False, null =False)
    asistente   = models.TextField('Asistentes')
    descripcion = models.TextField('Descripción')

    class Meta:
        verbose_name = 'Reunion'
        verbose_name_plural = 'Reuniones'

    def __unicode__(self):
        return u'%s' % (self.titulo)

class Informe(models.Model):
    publicado   = models.ForeignKey(Perfil, editable = False)
    titulo      = models.CharField('Informe', max_length = 250, blank = False, null =False)
    documento   = models.TextField('Documento', blank = False, null =False)
    fecha       = models.DateField('Fecha de publicación', default = datetime.date.today(), editable = False)
    ano         = models.CharField('Año',max_length = 4, default = datetime.date.today().year)
    descripcion = models.TextField('Descripción', blank = True, null = True)

    class Meta:
        verbose_name = 'Informe'
        verbose_name_plural = 'Informes'

    def __unicode__(self):
        return u'%s' % (force_unicode(self.titulo, encoding='utf-8', strings_only=False, errors='strict'),)

    def get_titulo(self):
        return self.titulo.replace(' ', '_')

    @staticmethod
    def get_informes():
        a = Informe.objects.values('ano').order_by('-ano').distinct()[:2]
        if a:
            return (Informe.objects.filter(ano = a[0]['ano']).order_by('-pk')[:3],Informe.objects.filter(ano = a[1]['ano']).order_by('-pk')[:3],[a[0]['ano'],a[1]['ano']],)
        return None

class Noticia(models.Model):
    publicado = models.ForeignKey(Perfil, editable = False)
    titulo    = models.CharField('Título', max_length = 250, blank = False, null =False)
    cuerpo    = models.TextField('Noticia', blank = False, null =False)
    fecha     = models.DateField('Fecha de publicación', default = datetime.date.today(), editable = False)
    foto      = models.CharField('Thumb', max_length = 250, blank = True, null = True)
    fuente    = models.CharField('Fuente', max_length = 20, blank = False, null =False)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __unicode__(self):
        return u'%s' % (self.titulo)

    def get_titulo(self):
        return u'%s' % self.titulo.replace(' ', '_')

    def vista_previa(self):
        if self.foto:
            return '<img src="%s" alt="thumb" heigth="50px" width="50px"/>' % self.foto
        return u''
    vista_previa.allow_tags = True

    @staticmethod
    def get_noticias():
        return Noticia.objects.all().order_by('-pk')[:2]

class Evento(models.Model):
    publicado   = models.ForeignKey(Perfil)
    titulo      = models.CharField('Título', max_length = 250, blank = False, null =False)
    direccion   = models.CharField('Dirección', max_length = 255, blank = False, null =False)
    inicio      = models.DateTimeField('Fecha de inicio', default = datetime.datetime.today())
    fin         = models.DateTimeField('Fecha de culminación', default = datetime.datetime.today())
    descripcion = models.TextField('Descripción', blank = False, null = False)
    foto        = models.ImageField('Foto', upload_to = 'uploads/fotos/', blank = True, null = True)
    publicacion = models.DateTimeField('Fecha de publicación', default = datetime.datetime.today(), editable = False)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __unicode__(self):
        return u'%s' % (self.titulo)

    def vista_previa(self):
        if self.foto:
            return '<img src="/media/%s" alt="thumb" heigth="50px" width="50px"/>' % "#"
        return u''
    vista_previa.allow_tags = True

    @staticmethod
    def get_eventos():
        return Evento.objects.all().order_by('-pk')[:2]

class Slide(models.Model):
    evento      = models.ForeignKey(Evento)
    titulo      = models.CharField('Título', max_length = 250, blank = False, null =False)
    descripcion = models.CharField('Descripcion', max_length = 255, blank = False, null =False)
    portada     = models.URLField('Portada', blank = False, null =False)
    foto_1      = models.URLField('Foto', blank = False, null =False)
    foto_2      = models.URLField('Foto', blank = False, null =False)
    foto_3      = models.URLField('Foto', blank = False, null =False)
    foto_4      = models.URLField('Foto', blank = False, null =False)

    def __unicode__(self):
        return u'%s' % (self.titulo)
