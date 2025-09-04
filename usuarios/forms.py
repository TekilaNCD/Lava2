# usuarios/forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # Incluye todos los campos de tu modelo UserProfile EXCEPTO el campo 'user'.
        # El campo 'user' lo asignaremos automáticamente en la vista.
        exclude = ['user']

