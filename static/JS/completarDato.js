// static/js/form-validation.js
document.addEventListener('DOMContentLoaded', () => {
    // --- LÓGICA PARA LA FOTO DE PERFIL ---
    const fileInput = document.getElementById('profilePic');
    const previewImg = document.getElementById('preview');

    if (fileInput && previewImg) {
        fileInput.addEventListener('change', function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    previewImg.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // --- LÓGICA PARA LA VALIDACIÓN DEL FORMULARIO ---
    const personalForm = document.getElementById('personalForm');
    const errorMessage = document.getElementById('form-error-message');

    if (personalForm) {
        personalForm.addEventListener('submit', function(event) {
            // Prevenimos el envío automático para poder validar
            event.preventDefault();

            let isValid = true;
            const requiredFields = personalForm.querySelectorAll('[required]');

            // Limpiamos errores anteriores
            errorMessage.style.display = 'none';
            document.querySelectorAll('.input-error').forEach(el => el.classList.remove('input-error'));
            
            // Verificamos cada campo requerido
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('input-error'); // Añadimos clase de error
                }
            });

            // Verificamos el checkbox de términos
            const termsCheckbox = document.getElementById('terms');
            if (termsCheckbox && !termsCheckbox.checked) {
                isValid = false;
                // Estilo simple para el label del checkbox si no está marcado
                termsCheckbox.parentElement.style.color = '#ffcdd2';
            } else if (termsCheckbox) {
                termsCheckbox.parentElement.style.color = ''; // Resetea el color
            }


            // Si todo es válido, se envía el formulario. Si no, se muestra un error.
            if (isValid) {
                personalForm.submit();
            } else {
                errorMessage.textContent = 'Por favor, completa todos los campos obligatorios y acepta los términos.';
                errorMessage.style.display = 'block';
            }
        });
    }
});
