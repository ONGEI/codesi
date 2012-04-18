# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db.models import Q
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
    list_display      = ('perfil','equipo','grupo','coordinador',)
    #search_fields     = ['entidad','contacto']
    list_filter       = ('coordinador',)
    list_per_page     = 25
    list_max_show_all = 30

    def queryset(self, request):
        qs = super(IntegranteAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(equipo__in = Integrante.objects.filter(perfil = request.user.get_profile()))

    #def add_view(self, request, form_url='', extra_context=None):
        #self.fields = ('title','content','only_users','authorize') if Integrate.objects.get(request.user.is_superuser) else ('title','content','only_users')
        #print dir(self.form)
    #    return super(IntegranteAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, extra_context=None):
        if not request.user.is_superuser:
            me = Integrante.objects.get(perfil=request.user.get_profile())
            self.fields = ('perfil','equipo','grupo','coordinador','retirado',) if me.coordinador and me.grupo == Integrante.objects.get(pk=object_id).grupo else ('perfil','equipo',)
        return super(IntegranteAdmin, self).change_view(request, object_id, extra_context=None)

    def save_model(self, request, obj, form, change):
        if not obj.activo:
            obj.perfil.user.is_staff = False
            obj.perfil.user.save()
        obj.save()

admin.site.register(Integrante, IntegranteAdmin)
