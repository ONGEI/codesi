# -*- coding: utf-8 -*-
from django.contrib import admin
#from sorl.thumbnail.admin import AdminImageMixin
from models import Objetivo

class ObjetivoAdmin(admin.ModelAdmin):
    list_display      = ('responsable','proyecto','peticion','creado_por','asignado_a','creado','terminado','prioridad','estado',)
    #search_fields     = ['peticion__asunto']
    list_per_page     = 25
    list_max_show_all = 30

    #def save_model(self, request, obj, form, change):
    #    if not obj.pk:
    #        obj.publicado = request.user.get_profile()
    #    obj.save()

admin.site.register(Objetivo, ObjetivoAdmin)