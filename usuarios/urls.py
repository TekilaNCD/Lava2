# usuarios/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views # Importamos nuestras vistas personalizadas (la de registro)

urlpatterns = [
    # Ruta para la página principal: usa la vista de Login de Django
    path('', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='home'),
    
    # Ruta para el login: también usa la vista de Login de Django
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),

    # Ruta para el registro: usa nuestra vista personalizada 'registro'
    path('registro/', views.registro, name='registro'),

    # Ruta para el logout: usa la vista de Logout de Django
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),

    # Ruta para el dashboard: usa nuestra vista personalizada 'dashboard'
    path('dashboard/', views.dashboard, name='dashboard'),

    # NUEVA RUTA para completar datos adicionales después del registro
    path('completar-datos/', views.completar_datos_view, name='completar_datos'),

]