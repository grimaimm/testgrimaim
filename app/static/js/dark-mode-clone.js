
var themeToggleDarkIconn = document.getElementById('theme-toggle-dark-iconn');
var themeToggleLightIconn = document.getElementById('theme-toggle-light-iconn');

// Change the icons inside the button based on previous settings
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    themeToggleLightIconn.classList.remove('hidden');
} else {
    themeToggleDarkIconn.classList.remove('hidden');
}

var themeToggleBtnn = document.getElementById('theme-togglee');

themeToggleBtnn.addEventListener('click', function() {

    // toggle icons inside button
    themeToggleDarkIconn.classList.toggle('hidden');
    themeToggleLightIconn.classList.toggle('hidden');

    // if set via local storage previously
    if (localStorage.getItem('color-theme')) {
        if (localStorage.getItem('color-theme') === 'light') {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        }

    // if NOT set via local storage previously
    } else {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        }
    }
    
});