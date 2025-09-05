# usuarios/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Enlace con el modelo User de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # --- DATOS PERSONALES ---
    # Corresponde a: <input type="file" id="profilePic">
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True, verbose_name="Foto de Perfil")
    
    # Corresponde a: <input type="text" id="nombre"> y <input type="text" id="apellido">
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    # Corresponde a: <select id="tipoDocumento">
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
        ('DE', 'Documento de Identidad Extranjero'),
    ]
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO_CHOICES, verbose_name="Tipo de Documento")
    
    # Corresponde a: <input type="text" id="numeroDocumento">
    numero_documento = models.CharField(max_length=50, unique=True, verbose_name="Número de Documento")

    # --- DATOS DE PAGO ---
    # Corresponde a: <select id="metodoPago">
    METODO_PAGO_CHOICES = [
        ('TC', 'Tarjeta de Crédito'),
        ('TD', 'Tarjeta Débito'),
        ('EF', 'Efectivo'),
        ('TB', 'Transferencia Bancaria'),
        ('ND', 'Nequi/Daviplata'),
    ]
    metodo_pago = models.CharField(max_length=2, choices=METODO_PAGO_CHOICES, verbose_name="Método de Pago")
    
    # Corresponde a: <input type="text" id="numeroCuenta"> (Opcional)
    numero_cuenta = models.CharField(max_length=50, blank=True, null=True, verbose_name="Número de Cuenta")

    # --- DATOS DEL VEHÍCULO ---
    # Corresponde a: <input type="text" id="modeloMarca">
    modelo_marca_vehiculo = models.CharField(max_length=100, verbose_name="Modelo y Marca del Vehículo")
    
    # Corresponde a: <input type="text" id="placa">
    placa_vehiculo = models.CharField(max_length=10, verbose_name="Placa del Vehículo")
    
    # Corresponde a: <input type="text" id="tipoCarro">
    tipo_vehiculo = models.CharField(max_length=50, verbose_name="Tipo de Carro")

    # --- DATOS DE UBICACIÓN ---
    # Corresponde a: <input type="text" id="ciudad"> y <input type="text" id="direccion">
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    # --- DATOS ADICIONALES ---
    # Corresponde a: <textarea id="cuidadoEspecial">
    cuidado_especial = models.TextField(blank=True, null=True, verbose_name="Cuidado Especial del Vehículo")
    
    # Corresponde a: <input type="checkbox" id="terms">
    acepta_terminos = models.BooleanField(default=False, verbose_name="Acepta Términos y Condiciones")

    def __str__(self):
        return f'Perfil de {self.user.username}'


# En usuarios/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # --- CAMPO NUEVO PARA EL ROL DEL USUARIO ---
    TIPO_USUARIO_CHOICES = [
        ('cliente', 'Cliente'),
        ('empleado', 'Empleado'),
        ('admin', 'Administrador'),
    ]
    # ¡AQUÍ ESTÁ LA MAGIA!
    # Por defecto, todos los nuevos perfiles serán 'cliente'.
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO_CHOICES,
        default='cliente',
        verbose_name="Tipo de Usuario"
    )

    # --- TUS CAMPOS EXISTENTES (sin cambios) ---
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True, verbose_name="Foto de Perfil")
    nombre = models.CharField(max_length=100)
    # ... (el resto de tus campos: apellido, tipo_documento, etc.)
    # ...
    acepta_terminos = models.BooleanField(default=False, verbose_name="Acepta Términos y Condiciones")

    def __str__(self):
        # Podemos mejorar esto para ver el tipo de usuario en el admin
        return f'Perfil de {self.user.username} ({self.get_tipo_usuario_display()})'
