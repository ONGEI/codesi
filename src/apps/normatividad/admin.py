# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Nomatividad

class NomatividadAdmin(admin.ModelAdmin):
    list_display   = ('publicado','categoria','titulo','autorizado')
    search_fields  = ['titulo','categoria']
    list_filter = ('autorizado')
    list_per_page = 25
    list_max_show_all = 30

admin.site.register(Nomatividad, NomatividadAdmin)