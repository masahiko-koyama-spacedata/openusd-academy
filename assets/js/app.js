(function () {
  const root = document.documentElement;
  const toggle = document.querySelector('[data-theme-toggle]');
  if (!toggle) return;

  const storedTheme = localStorage.getItem('openusd-academy-theme');
  if (storedTheme === 'light' || storedTheme === 'dark') {
    root.dataset.theme = storedTheme;
  }

  function currentTheme() {
    if (root.dataset.theme) return root.dataset.theme;
    return matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
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
