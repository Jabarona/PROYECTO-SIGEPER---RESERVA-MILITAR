document.addEventListener("DOMContentLoaded", function () {
    initializeCustomSelects();
    initializeTabs();
});

function initializeTabs() {
    const tabLinks = document.querySelectorAll('a[data-bs-toggle="tab"]');
    tabLinks.forEach(tab => {
        tab.addEventListener('shown.bs.tab', function (event) {
            initializeCustomSelects();
        });
    });
}

function initializeCustomSelects() {
    const customSelectContainers = document.querySelectorAll(".custom-select-container");

    customSelectContainers.forEach(container => {
        const input = container.querySelector(".custom-select-input");
        const clearButton = container.querySelector(".custom-select-clear");
        const optionsContainer = container.querySelector(".custom-select-options");
        const options = optionsContainer.querySelectorAll(".custom-option");
        const originalSelect = container.querySelector(".original-select");

        input.addEventListener("click", (e) => {
            e.stopPropagation();
            toggleDropdown(container);
        });

        document.addEventListener("click", (e) => {
            if (!container.contains(e.target)) {
                closeDropdown(container);
            }
        });

        input.addEventListener("input", (e) => {
            const filter = e.target.value.trim().toLowerCase();
            
            options.forEach((option) => {
                const text = option.textContent.trim().toLowerCase();
                option.style.display = text.includes(filter) ? "block" : "none";
            });
        });

        options.forEach((option) => {
            option.addEventListener("click", () => {
                selectOption(container, option);
            });
        });

        clearButton.addEventListener("click", (e) => {
            e.stopPropagation();
            clearSelection(container);
        });

        // Inicializar el valor del input si hay una opción seleccionada
        const selectedOption = originalSelect.options[originalSelect.selectedIndex];
        if (selectedOption && selectedOption.value) {
            input.value = selectedOption.text;
            clearButton.style.display = "block";
        }
    });
}

function toggleDropdown(container) {
    const isOpen = container.classList.contains("open");
    closeAllDropdowns();
    if (!isOpen) {
        container.classList.add("open");
    }
}

function closeDropdown(container) {
    container.classList.remove("open");
}

function closeAllDropdowns() {
    document.querySelectorAll(".custom-select-container").forEach(container => {
        container.classList.remove("open");
    });
}

function selectOption(container, option) {
    const input = container.querySelector(".custom-select-input");
    const originalSelect = container.querySelector(".original-select");
    const clearButton = container.querySelector(".custom-select-clear");
    const value = option.getAttribute("data-value").trim();
    const text = option.textContent.trim();

    input.value = text;
    
    // Actualizar el valor del select original
    originalSelect.value = value;

    // Actualizar la opción seleccionada en el select original
    Array.from(originalSelect.options).forEach((opt) => {
        opt.selected = opt.value === value;
    });

    // Disparar un evento de cambio en el select original
    const event = new Event('change', { bubbles: true });
    originalSelect.dispatchEvent(event);

    container.querySelectorAll(".custom-option").forEach((opt) => opt.classList.remove("selected"));
    option.classList.add("selected");

    closeDropdown(container);
    clearButton.style.display = "block";

    console.log("Valor seleccionado:", value); // Para depuración
}

function clearSelection(container) {
    const input = container.querySelector(".custom-select-input");
    const originalSelect = container.querySelector(".original-select");
    const clearButton = container.querySelector(".custom-select-clear");

    input.value = "";
    originalSelect.value = "";

    // Deseleccionar todas las opciones en el select original
    Array.from(originalSelect.options).forEach((opt) => {
        opt.selected = false;
    });

    // Disparar un evento de cambio en el select original
    const event = new Event('change', { bubbles: true });
    originalSelect.dispatchEvent(event);

    clearButton.style.display = "none";
    container.querySelectorAll(".custom-option").forEach((opt) => opt.classList.remove("selected"));

    console.log("Selección limpiada"); // Para depuración
}

// Agregar un event listener al formulario para verificar los valores antes de enviar
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        const customSelects = this.querySelectorAll('.custom-select-container');
        customSelects.forEach(container => {
            const originalSelect = container.querySelector('.original-select');
            const input = container.querySelector('.custom-select-input');
            console.log(`Formulario enviado - Select: ${originalSelect.name}, Valor: ${originalSelect.value}, Input: ${input.value}`);
        });
    });
});