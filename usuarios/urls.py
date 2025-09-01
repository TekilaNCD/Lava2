# usuarios/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Este es el archivo que define las rutas específicas de la app 'usuarios'
urlpatterns = [
    # Ruta para la página de registro
    path('registro/', views.registro, name='registro'),
    
    # Rutas para el login y el logout, usando las vistas que Django ya tiene
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]
