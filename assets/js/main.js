// PQExpert.io — main.js

// --- Mobile nav ---
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

// --- Active nav state ---
const currentPath = window.location.pathname.replace('.html', '').replace(/\/$/, '') || '/';
document.querySelectorAll('.nav-links a').forEach(link => {
  const linkPath = new URL(link.href, window.location.origin).pathname.replace('.html', '').replace(/\/$/, '') || '/';
  if (linkPath === currentPath) link.classList.add('active');
});

// --- Site-wide operating-principles route ---
// Every public page gets a durable path to the public operating charter without
// exposing private spiritual, health, identity, or other sensitive context.
document.querySelectorAll('.footer-links').forEach(footerLinks => {
  const hasPrinciples = Array.from(footerLinks.querySelectorAll('a')).some(link => {
    const path = new URL(link.href, window.location.origin).pathname;
    return path === '/principles.html' || path === '/principles';
  });
  if (!hasPrinciples) {
    const principlesLink = document.createElement('a');
    principlesLink.href = '/principles.html';
    principlesLink.textContent = 'Principles';
    footerLinks.prepend(principlesLink);
  }
});

