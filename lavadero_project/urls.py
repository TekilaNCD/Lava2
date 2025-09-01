# lavadero_project/urls.py

from django.contrib import admin
from django.urls import path, include

# Esta es la lista que Django usa para buscar las rutas de URL.
urlpatterns = [
    # Ruta para el panel de administración de Django.
    path('admin/', admin.site.urls),
    
    # La línea más importante: conecta tu proyecto con las URLs de tu app 'usuarios'.
    path('', include('usuarios.urls')),
]
