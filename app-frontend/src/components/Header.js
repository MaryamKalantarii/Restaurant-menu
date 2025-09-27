import React, { useState } from 'react';
import { Link as RouterLink, useNavigate, useLocation } from 'react-router-dom';
import { scroller } from 'react-scroll';
import ThemeToggle from './ThemeToggle';
import { useTranslation } from 'react-i18next';
import '../styles/styles.css';
function Header() {
  const { t, i18n } = useTranslation();
  const [langMenuOpen, setLangMenuOpen] = useState(false);
  const [activeLink, setActiveLink] = useState('hero');
  const [menuOpen, setMenuOpen] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  const navLinks = [
    { id: 'hero', label: t('home') },
    { id: 'about', label: t('aboutYummy') },
    { id: 'menu', label: t('menuu') },
    { id: 'events', label: t('eveents') },
    { id: 'chefs', label: t('chefsTitle') },
    { id: 'gallery', label: t('gallerry') },
    { id: 'contact', label: t('contactt') },
  ];

  const scrollToSection = (id) => {
    if (location.pathname !== '/') {
      navigate('/', { replace: false });
      setTimeout(() => {
        scroller.scrollTo(id, { duration: 500, smooth: true, offset: -80 });
      }, 100);
    } else {
      scroller.scrollTo(id, { duration: 500, smooth: true, offset: -80 });
    }
    setActiveLink(id);
    setMenuOpen(false); // بستن منو پس از کلیک
  };

  const changeLanguage = (lng) => {
    i18n.changeLanguage(lng);
    setLangMenuOpen(false);
    setMenuOpen(false);
  };

  const handleLogout = () => {
    localStorage.removeItem('access');
    window.location.reload();
  };

  return (
    <header id="header" className="header d-flex align-items-center sticky-top">
      <div className="container position-relative d-flex align-items-center justify-content-between">
        <a href="#hero" className="logo d-flex align-items-center me-auto me-xl-0">
          <h1 className="sitename">Yummy</h1><span>.</span>
        </a>

        {/* همبرگر موبایل */}
        <button className="hamburger" onClick={() => setMenuOpen(!menuOpen)}>
          <span className={`bar ${menuOpen ? 'open' : ''}`}></span>
          <span className={`bar ${menuOpen ? 'open' : ''}`}></span>
          <span className={`bar ${menuOpen ? 'open' : ''}`}></span>
        </button>

        {/* منوی اصلی */}
        <nav id="navmenu" className={`navmenu ${menuOpen ? 'open' : ''}`}>
          <ul>
            {navLinks.map((link) => (
              <li key={link.id}>
                <button
                  className={`nav-link ${activeLink === link.id ? 'active' : ''}`}
                  onClick={() => scrollToSection(link.id)}
                >
                  {link.label}
                </button>
              </li>
            ))}

            {!localStorage.getItem('access') ? (
              <li>
                <RouterLink to="/login" className="nav-link">
                  {t('login')}
                </RouterLink>
              </li>
            ) : (
              <li>
                <button onClick={handleLogout} className="nav-link">
                  {t('logout')}
                </button>
              </li>
            )}

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
        </nav>

        {localStorage.getItem('access') && (
          <RouterLink to="/dashboard" title="dashboard" className="dashboard-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none" stroke="#6f4e37"
              strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24">
              <path d="M12 12c2.21 0 4-1.79 4-4S14.21 4 12 4 8 5.79 8 8s1.79 4 4 4Z" />
              <path d="M20 20c0-4-4-6-8-6s-8 2-8 6" />
            </svg>
          </RouterLink>
        )}
      </div>
    </header>
  );
}

export default Header;
