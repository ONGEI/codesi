# -*- coding: utf-8 -*-
from django.contrib import admin
#from sorl.thumbnail.admin import AdminImageMixin
from models import Reunion, Informe, Noticia, Evento, Slide

class ReunionAdmin(admin.ModelAdmin):
    list_display      = ('titulo','publicado','fecha')
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
    list_display      = ('titulo','publicado','fecha', 'ano')
    search_fields     = ['titulo']
    list_per_page     = 25
    list_max_show_all = 30

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.publicado = request.user.get_profile()
        obj.save()

admin.site.register(Informe, InformeAdmin)

class NoticiaAdmin(admin.ModelAdmin):
    list_display      = ('titulo','publicado','fecha','fuente','vista_previa',)
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

class EventoAdmin(admin.ModelAdmin):
    list_display      = ('titulo','publicado','inicio','fin','direccion','vista_previa')
    search_fields     = ['titulo',]
    list_display_links = ('titulo',)
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

class SlideAdmin(admin.ModelAdmin):
    #list_display      = ('publicado', 'titulo','inicio','fin','direccion','vista_previa')
    search_fields     = ['titulo',]
    list_per_page     = 25
    list_max_show_all = 30

admin.site.register(Slide, SlideAdmin)
