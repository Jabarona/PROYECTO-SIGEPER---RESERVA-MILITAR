from django.urls import path
from .views import *

urlpatterns = [
    # Mantenedor
    path('', MantenedorView.as_view(), name='mantenedor'),
    
    #URLS de AFP
    path('list-afp/', AFPListView.as_view(), name='list_afp'),
    path('update-afp/<int:pk>',AfpUpdate.as_view(), name='update_afp'),
    path('delete-afp/<int:pk>/', AfpDelete.as_view(), name='delete_afp'),
    
    #URLS de arma    
    path('list-arma/', ArmaListView.as_view(), name='list_arma'),
    path('update-arma/<int:pk>',ArmaUpdate.as_view(), name='update_arma'),
    path('delete-arma/<int:pk>/', ArmaDelete.as_view(), name='delete_arma'),
    
    #URLS de ciudad
    path('list-ciudad/',CiudadListView.as_view(), name='list_ciudad'),
    path('update-ciudad/<int:pk>',CiudadUpdate.as_view(), name='update_ciudad'),
    path('delete-ciudad/<int:pk>/', CiudadDelete.as_view(), name='delete_ciudad'),
    
    #URLS de estado civil
    path('list-estado_civil/', EstadoCivilListView.as_view(), name='list_estado_civil'),
    path('update-estado_civil/<int:pk>',EstadoCivilUpdate.as_view(), name='update_estado_civil'),
    path('delete-estado_civil/<int:pk>/', EstadoCivilDelete.as_view(), name='delete_estado_civil'),
    
    #URLS de grado
    path('list-grado/', GradoListView.as_view(), name='list_grado'),
    path('update-grado/<int:pk>',GradoUpdate.as_view(), name='update_grado'),
    path('delete-grado/<int:pk>/', GradoDelete.as_view(), name='delete_grado'),
    
    #URLS de ISAPRE
    path('list-isapre/', ISAPREListView.as_view(), name='list_isapre'),
    path('update-isapre/<int:pk>',ISAPREUpdate.as_view(), name='update_isapre'),
    path('delete-isapre/<int:pk>/', ISAPREDelete.as_view(), name='delete_isapre'),
    
    #URLS de profesión
    path('list-profesion/', ProfesionListView.as_view(), name='list_profesion'),
    path('update-profesion/<int:pk>',ProfesionUpdate.as_view(), name='update_profesion'),
    path('delete-profesion/<int:pk>/', ProfesionDelete.as_view(), name='delete_profesion'),
    
    #URLS de religión
    path('list-religion/', ReligionListView.as_view(), name='list_religion'),
    path('update-religion/<int:pk>',ReligionUpdate.as_view(), name='update_religion'),
    path('delete-religion/<int:pk>/', ReligionDelete.as_view(), name='delete_religion'),
    
    #URLS de UAC
    path('list-uac/', UACListView.as_view(), name='list_uac'),
    path('update-uac/<int:pk>',UACUpdate.as_view(), name='update_uac'),
    path('delete-uac/<int:pk>/', UACDelete.as_view(), name='delete_uac'),
    
    #URLS de UBM
    path('list-ubm/', UBMListView.as_view(), name='list_ubm'),
    path('update-ubm/<int:pk>',UBMUpdate.as_view(), name='update_ubm'),
    path('delete-ubm/<int:pk>/', UBMDelete.as_view(), name='delete_ubm'),
    
    #URLS de grupo sanguineo
    path('list-grupo_sanguineo/', GrupoSanguineoListView.as_view(), name='list_grupo_sanguineo'),
    path('update-grupo_sanguineo/<int:pk>',GrupoSanguineoUpdate.as_view(), name='update_grupo_sanguineo'),
    path('delete-grupo_sanguineo/<int:pk>/', GrupoSanguineoDelete.as_view(), name='delete_grupo_sanguineo'),
    
    #URLS de medalla
    path('list-medalla/', MedallaListView.as_view(), name='list_medalla'),
    path('update-medalla/<int:pk>',MedallaUpdate.as_view(), name='update_medalla'),
    path('delete-medalla/<int:pk>/', MedallaDelete.as_view(), name='delete_medalla'),
    
    #URLS de categoria
    path('list-categoria/', CategoriaListView.as_view(), name='list_categoria'),
    path('update-categoria/<int:pk>',CategoriaUpdate.as_view(), name='update_categoria'),
    path('delete-categoria/<int:pk>/', CategoriaDelete.as_view(), name='delete_categoria'),
    
    #URLS de unidad
    path('list-unidad/', UnidadListView.as_view(), name='list_unidad'),
    path('update-unidad/<int:pk>',UnidadUpdate.as_view(), name='update_unidad'),
    path('delete-unidad/<int:pk>/', UnidadDelete.as_view(), name='delete_unidad'),
]
