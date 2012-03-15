# -*- coding: utf-8 -*-
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from models import Integrante, Reunion, Informe, Noticia, Evento

class IntegranteAdmin(admin.ModelAdmin):
    list_display      = ('publicado','entidad','contacto','cargo','telefono','email')
    search_fields     = ['entidad','contacto']
    list_per_page     = 25
    list_max_show_all = 30

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.publicado = request.user.get_profile()
        obj.save()

admin.site.register(Integrante, IntegranteAdmin)

class ReunionAdmin(admin.ModelAdmin):
    list_display      = ('publicado','titulo','fecha')
    search_fields     = ['titulo']
    list_per_page     = 25
    list_max_show_all = 30
    exclide           = ["publicado"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.publicado = request.user.get_profile()
        obj.save()

admin.site.register(Reunion, ReunionAdmin)

class InformeAdmin(admin.ModelAdmin):
    list_display      = ('publicado','titulo','fecha', 'ano')
    search_fields     = ['titulo']
    list_per_page     = 25
    list_max_show_all = 30

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.publicado = request.user.get_profile()
        obj.save()

admin.site.register(Informe, InformeAdmin)

class NoticiaAdmin(admin.ModelAdmin):
    list_display      = ('publicado','titulo','fecha','fuente','vista_previa',)
    search_fields     = ['titulo','fuente']
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

admin.site.register(Noticia, NoticiaAdmin)

class EventoAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display      = ('publicado', 'titulo','inicio','fin','direccion','vista_previa')
    search_fields     = ['titulo',]
    list_per_page     = 25
    list_max_show_all = 30
    exclude           = ["publicado",]

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                'filebrowser/js/FB_TinyMCE.js',
                'filebrowser/js/TinyMCEAdmin.js',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.publicado = request.user.get_profile()
        obj.save()

admin.site.register(Evento, EventoAdmin)
