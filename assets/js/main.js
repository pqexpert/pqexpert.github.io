// PQExpert.io — main.js

const toggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

if (toggle && navLinks) {
  toggle.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('open');
    toggle.setAttribute('aria-expanded', isOpen);
  });
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
}

const currentPath = window.location.pathname.replace('.html', '').replace(/\/$/, '') || '/';
document.querySelectorAll('.nav-links a').forEach(link => {
  const linkPath = new URL(link.href, window.location.origin).pathname.replace('.html', '').replace(/\/$/, '') || '/';
  if (linkPath === currentPath) link.classList.add('active');
});
