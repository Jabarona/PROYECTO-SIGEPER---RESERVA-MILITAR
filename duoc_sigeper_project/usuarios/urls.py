from django.urls import path
from .views import *

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('user-create/', CreateUserView.as_view(), name='user_create'), 
    path('user-list/', UserListView.as_view(), name='user_list'),
    path('user-update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-change-password/', ProfileChangePasswordView.as_view(), name='profile_change_password'),
    path('profile-edit/', ProfileEditView.as_view(), name='profile_edit'),    
    path('verificar-2fa/', Verificar2FAView.as_view(), name='verificar_2fa'),
]
