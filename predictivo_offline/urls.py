from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('mediciones/<str:pk>', views.mediciones, name='mediciones'),
    path('arbol_equipos', views.arbolEquipos, name='arbol_equipos'),
]
