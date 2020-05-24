(function() {
  const cookieRegex = /^ajTheme=(dark|light)$/;
  const themeRegex  = /^(dark|light)$/;
  const isDarkRegex = /dark/;

  const themeLinkTag = document.querySelector('link[rel="stylesheet"]');
  const themeButton  = document.querySelector('#theme-button');
  const logoImg      = document.querySelector('#header-logoImage');

  const isDark = (t) => isDarkRegex.test(t);

  const isValidTheme = (t) => themeRegex.test(t);

  const getOppositeTheme = (t) => isDark(t) ? 'light' : 'dark';

  const getCookieFromDocument = () => document.cookie.split('; ').find(c => cookieRegex.test(c));

  const getThemeFromCookie = (c) => c && c.split('=').pop();

  const setThemeCookie = (t) => document.cookie = `ajTheme=${t}`;

  const setThemeLinkTag = (t) => {
    hrefArr = themeLinkTag.href.split('/');

    if (hrefArr[hrefArr.length - 1] === `${t}.css`)
      return;

    hrefArr[hrefArr.length - 1] = `${t}.css`;
    themeLinkTag.href = hrefArr.join('/');
  }

  const setThemeLogo = (t) => {
    const logoSrcArr = logoImg.attributes.src.value.split('/');
    const currentSrc = logoSrcArr.pop();

    if (isDark(t)) {
      if (isDark(currentSrc)) return;
      logoSrcArr.push('logo-dark.png');
    } else {
      if (!isDark(currentSrc)) return;
      logoSrcArr.push('favicon.ico');
    }

    logoImg.attributes.src.value = logoSrcArr.join('/');
  }

  const setThemeButton = (t) => {
    themeButton.innerText = getOppositeTheme(t).toUpperCase();
    themeButton.attributes['data-theme'].value = t;
  }

  const setTheme = (t) => {
    if (!isValidTheme(t))
      return setTheme('light');

    setThemeCookie(t);
    setThemeLinkTag(t);
    setThemeLogo(t);
    setThemeButton(t);
  }

  const toggleTheme = (e) => {
    const currentTheme = e.target.attributes['data-theme'].value;
    e.target.blur();
    setTheme(getOppositeTheme(currentTheme));
  }

  let theme = null;
  const themeCookie = getCookieFromDocument();
  theme = themeCookie ? getThemeFromCookie(themeCookie) : 'light';
  theme && setTheme(theme);
  themeButton.addEventListener('click', toggleTheme);
})();
