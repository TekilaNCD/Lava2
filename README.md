🚗 LAVA2 - Plataforma de Gestión de Lavado de Autos
¡Bienvenido a LAVA2! Este proyecto es una aplicación web completa, desarrollada con Python y el framework Django, diseñada para gestionar los servicios y clientes de un lavadero de autos moderno. La plataforma permite a los usuarios registrarse, gestionar sus datos personales y de sus vehículos, y prepararse para interactuar con los servicios del lavadero.

Este proyecto ha sido desarrollado como parte del curso de Ingeniería de Software, aplicando la arquitectura MVT (Modelo-Vista-Template) y las mejores prácticas de desarrollo con Django.

✨ Características Principales
Sistema de Autenticación Completo:

Registro de Usuarios en 2 Pasos: Un flujo de registro profesional donde los usuarios primero crean sus credenciales (usuario y contraseña) y luego son guiados a una página para completar su perfil detallado.

Inicio y Cierre de Sesión Seguro: Utiliza el sistema de autenticación robusto y probado de Django.

Gestión de Perfil Extendido: Los usuarios pueden registrar información detallada, incluyendo datos personales, de contacto, y especificaciones de sus vehículos.

Interfaz de Usuario Moderna y Responsiva:

Diseño Profesional: Formularios estilizados con un look moderno y limpio, utilizando tonos azules que reflejan la identidad de la marca.

Validación en el Frontend: Scripts de JavaScript que validan los datos en tiempo real antes de ser enviados al servidor, mejorando la experiencia del usuario.

Backend Robusto y Escalable:

Arquitectura MVT: Código organizado siguiendo el patrón Modelo-Vista-Template de Django para una fácil mantenibilidad.

Base de Datos en la Nube: Conectado a una instancia de PostgreSQL alojada en Render, demostrando la capacidad de la aplicación para funcionar en un entorno de producción.

Gestión de Archivos Estáticos y Multimedia: Configuración optimizada para servir archivos CSS, JavaScript e imágenes de perfil de usuario.

🛠️ Tecnologías Utilizadas
Backend:

Python 3.12

Django 5.2.5

Psycopg2-binary: Conector para la base de datos PostgreSQL.

Pillow: Biblioteca para el procesamiento de imágenes (fotos de perfil).

Frontend:

HTML5

CSS3 (con un diseño que incluye efectos modernos como Glassmorphism).

JavaScript (ES6): Para validaciones de formularios del lado del cliente.

Base de Datos:

PostgreSQL (alojada en Render).

🚀 Cómo Empezar
Para poner en marcha este proyecto en un entorno de desarrollo local, sigue estos pasos:

Prerrequisitos
Tener Python 3.10+ instalado.

Tener pip (el gestor de paquetes de Python) instalado.

Instalación
Clona el repositorio:

bash
git clone [URL-DE-TU-REPOSITORIO]
cd LAVA2
(Opcional pero recomendado) Crea y activa un entorno virtual:

bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate
Instala las dependencias:
El archivo requirements.txt contiene todas las bibliotecas de Python necesarias.

bash
pip install -r requirements.txt
(Nota: Si no tienes un requirements.txt, puedes instalar las dependencias manualmente: pip install Django psycopg2-binary Pillow)

Configura las variables de entorno:
Este proyecto está configurado para conectarse a una base de datos externa. Asegúrate de que la sección DATABASES en lavadero_project/settings.py apunte a tu instancia de base de datos.

Aplica las migraciones:
Este comando creará todas las tablas necesarias en tu base de datos.

bash
python manage.py makemigrations
python manage.py migrate
¡Ejecuta el servidor de desarrollo!

bash
python manage.py runserver
¡Y listo! Abre tu navegador y visita http://127.0.0.1:8000/ para ver la aplicación en acción.
