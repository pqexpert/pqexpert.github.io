// Fixed native form destinations; no API keys or form-submission proxy.
(() => {
  const journeys = {
  "professional": {
    "title": "Professional & firm",
    "description": "Cybersecurity, post-quantum readiness, research, briefings, partnerships, and company work.",
    "form": "z3HWJ4Zx58oSRGaBNGe8"
  },
  "hiring": {
    "title": "Hiring & career",
    "description": "A role, recruiting conversation, contract seat, or introduction to a team.",
    "form": "exWtcI61S1NFaCu7KBim"
  },
  "author": {
    "title": "Author & editorial",
    "description": "The Restoration Ledger, an article question or correction, interviews, speaking, and writing collaboration.",
    "form": "q0gHjc3JLvW5mWyDX84J"
  },
  "private": {
    "title": "Private contact",
    "description": "Ask Josh to contact you before sharing the matter. Contact details only; this is not a confidential reporting channel.",
    "form": "iRM4C5uP5szGGwqUDyva"
  }
};
  const params = new URLSearchParams(window.location.search);
  const selected = params.get('journey');
  if (!Object.prototype.hasOwnProperty.call(journeys, selected)) return;
  const journey = journeys[selected];
  const section = document.getElementById('inquiry');
  const formUrl = new URL('https://api.leadconnectorhq.com/widget/form/' + journey.form);
  // Never pass arbitrary query parameters or contact details to the provider.
  if (selected !== 'private') {
    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'].forEach(key => {
      const value = params.get(key);
      if (value && /^[a-zA-Z0-9_.-]{1,80}$/.test(value)) formUrl.searchParams.set(key, value);
    });
  }
  document.getElementById('inquiry-heading').textContent = journey.title;
  document.getElementById('inquiry-description').textContent = journey.description;
  const frame = document.createElement('iframe');
  frame.src = formUrl.href;
  frame.title = journey.title + ' form';
  frame.id = 'inline-' + journey.form;
  frame.setAttribute('data-layout', "{'id':'INLINE'}");
  frame.setAttribute('data-trigger-type', 'alwaysShow');
  frame.setAttribute('data-activation-type', 'alwaysActivated');
  frame.setAttribute('data-deactivation-type', 'neverDeactivate');
  frame.setAttribute('data-form-name', journey.title);
  frame.setAttribute('data-layout-iframe-id', frame.id);
  frame.setAttribute('data-form-id', journey.form);
  frame.setAttribute('data-cookie-consent', 'true');
  frame.setAttribute('data-cookie-consent-provider', 'auto');
  frame.referrerPolicy = 'no-referrer';
  document.getElementById('inquiry-embed').append(frame);
  document.getElementById('direct-form').href = formUrl.href;
  section.hidden = false;
  document.querySelector('[data-journey="' + selected + '"]').classList.add('journey-selected');
  // Keep the private route isolated from host-page tracking scripts.
  if (selected !== 'private') {
  const resizeScript = document.createElement('script');
  resizeScript.src = 'https://link.msgsndr.com/js/form_embed.js';
  resizeScript.async = true;
  document.body.append(resizeScript);
  }
  if (window.location.hash === '#inquiry') section.scrollIntoView();
})();
