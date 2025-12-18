from django.urls import path
from .views import *

urlpatterns = [
    # Gestión de la Reserva
    path('list-reservista/', ReservistaListView.as_view(), name='list_reservista'),
    path('exportar-reservistas/', ExportReservistasExcelView.as_view(), name='exportar_reservistas'),
    path('search-reservista/', SearchReservistaView.as_view(), name='search_reservista'),
    
    path('reservista/<int:pk>/', ProfileReservistaView.as_view(), name='profile_reservista'),
    path('reservista-update/<int:pk>/', ProfileReservistaUpdate.as_view(), name='profile_reservista-update'),
    path('reservista-delete/<int:pk>/', ProfileReservistaDelete.as_view(), name='profile_reservista-delete'),
    path('reservista', ProfileReservistaCreate.as_view(), name='profile_reservista-create'),
]
