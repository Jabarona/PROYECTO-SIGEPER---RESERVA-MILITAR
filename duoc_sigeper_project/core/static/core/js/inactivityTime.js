let inactivityTime = function () {
    let time;
    const maxInactivity = 20 * 60 * 1000; // 20 minutos
    const warningTime = 19 * 60 * 1000;  // 19 minutos
    let warningShown = false;  // Variable para controlar si la alerta ya se mostró

    window.onload = resetTimer;
    document.onmousemove = resetTimer;
    document.onkeypress = resetTimer;
    document.onscroll = resetTimer;
    document.onclick = resetTimer;

    function logout() {
        window.location.href = logoutUrl; 
    }

    function showWarning() {
        if (!warningShown) {  // Verificar si ya se mostró la alerta
            alert("Has estado inactivo durante 19 minutos. Tu sesión se cerrará en 1 minuto si no interactúas.");
            warningShown = true;  // Marcar que la alerta fue mostrada
        }
    }

    function resetTimer() {
        clearTimeout(time);
        time = setTimeout(logout, maxInactivity); 
        setTimeout(showWarning, warningTime);    
    }
};

inactivityTime();

