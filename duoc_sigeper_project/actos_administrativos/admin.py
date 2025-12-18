from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(ResolucionAscenso)
class ResolucionAscensoAdmin(ImportExportModelAdmin):
    pass

@admin.register(ResolucionCambioEscalafon)
class ResolucionCambioEscalafonAdmin(ImportExportModelAdmin):
    pass

@admin.register(ResolucionCambioInstitucion)
class ResolucionCambioInstitucionAdmin(ImportExportModelAdmin):
    pass

@admin.register(ResolucionMedalla)
class ResolucionMedallaAdmin(ImportExportModelAdmin):
    pass