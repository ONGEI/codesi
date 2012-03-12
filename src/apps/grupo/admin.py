# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Grupo, Integrante, Reunion, Documento, Nota, Evento

class GrupoAdmin(admin.ModelAdmin):
    list_display      = ('numero','nombre','funcionario')
    search_fields     = ['nombre']
    list_filter       = ('numero',)
    list_per_page     = 25
    list_max_show_all = 30

admin.site.register(Grupo, GrupoAdmin)

class IntegranteAdmin(admin.ModelAdmin):
    list_display      = ('grupo','publicado','entidad','contacto','cargo','telefono','email')
    search_fields     = ['entidad','contacto']
    list_per_page     = 25
    list_max_show_all = 30

admin.site.register(Integrante, IntegranteAdmin)

class ReunionAdmin(admin.ModelAdmin):
    list_display      = ('grupo','publicado','titulo','fecha')
    search_fields     = ['titulo']
    list_per_page     = 25
    list_max_show_all = 30

admin.site.register(Reunion, ReunionAdmin)

class DocumentoAdmin(admin.ModelAdmin):
    list_display      = ('grupo','publicado','titulo','fecha')
    search_fields     = ['titulo']
    list_per_page     = 25
    list_max_show_all = 30

admin.site.register(Documento, DocumentoAdmin)

class NotaAdmin(admin.ModelAdmin):
    list_display      = ('grupo','publicado','titulo','fecha','fuente','foto')
    search_fields     = ['titulo','fuente']
    list_per_page     = 25
    list_max_show_all = 30

admin.site.register(Nota, NotaAdmin)

class EventoAdmin(admin.ModelAdmin):
    list_display      = ('grupo','titulo','inicio','fin','foto')
    search_fields     = ['titulo',]
    list_per_page     = 25
    list_max_show_all = 30

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                'filebrowser/js/FB_TinyMCE.js',
                'filebrowser/js/TinyMCEAdmin.js',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.publicado = request.user.get_profile()
        obj.save()

admin.site.register(Evento, EventoAdmin)
