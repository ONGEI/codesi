# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Equipo, Integrante

class EquipoAdmin(admin.ModelAdmin):
    list_display      = ('numero','nombre',)
    search_fields     = ['nombre']
    list_filter       = ('numero',)
    list_per_page     = 25
    list_max_show_all = 30

    def queryset(self, request):
        qs = super(EquipoAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(pk__in = Integrante.objects.values('equipo').filter(perfil = request.user.get_profile()))

admin.site.register(Equipo, EquipoAdmin)

class IntegranteAdmin(admin.ModelAdmin):
    list_display      = ('perfil','equipo','coordinador')
    #search_fields     = ['entidad','contacto']
    list_filter       = ('coordinador',)
    list_per_page     = 25
    list_max_show_all = 30

    def queryset(self, request):
        qs = super(IntegranteAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(equipo__in = Integrante.objects.filter(perfil = request.user.get_profile()))

    #def save_model(self, request, obj, form, change):
    #    if not obj.pk:
    #        obj.publicado = request.user.get_profile()
    #    obj.save()

admin.site.register(Integrante, IntegranteAdmin)
