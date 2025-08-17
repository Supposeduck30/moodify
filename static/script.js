
(function applySavedTheme() {
  const saved = localStorage.getItem('moodify_theme') || 'default';
  setTheme(saved);
})();

const form = document.querySelector('.mood-form');
const moodInput = document.getElementById('m');
const emojiButtons = document.querySelectorAll('.emoji-btn');

emojiButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const mood = btn.getAttribute('data-mood') || btn.textContent.trim();
    const theme = btn.getAttribute('data-theme') || 'default';

    if (moodInput) moodInput.value = mood;

    setTheme(theme);

    emojiButtons.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');


    if (form) form.submit();
  });
});

function setTheme(themeName){
  document.body.classList.forEach(c => {
    if (c.startsWith('theme-')) document.body.classList.remove(c);
  });
  document.body.classList.add('theme-' + themeName);
  localStorage.setItem('moodify_theme', themeName);
}
