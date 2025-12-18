from django.contrib import admin
from .models import *

# Register your models here.
class AfpAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class IsapeAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class CiudadAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class ArmaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class EstadoCivilAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class GradoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class GrupoSanguineoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class ProfesionAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class ReligionAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class UacAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class UbmAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class CondecoracionAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')
    
class UnidadAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

admin.site.register(AFPModel, AfpAdmin)
admin.site.register(ISAPREModel, IsapeAdmin)
admin.site.register(CiudadModel, CiudadAdmin)
admin.site.register(ArmaServicioModel, ArmaAdmin)
admin.site.register(EstadoCivilModel, EstadoCivilAdmin)
admin.site.register(GradoModel, GradoAdmin)
admin.site.register(GrupoSanguineoModel, GrupoSanguineoAdmin)
admin.site.register(ProfesionModel, ProfesionAdmin)
admin.site.register(ReligionModel, ReligionAdmin)
admin.site.register(UACModel, UacAdmin)
admin.site.register(UBMModel, UbmAdmin)
admin.site.register(ConedecoracionModel, CondecoracionAdmin)
admin.site.register(categoriaModel, CategoriaAdmin)
admin.site.register(UnidadModel, UnidadAdmin)

