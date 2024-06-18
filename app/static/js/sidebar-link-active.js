document.addEventListener('DOMContentLoaded', function() {
    // Get the current path from the URL
    var currentPath = window.location.pathname;

    function toggleRotationClass(linkId, activeCondition) {
        var link = document.getElementById(linkId);
        if (link) {
            link.classList.toggle('group-hover:-rotate-12', !activeCondition);
            link.classList.toggle('-rotate-12', activeCondition);
        }
    }

    // Home link
    var homeLink = document.getElementById('home-link');
    if (homeLink) {
        homeLink.classList.toggle('text-neutral-900', currentPath === '/');
        homeLink.classList.toggle('dark:!text-neutral-200', currentPath === '/');
        homeLink.classList.toggle('bg-neutral-200', currentPath === '/');
        homeLink.classList.toggle('dark:bg-neutral-800', currentPath === '/');
        homeLink.classList.toggle('lg:hover:gap-4', currentPath !== '/');
        homeLink.classList.toggle('hover:text-neutral-900', currentPath !== '/');
        homeLink.classList.toggle('hover:dark:text-neutral-300', currentPath !== '/');
        toggleRotationClass('icon-link-home', currentPath === '/');
    }

    // Blog link
    var blogLink = document.getElementById('blog-link');
    if (blogLink) {
        blogLink.classList.toggle('text-neutral-900', currentPath === '/blog');
        blogLink.classList.toggle('dark:!text-neutral-200', currentPath === '/blog');
        blogLink.classList.toggle('bg-neutral-200', currentPath === '/blog');
        blogLink.classList.toggle('dark:bg-neutral-800', currentPath === '/blog');
        blogLink.classList.toggle('lg:hover:gap-4', currentPath !== '/blog');
        blogLink.classList.toggle('hover:text-neutral-900', currentPath !== '/blog');
        blogLink.classList.toggle('hover:text-neutral-900', currentPath !== '/blog');
        toggleRotationClass('icon-link-blog', currentPath === '/blog');
    }

    // Project link
    var projectLink = document.getElementById('project-link');
    if (projectLink) {
        projectLink.classList.toggle('text-neutral-900', currentPath === '/project');
        projectLink.classList.toggle('dark:!text-neutral-200', currentPath === '/project');
        projectLink.classList.toggle('bg-neutral-200', currentPath === '/project');
        projectLink.classList.toggle('dark:bg-neutral-800', currentPath === '/project');
        projectLink.classList.toggle('lg:hover:gap-4', currentPath !== '/project');
        projectLink.classList.toggle('hover:text-neutral-900', currentPath !== '/project');
        projectLink.classList.toggle('hover:dark:text-neutral-300', currentPath !== '/project');
        toggleRotationClass('icon-link-project', currentPath === '/project');
    }

    // Learn link
    var learnLink = document.getElementById('learn-link');
    if (learnLink) {
        learnLink.classList.toggle('text-neutral-900', currentPath === '/learn');
        learnLink.classList.toggle('dark:!text-neutral-200', currentPath === '/learn');
        learnLink.classList.toggle('bg-neutral-200', currentPath === '/learn');
        learnLink.classList.toggle('dark:bg-neutral-800', currentPath === '/learn');
        learnLink.classList.toggle('lg:hover:gap-4', currentPath !== '/learn');
        learnLink.classList.toggle('hover:text-neutral-900', currentPath !== '/learn');
        learnLink.classList.toggle('hover:dark:text-neutral-300', currentPath !== '/learn');
        toggleRotationClass('icon-link-learn', currentPath === '/learn');
    }

    // About link
    var aboutLink = document.getElementById('about-link');
    if (aboutLink) {
        aboutLink.classList.toggle('text-neutral-900', currentPath === '/about');
        aboutLink.classList.toggle('dark:!text-neutral-200', currentPath === '/about');
        aboutLink.classList.toggle('bg-neutral-200', currentPath === '/about');
        aboutLink.classList.toggle('dark:bg-neutral-800', currentPath === '/about');
        aboutLink.classList.toggle('lg:hover:gap-4', currentPath !== '/about');
        aboutLink.classList.toggle('hover:text-neutral-900', currentPath !== '/about');
        aboutLink.classList.toggle('hover:dark:text-neutral-300', currentPath !== '/about');
        toggleRotationClass('icon-link-about', currentPath === '/about');
    }

    // Contact link
    var contactLink = document.getElementById('contact-link');
    if (contactLink) {
        contactLink.classList.toggle('text-neutral-900', currentPath === '/contact');
        contactLink.classList.toggle('dark:!text-neutral-200', currentPath === '/contact');
        contactLink.classList.toggle('bg-neutral-200', currentPath === '/contact');
        contactLink.classList.toggle('dark:bg-neutral-800', currentPath === '/contact');
        contactLink.classList.toggle('lg:hover:gap-4', currentPath !== '/contact');
        contactLink.classList.toggle('hover:text-neutral-900', currentPath !== '/contact');
        contactLink.classList.toggle('hover:dark:text-neutral-300', currentPath !== '/contact');
        toggleRotationClass('icon-link-contact', currentPath === '/contact');
    }

    // Dashboard link
    var dashboarLink = document.getElementById('dashboard-link');
    if (dashboarLink) {
        dashboarLink.classList.toggle('text-neutral-900', currentPath === '/dashboard');
        dashboarLink.classList.toggle('dark:!text-neutral-200', currentPath === '/dashboard');
        dashboarLink.classList.toggle('bg-neutral-200', currentPath === '/dashboard');
        dashboarLink.classList.toggle('dark:bg-neutral-800', currentPath === '/dashboard');
        dashboarLink.classList.toggle('lg:hover:gap-4', currentPath !== '/dashboard');
        dashboarLink.classList.toggle('hover:text-neutral-900', currentPath !== '/dashboard');
        dashboarLink.classList.toggle('hover:dark:text-neutral-300', currentPath !== '/dashboard');
        toggleRotationClass('icon-link-dashboard', currentPath === '/dashboard');
    }
});
