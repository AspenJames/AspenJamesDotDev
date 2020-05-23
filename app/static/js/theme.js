const themeRegex = /^(dark|light)$/;
const cookieRegex = /^ajTheme=(dark|light)$/;
const themeLinkTag = document.querySelector('link[rel="stylesheet"]');
const themeCheckbox = document.querySelector('#theme-checkbox');

const isValidTheme = (t) => themeRegex.test(t);

const getThemeCookieFromDocument = () => document.cookie.split('; ').find(c => cookieRegex.test(c));

const getThemeFromCookie = (c) => c && c.split('=').pop();

const setThemeCookie = (t) => document.cookie = `ajTheme=${t}`;

const setThemeLinkTag = (t) => {
  hrefArr = themeLinkTag.href.split('/');

  if (hrefArr[hrefArr.length - 1] === `${t}.css`)
    return;

  hrefArr[hrefArr.length - 1] = `${t}.css`;
  themeLinkTag.href = hrefArr.join('/');
}

const setThemeCheckbox = (t) => {
  shouldCheck = t === 'dark';
  themeCheckbox.checked = shouldCheck;
}

const setTheme = (t) => {
  if (!isValidTheme(t))
    return;
  setThemeCookie(t);
  setThemeLinkTag(t);
  setThemeCheckbox(t);
}

const toggleTheme = (e) => {
  if (e.target.checked) {
    return setTheme('dark');
  }
  return setTheme('light');
}


let theme = null;
const themeCookie = getThemeCookieFromDocument();


if (!themeCookie) {
  theme = 'light';
} else {
  theme = getThemeFromCookie(themeCookie);
}

theme && setTheme(theme);
themeCheckbox.addEventListener('change', toggleTheme)