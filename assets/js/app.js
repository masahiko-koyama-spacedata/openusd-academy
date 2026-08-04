(function () {
  const root = document.documentElement;
  let toggle = document.querySelector('[data-theme-toggle]');
  if (!toggle) {
    const header = document.querySelector('.site-header');
    if (!header) return;
    toggle = document.createElement('button');
    toggle.className = 'theme-toggle';
    toggle.type = 'button';
    toggle.dataset.themeToggle = '';
    toggle.innerHTML = '<span aria-hidden="true">◐</span><span class="theme-label">テーマ</span>';
    header.appendChild(toggle);
  }

  const storedTheme = localStorage.getItem('openusd-academy-theme');
  if (storedTheme === 'light' || storedTheme === 'dark') {
    root.dataset.theme = storedTheme;
  }

  function currentTheme() {
    if (root.dataset.theme) return root.dataset.theme;
    return 'light';
  }

  function updateButton() {
    const isDark = currentTheme() === 'dark';
    toggle.setAttribute('aria-pressed', String(isDark));
    toggle.setAttribute('aria-label', isDark ? 'ライトモードに切り替える' : 'ダークモードに切り替える');
  }

  toggle.addEventListener('click', function () {
    const nextTheme = currentTheme() === 'dark' ? 'light' : 'dark';
    root.dataset.theme = nextTheme;
    localStorage.setItem('openusd-academy-theme', nextTheme);
    updateButton();
  });

  updateButton();
}());
