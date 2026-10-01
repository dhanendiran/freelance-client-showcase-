// Theme Toggle (Dark Mode / Light Mode with LocalStorage persistence)
const themeToggle = document.getElementById('themeToggle');
const mobileThemeToggle = document.getElementById('mobileThemeToggle');

function applyTheme(isDark) {
  if (isDark) {
    document.documentElement.classList.add('dark');
    localStorage.setItem('theme', 'dark');
  } else {
    document.documentElement.classList.remove('dark');
    localStorage.setItem('theme', 'light');
  }
  if (window.lucide) {
    lucide.createIcons();
  }
}

// Initial theme check
const savedTheme = localStorage.getItem('theme');
const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
  applyTheme(true);
} else {
  applyTheme(false);
}

function toggleTheme() {
  const isDark = document.documentElement.classList.contains('dark');
  applyTheme(!isDark);
}

if (themeToggle) themeToggle.addEventListener('click', toggleTheme);
if (mobileThemeToggle) mobileThemeToggle.addEventListener('click', toggleTheme);

// Mobile Drawer Navigation
const menuBtn = document.getElementById('menuBtn');
const mobileMenu = document.getElementById('mobileMenu');
const mobileLinks = document.querySelectorAll('.mobile-nav-link');

if (menuBtn && mobileMenu) {
  menuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
  });

  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.add('hidden');
    });
  });
}

// Interactive Contact Form Handling
const contactForm = document.getElementById('contactForm');
const submitBtn = document.getElementById('submitBtn');
const btnText = document.getElementById('btnText');
const btnIcon = document.getElementById('btnIcon');
const formSuccessToast = document.getElementById('formSuccessToast');

if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Visual loading state
    btnText.textContent = 'Sending Message...';
    submitBtn.disabled = true;
    submitBtn.classList.add('opacity-75', 'cursor-not-allowed');

    // Simulate sending or trigger email endpoint
    setTimeout(() => {
      // Success feedback
      btnText.textContent = 'Message Sent!';
      submitBtn.classList.remove('opacity-75', 'cursor-not-allowed', 'bg-brand-600', 'hover:bg-brand-700');
      submitBtn.classList.add('bg-emerald-600', 'hover:bg-emerald-700');

      if (formSuccessToast) {
        formSuccessToast.classList.remove('hidden');
        formSuccessToast.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      contactForm.reset();

      // Reset button after 4 seconds
      setTimeout(() => {
        btnText.textContent = 'Send Inquiry Now';
        submitBtn.disabled = false;
        submitBtn.classList.remove('bg-emerald-600', 'hover:bg-emerald-700');
        submitBtn.classList.add('bg-brand-600', 'hover:bg-brand-700');
      }, 4000);
    }, 900);
  });
}
