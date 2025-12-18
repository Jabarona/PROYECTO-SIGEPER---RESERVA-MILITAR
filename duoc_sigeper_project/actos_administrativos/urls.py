from django.urls import path
from .views import *

urlpatterns = [
    
    #URL de mantenedor de resoluciones 
    path('ingreso_resolucion/', IngresoResolucionView.as_view()  ,name='ingreso_resolucion'),
    
    #URLs de resolución de condecoraciones
    path('res_condecoracion/', ResolucionMedallaListView.as_view(), name='list_res_condecoracion'),
    path('update-res_condecoracion/<int:pk>',ResolucionMedallaUpdate.as_view(), name='update_res_condecoracion'),
    path('delete-res_condecoracion/<int:pk>/', ResolucionMedallaDelete.as_view(), name='delete_res_condecoracion'),
    
    
    #URLs de resoluciones de nombramientos y ascensos
    path('res_ascenso/', ResolucionAscensoListView.as_view(), name='list_res_ascenso'),
    path('update-res_ascenso/<int:pk>',ResolucionAscensoUpdate.as_view(), name='update_res_ascenso'),
    path('delete-res_ascenso/<int:pk>/', ResolucionAscensoDelete.as_view(), name='delete_res_ascenso'),
    path('search_ascensos/', SearchResAscensoView.as_view(), name='search_ascensos'),
    
    #URLs de cambio de escalafón
    path('res_escalafon/', ResolucionCambioEscalafonListView.as_view(), name='list_res_escalafon'),
    path('update-res_escalafon/<int:pk>',ResolucionCambioEscalafonUpdate.as_view(), name='update_res_escalafon'),
    path('delete-res_escalafon/<int:pk>/', ResolucionCambioEscalafonDelete.as_view(), name='delete_res_escalafon'),
    
    #URLs de cambio de institución
    path('res_institucion/', ResolucionCambioInstitucionListView.as_view(), name='list_res_institucion'),
    path('update-res_institucion/<int:pk>',ResolucionCambioInstitucionUpdate.as_view(), name='update_res_institucion'),
    path('delete-res_institucion/<int:pk>/', ResolucionCambioInstitucionDelete.as_view(), name='delete_res_institucion'),
    
    #URL para descargar archivos PDF.    
    path('gestion/descargar_documento/<str:model>/<int:pk>/', DescargarDocumentoGenericaView.as_view(), name='descargar_documento'),
]
