# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Nomatividad

class NomatividadAdmin(admin.ModelAdmin):
    list_display      = ('titulo','publicado','categoria','autorizado')
    search_fields     = ['titulo','categoria']
    list_filter       = ('autorizado',)
    list_per_page     = 25
    list_max_show_all = 30

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.publicado = request.user.get_profile()
        obj.save()

admin.site.register(Nomatividad, NomatividadAdmin)
