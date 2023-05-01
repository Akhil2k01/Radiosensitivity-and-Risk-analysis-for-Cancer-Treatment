from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('cregister', views.cregister, name='cregister'),
    path('pform', views.pform, name='pform'),
    path('help', views.help , name='help'),
] 