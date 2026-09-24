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


// Carry only public campaign labels through same-site navigation; no persistent storage.
const campaignParams = new URLSearchParams(window.location.search);
document.querySelectorAll('a[href]').forEach(link => {
  const destination = new URL(link.getAttribute('href'), window.location.origin);
  if (destination.origin !== window.location.origin || destination.searchParams.get('journey') === 'private' || campaignParams.get('journey') === 'private') return;
  ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'].forEach(key => {
    const value = campaignParams.get(key);
    if (value && /^[a-zA-Z0-9_.-]{1,80}$/.test(value) && !destination.searchParams.has(key)) destination.searchParams.set(key, value);
  });
  link.href = destination.pathname + destination.search + destination.hash;
});
document.querySelectorAll('.footer-links').forEach(links => {
  if (!links.querySelector('a[href="/privacy.html"]')) {
    const link = document.createElement('a');
    link.href = '/privacy.html';
    link.textContent = 'Privacy';
    links.append(link);
  }
});
