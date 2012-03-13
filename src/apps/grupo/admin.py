# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Grupo

class GrupoAdmin(admin.ModelAdmin):
    list_display      = ('numero','nombre',)
    search_fields     = ['nombre']
    list_filter       = ('numero',)
    list_per_page     = 25
    list_max_show_all = 30

admin.site.register(Grupo, GrupoAdmin)
