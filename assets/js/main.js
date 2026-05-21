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

// --- Protected identity rendering ---
// Names rendered at runtime via JS — not present as plain text in HTML source.
// Prevents indexing/scraping of legal identity by crawlers and aggregators.
document.querySelectorAll('.protected-identity').forEach(function(el) {
  try {
    el.textContent = atob(el.getAttribute('data-n'));
  } catch (e) { /* silently fail — element stays empty */ }
});
