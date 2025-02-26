const sidebar = document.getElementById('sidebar');
const content = document.getElementById('main-content');
const toggleButton = document.getElementById('toggle-sidebar');
const toggleButtonIcon = document.getElementById('toggle-sidebar-icon');

function saveSidebarState(isClosed) {
    localStorage.setItem('sidebarState', isClosed ? 'closed' : 'open');
}

function loadSidebarState() {
    const savedState = localStorage.getItem('sidebarState');
    if (savedState === 'open') {
        sidebar.classList.add('open');
        sidebar.classList.remove('closed');
    } else {
        sidebar.classList.add('closed');
        sidebar.classList.remove('open');
    }
}

toggleButton.addEventListener('click', () => {
    const isClosed = sidebar.classList.toggle('closed');
    sidebar.classList.toggle('open');
    saveSidebarState(isClosed);
});

document.addEventListener('DOMContentLoaded', loadSidebarState);


