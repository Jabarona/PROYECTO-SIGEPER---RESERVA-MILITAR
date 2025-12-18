from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('correo', 'nombre', 'apellido_paterno', 'is_staff')
    list_filter = ('is_admin', 'is_divper','is_uac', 'is_ubm','is_lector' ,'is_staff')
    fieldsets = (
        (None, {'fields': ('correo', 'password')}),
        ('Personal Info', {'fields': ('nombre', 'apellido_paterno', 'apellido_materno', 'unidad', 'grado', 'foto', 'citofono')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_admin', 'is_divper', 'is_uac', 'is_ubm', 'is_lector')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('correo','password1', 'password2')}
        ),
    )
    search_fields = ('correo',)
    ordering = ('correo',)



admin.site.register(CustomUser, CustomUserAdmin)