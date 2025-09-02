// Validación del formulario de registro
document.getElementById("registerForm")?.addEventListener("submit", function(e) {
  e.preventDefault();
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirmPassword").value;

  if (password !== confirmPassword) {
    alert("Las contraseñas no coinciden");
    return;
  }

  alert("Registro exitoso, ahora completa tus datos personales");
  window.location.href = "datos_personales.html"; // redirige al siguiente form
});

// Validación del formulario de datos personales
document.getElementById("personalForm")?.addEventListener("submit", function(e) {
  e.preventDefault();
  if (!document.getElementById("terminos").checked) {
    alert("Debes aceptar los términos y condiciones");
    return;
  }

  alert("Datos guardados correctamente");
  // Aquí después se manda al backend de Django con fetch() o axios
});
