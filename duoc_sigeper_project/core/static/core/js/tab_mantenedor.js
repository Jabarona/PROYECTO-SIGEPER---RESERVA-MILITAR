document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const tab = urlParams.get('tab');
    
    if (tab) {
        // Selecciona la pestaña correspondiente usando el parámetro `tab`
        const tabButton = document.querySelector(`[data-bs-target="#admin-${tab}"]`);
        if (tabButton) {
        const activeTab = document.querySelector('.nav-link.active');
        if (activeTab) {
            activeTab.classList.remove('active');
        }
        tabButton.classList.add('active');
        
        const activeTabContent = document.querySelector('.tab-pane.show.active');
        if (activeTabContent) {
            activeTabContent.classList.remove('show', 'active');
        }
        
        const tabContent = document.querySelector(`#admin-${tab}`);
        if (tabContent) {
            tabContent.classList.add('show', 'active');
        }
        }
    }
    });
