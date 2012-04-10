# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Perfil

class PerfilAdmin(admin.ModelAdmin):
    #list_display      = ('user','mi_grupo','dni','entidad','cargo')
    search_fields     = ['dni','entidad','cargo']
    list_per_page     = 25
    list_max_show_all = 30

#admin.site.register(Perfil, PerfilAdmin)
