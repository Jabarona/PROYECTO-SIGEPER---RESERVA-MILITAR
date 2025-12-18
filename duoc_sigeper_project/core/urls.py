from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler404

urlpatterns = [
    # Core
    path('', IndexTemplateView.as_view(), name='index'),
    path('faq/', FaqTemplateView.as_view(), name='faq'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('error404/', Error404Views.as_view(), name='error404'),
]