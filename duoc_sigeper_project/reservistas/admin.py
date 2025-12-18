from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ReservistaModel

@admin.register(ReservistaModel)
class ReservistaAdmin(ImportExportModelAdmin):
    pass
