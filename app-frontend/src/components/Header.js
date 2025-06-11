import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import ThemeToggle from './ThemeToggle';
import { useTranslation } from 'react-i18next';

function Header() {
  const { t, i18n } = useTranslation();
  const [activeLink, setActiveLink] = useState('#hero');
  const [langMenuOpen, setLangMenuOpen] = useState(false);

  const navLinks = [
    { href: '#hero', label: t('home') },
    { href: '#about', label: t('aboutYummy') },
    { href: '#menu', label: t('menuu') },
    { href: '#events', label: t('eveents') },
    { href: '#chefs', label: t('chefsTitle') },
    { href: '#gallery', label: t('gallerry') },
    { href: '#contact', label: t('contactt') },
  ];

  const changeLanguage = (lng) => {
    i18n.changeLanguage(lng);
    setLangMenuOpen(false);
  };

  return (
    <header id="header" className="header d-flex align-items-center sticky-top">
      <div className="container position-relative d-flex align-items-center justify-content-between">
        <a href="#hero" className="logo d-flex align-items-center me-auto me-xl-0">
          <h1 className="sitename">Yummy</h1><span>.</span>
        </a>

        <nav id="navmenu" className="navmenu">
          <ul>
            {navLinks.map((link) => (
              <li key={link.href}>
                <a
                  href={link.href}
                  className={activeLink === link.href ? 'active' : ''}
                  onClick={() => setActiveLink(link.href)}
                >
                  {link.label}
                </a>
              </li>
            ))}
            <li>
              <Link to="/login" className="nav-link">{t('login')}</Link>
            </li>
            <li>
              <ThemeToggle />
            </li>
            <li className="language-dropdown">
              <button onClick={() => setLangMenuOpen(!langMenuOpen)} className="lang-btn">
                🌐 {i18n.language.toUpperCase()}
              </button>
              {langMenuOpen && (
                <ul className="lang-menu">
                  <li onClick={() => changeLanguage('fa')}>🇮🇷 فارسی</li>
                  <li onClick={() => changeLanguage('en')}>🇺🇸 English</li>
                </ul>
              )}
            </li>
          </ul>
          <i className="mobile-nav-toggle d-xl-none bi bi-list"></i>
        </nav>

        <a className="btn-getstarted" href="#book-a-table">{t('bookTable')}</a>
      </div>
    </header>
  );
}

export default Header;
