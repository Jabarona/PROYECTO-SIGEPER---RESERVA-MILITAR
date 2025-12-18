document.addEventListener("DOMContentLoaded", function () {
    const passwordField = document.getElementById("id_password"); // ⚠️ Usa el ID real del input
    const togglePassword = document.getElementById("toggle-password");
    const passwordIcon = document.getElementById("password-icon");

    if (passwordField && togglePassword && passwordIcon) {
        togglePassword.addEventListener("click", function () {
            if (passwordField.type === "password") {
                passwordField.type = "text";
                passwordIcon.classList.replace("bi-eye-slash", "bi-eye");
            } else {
                passwordField.type = "password";
                passwordIcon.classList.replace("bi-eye", "bi-eye-slash");
            }
        });
    } else {
        console.error("⚠️ Elemento no encontrado:", { passwordField, togglePassword, passwordIcon });
    }
});