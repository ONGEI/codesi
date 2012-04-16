# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Perfil
from forms import PerfilForm

class PerfilAdmin(admin.ModelAdmin):
    list_display      = ('user','entidad','dni','cargo')
    search_fields     = ['dni','entidad','cargo']
    list_per_page     = 25
    list_max_show_all = 30
    form              = PerfilForm

    def save_model(self, request, obj, form, change):
        obj.user.first_name = form.cleaned_data.get('nombres')
        obj.user.last_name = form.cleaned_data.get('apellidos')
        obj.user.is_staff = form.cleaned_data.get('ingresar')
        obj.user.email = form.cleaned_data.get('email')
        obj.user.save()
        obj.save()

admin.site.register(Perfil, PerfilAdmin)
