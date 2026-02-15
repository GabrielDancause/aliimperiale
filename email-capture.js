(function () {
  'use strict';

  var APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzyxMBbzpTh4An8umtkgzIMZNYkLNADkYzh2_iDngYtHvp1vVXR5Tvkb_R_-QfvjRD1/exec';
  var STORAGE_PREFIX = 'email_capture_';

  if (document.body) { init(); }
  else { document.addEventListener('DOMContentLoaded', init); }

  function init() {
    var container = document.getElementById('email-capture-form');
    if (!container) return;

    var postSlug = container.getAttribute('data-post-slug') || '';
    var pdfUrl = container.getAttribute('data-pdf-url') || '';
    var pdfName = container.getAttribute('data-pdf-name') || 'Free Guide';

    // No PDF configured — don't render anything
    if (!pdfUrl) return;

    injectStyles();

    // Check if already subscribed for this post
    var saved;
    try { saved = localStorage.getItem(STORAGE_PREFIX + postSlug); } catch (e) {}

    if (saved) {
      renderAlreadySubscribed(container, pdfUrl, pdfName);
    } else {
      renderForm(container, postSlug, pdfUrl, pdfName);
    }
  }

  // ========================
  //  CSS Injection
  // ========================
  function injectStyles() {
    var css =
      '#email-capture-form .ec-card{' +
        'background:#fff;border-radius:18px;padding:32px 28px;' +
        'margin:36px 0 20px;text-align:center;' +
        'box-shadow:0 1px 4px rgba(46,62,36,.06);' +
        'border:1px solid rgba(46,62,36,.06);' +
      '}' +
      '#email-capture-form .ec-badge{' +
        'display:inline-block;font-size:.7rem;font-weight:600;' +
        'letter-spacing:.08em;text-transform:uppercase;' +
        'color:#AD9846;margin-bottom:8px;' +
      '}' +
      '#email-capture-form .ec-heading{' +
        "font-family:'The Bloomington',cursive;" +
        'font-size:2rem;font-weight:400;color:#2E3E24;' +
        'margin:0 0 10px;line-height:1.2;' +
      '}' +
      '#email-capture-form .ec-desc{' +
        'font-size:.88rem;color:#555549;line-height:1.7;' +
        'margin:0 0 22px;max-width:440px;margin-left:auto;margin-right:auto;' +
      '}' +
      '#email-capture-form .ec-form{' +
        'display:flex;justify-content:center;gap:10px;max-width:440px;margin:0 auto;' +
      '}' +
      '#email-capture-form .ec-input{' +
        'flex:1;padding:14px 18px;border:1px solid #C6C8BB;' +
        'border-radius:10px;font-family:inherit;font-size:.9rem;' +
        'background:#FAF8EB;color:#2E3E24;outline:none;' +
        'transition:border-color .15s ease,box-shadow .15s ease;' +
      '}' +
      '#email-capture-form .ec-input:focus{' +
        'border-color:#AD9846;box-shadow:0 0 0 3px rgba(173,152,70,.15);' +
      '}' +
      '#email-capture-form .ec-input.ec-error{' +
        'border-color:#9b3c3c;' +
      '}' +
      '#email-capture-form .ec-btn{' +
        'padding:14px 28px;background:#AD9846;color:#FAF8EB;' +
        'border:none;border-radius:10px;font-family:inherit;' +
        'font-size:.9rem;font-weight:600;cursor:pointer;white-space:nowrap;' +
        'transition:background .15s ease,transform .15s ease;' +
      '}' +
      '#email-capture-form .ec-btn:hover{background:#c4ad52;transform:translateY(-1px)}' +
      '#email-capture-form .ec-btn:disabled{opacity:.6;cursor:wait;transform:none}' +
      '#email-capture-form .ec-note{' +
        'font-size:.75rem;color:#8a8a7a;margin:14px 0 0;' +
      '}' +
      '#email-capture-form .ec-error-msg{' +
        'font-size:.82rem;color:#9b3c3c;margin:10px 0 0;' +
      '}' +
      '#email-capture-form .ec-success-icon{' +
        'font-size:2.5rem;margin-bottom:10px;' +
      '}' +
      '#email-capture-form .ec-download-btn{' +
        'display:inline-block;padding:14px 32px;background:#2E3E24;color:#FAF8EB;' +
        'text-decoration:none;border-radius:10px;font-weight:600;font-size:.9rem;' +
        'transition:background .15s ease,transform .15s ease;margin-top:18px;' +
      '}' +
      '#email-capture-form .ec-download-btn:hover{background:#3a5030;transform:translateY(-1px)}' +
      '@media(max-width:480px){' +
        '#email-capture-form .ec-card{padding:26px 20px}' +
        '#email-capture-form .ec-form{flex-direction:column}' +
        '#email-capture-form .ec-input{width:100%}' +
        '#email-capture-form .ec-btn{width:100%;min-height:44px}' +
      '}';

    var style = document.createElement('style');
    style.textContent = css;
    document.head.appendChild(style);
  }

  // ========================
  //  Render Form
  // ========================
  function renderForm(container, postSlug, pdfUrl, pdfName) {
    container.innerHTML =
      '<div class="ec-card">' +
        '<div class="ec-badge">Free Download</div>' +
        '<p class="ec-heading">' + pdfName + '</p>' +
        '<p class="ec-desc">Get our free guide delivered straight to your inbox. ' +
          'Practical insights you won\'t find in the video.</p>' +
        '<form class="ec-form" id="ec-form-inner">' +
          '<input class="ec-input" type="email" name="email" placeholder="Your email address" required autocomplete="email">' +
          '<button class="ec-btn" type="submit">Send Me the Guide</button>' +
        '</form>' +
        '<p class="ec-note">No spam, ever. Your email stays between us.</p>' +
      '</div>';

    var form = document.getElementById('ec-form-inner');
    form.addEventListener('submit', function (e) {
      handleSubmit(e, postSlug, pdfUrl, pdfName, container);
    });
  }

  // ========================
  //  Render Success
  // ========================
  function renderSuccess(container, pdfUrl, pdfName) {
    container.innerHTML =
      '<div class="ec-card">' +
        '<div class="ec-success-icon">\u2714\uFE0F</div>' +
        '<p class="ec-heading">You\'re In!</p>' +
        '<p class="ec-desc">Your guide is ready. Click below to download it now.</p>' +
        '<a class="ec-download-btn" href="' + pdfUrl + '" download>Download ' + pdfName + ' \u2192</a>' +
      '</div>';
  }

  // ========================
  //  Render Already Subscribed
  // ========================
  function renderAlreadySubscribed(container, pdfUrl, pdfName) {
    container.innerHTML =
      '<div class="ec-card">' +
        '<div class="ec-success-icon">\uD83D\uDC4B</div>' +
        '<p class="ec-heading">Welcome Back!</p>' +
        '<p class="ec-desc">You already grabbed this guide. Here it is again if you need it.</p>' +
        '<a class="ec-download-btn" href="' + pdfUrl + '" download>Download ' + pdfName + ' \u2192</a>' +
      '</div>';
  }

  // ========================
  //  Handle Submit
  // ========================
  function handleSubmit(e, postSlug, pdfUrl, pdfName, container) {
    e.preventDefault();

    var form = document.getElementById('ec-form-inner');
    var input = form.querySelector('.ec-input');
    var btn = form.querySelector('.ec-btn');
    var email = input.value.trim();

    // Clear previous errors
    var prevError = form.parentNode.querySelector('.ec-error-msg');
    if (prevError) prevError.remove();
    input.classList.remove('ec-error');

    // Validate
    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      input.classList.add('ec-error');
      showError(form.parentNode, 'Please enter a valid email address.');
      input.focus();
      return;
    }

    // Loading state
    btn.disabled = true;
    var originalText = btn.textContent;
    btn.textContent = 'Sending\u2026';

    // If Apps Script URL not configured, skip the POST and go straight to success
    if (APPS_SCRIPT_URL === 'PASTE_YOUR_APPS_SCRIPT_URL_HERE') {
      saveAndShowSuccess(postSlug, email, pdfUrl, pdfName, container);
      return;
    }

    var payload = JSON.stringify({
      email: email,
      post_slug: postSlug,
      source_url: window.location.href
    });

    // Use AbortController for timeout
    var controller;
    var timeoutId;
    if (typeof AbortController !== 'undefined') {
      controller = new AbortController();
      timeoutId = setTimeout(function () { controller.abort(); }, 15000);
    }

    var fetchOptions = {
      method: 'POST',
      redirect: 'follow',
      headers: { 'Content-Type': 'text/plain' },
      body: payload
    };
    if (controller) fetchOptions.signal = controller.signal;

    fetch(APPS_SCRIPT_URL, fetchOptions)
      .then(function (r) { return r.json(); })
      .then(function (data) {
        if (timeoutId) clearTimeout(timeoutId);
        if (data && data.success !== false) {
          saveAndShowSuccess(postSlug, email, pdfUrl, pdfName, container);
        } else {
          btn.disabled = false;
          btn.textContent = originalText;
          showError(form.parentNode, 'Something went wrong. Please try again.');
        }
      })
      .catch(function () {
        if (timeoutId) clearTimeout(timeoutId);
        // On network error or opaque response, still give the user the PDF
        // (better UX: don't punish the user for a backend hiccup)
        saveAndShowSuccess(postSlug, email, pdfUrl, pdfName, container);
      });
  }

  function saveAndShowSuccess(postSlug, email, pdfUrl, pdfName, container) {
    try { localStorage.setItem(STORAGE_PREFIX + postSlug, email); } catch (e) {}
    renderSuccess(container, pdfUrl, pdfName);
  }

  function showError(parent, message) {
    var p = document.createElement('p');
    p.className = 'ec-error-msg';
    p.textContent = message;
    parent.appendChild(p);
  }
})();
