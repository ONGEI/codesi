# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Miembro

class MiembroAdmin(admin.ModelAdmin):
    list_display      = ('iniciales','entidad','permanente','activo')
    search_fields     = ['iniciales','entidad']
    list_filter       = ('permanente','activo')
    list_per_page     = 25
    list_max_show_all = 30

#admin.site.register(Miembro, MiembroAdmin)
