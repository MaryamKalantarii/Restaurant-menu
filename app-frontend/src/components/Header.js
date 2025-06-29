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

        {/* دکمه رزرو و آیکن داشبورد در کنار هم */}
        <div className="d-flex align-items-center gap-3">
          <a className="btn-getstarted" href="#book-a-table">{t('bookTable')}</a>
        </div>
{localStorage.getItem('access') && (
  <Link to="/dashboard" title="dashboard" className="dashboard-icon">
    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" stroke="#6f4e37"
      strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24">
      <path d="M12 12c2.21 0 4-1.79 4-4S14.21 4 12 4 8 5.79 8 8s1.79 4 4 4Z" />
      <path d="M20 20c0-4-4-6-8-6s-8 2-8 6" />
    </svg>
  </Link>
)}



      </div>
    </header>
  );
}

export default Header;
