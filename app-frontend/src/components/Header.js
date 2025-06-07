import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import ThemeToggle from './ThemeToggle';


function Header() {
  const [activeLink, setActiveLink] = useState('#hero');

  const navLinks = [
    { href: '#hero', label: 'Home' },
    { href: '#about', label: 'About' },
    { href: '#menu', label: 'Menu' },
    { href: '#events', label: 'Events' },
    { href: '#chefs', label: 'Chefs' },
    { href: '#gallery', label: 'Gallery' },
    { href: '#contact', label: 'Contact' },
  ];

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
              <Link to="/login" className="nav-link">Login</Link>
              
            </li>
            <li>
              <ThemeToggle />

            </li>
          </ul>
          <i className="mobile-nav-toggle d-xl-none bi bi-list"></i>
         
        </nav>

        <a className="btn-getstarted" href="#book-a-table">Book a Table</a>
      </div>
    </header>
  );
}

export default Header;
