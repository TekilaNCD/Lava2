# usuarios/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm # Asegúrate de tener este archivo con el UserProfileForm

def registro(request):
    """
    PASO 1 del registro: Crea el usuario y la contraseña.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Guarda el nuevo usuario en la base de datos
            user = form.save()
            
            # ¡CAMBIO CLAVE 1!
            # Inicia sesión automáticamente para que el siguiente paso
            # (completar datos) sepa a qué usuario pertenece el perfil.
            login(request, user)
            
            # ¡CAMBIO CLAVE 2!
            # Redirige al usuario a la nueva vista para completar datos,
            # en lugar de a 'login'.
            return redirect('completar_datos')
    else:
        form = UserCreationForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})

# --- VISTA NUEVA ---
@login_required # Protege esta vista. Solo un usuario logueado puede completarla.
def completar_datos_view(request):
    """
    PASO 2 del registro: Recoge y guarda los datos adicionales del perfil.
    """
    if request.method == 'POST':
        # Pasamos request.FILES para poder manejar la subida de archivos (la foto)
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile if hasattr(request.user, 'userprofile') else None)
        if form.is_valid():
            # Creamos una instancia del perfil pero no la guardamos todavía
            profile = form.save(commit=False)
            # Asignamos el usuario que está actualmente logueado
            profile.user = request.user
            # Ahora sí guardamos el perfil completo en la base de datos
            profile.save()
            
            messages.success(request, '¡Tu perfil se ha completado exitosamente!')
            # Una vez completado, redirigimos al dashboard final
            return redirect('dashboard')
    else:
        form = UserProfileForm()

    return render(request, 'usuarios/completarDatos.html', {'form': form})

@login_required
def dashboard(request):
    """
    Muestra la página principal al usuario después de iniciar sesión y completar el perfil.
    """
    return render(request, 'usuarios/dashboard.html')

