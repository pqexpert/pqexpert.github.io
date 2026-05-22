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
// Names rendered at runtime via JS only — never present as plain text in HTML.
// Prevents indexing by crawlers, aggregators, and scrapers.
document.querySelectorAll('.protected-identity').forEach(function(el) {
  try { el.textContent = atob(el.getAttribute('data-n')); }
  catch (e) { /* silently fail */ }
});

// --- Identity reveal toggle ---
(function() {
  const btn   = document.getElementById('identityReveal');
  const panel = document.getElementById('identityRevealPanel');
  if (!btn || !panel) return;

  btn.addEventListener('click', function() {
    const open = this.getAttribute('aria-expanded') === 'true';
    this.setAttribute('aria-expanded', String(!open));
    panel.hidden = open;
    this.classList.toggle('is-open', !open);
    const label = this.querySelector('.identity-reveal-label');
    if (label) label.textContent = open ? 'Legal identity' : 'Close';
  });
})();
