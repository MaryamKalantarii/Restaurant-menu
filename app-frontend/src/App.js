import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { ThemeProvider } from './context/ThemeContext';
import Header from './components/Header';
import Hero from './components/Hero';
import About from './components/About';
import WhyUs from './components/WhyUs';
import Stats from './components/Stats';
import Menu from './components/Menu';
import Testimonials from './components/Testimonials';
import Events from './components/Events';
import Chefs from './components/Chefs';
import ReservationForm from './components/ReservationForm';
import Gallery from './components/Gallery';
import Contact from './components/Contact';
import Footer from './components/Footer';
import AuthForm from './components/AuthForm';
import EmailVerified from './components/EmailVerified';
import './styles/styles.css';

function App() {
  const { t, i18n } = useTranslation();

  // تغییر زبان
  const changeLanguage = (lng) => {
    i18n.changeLanguage(lng);
  };

  // تغییر جهت صفحه بر اساس زبان
  useEffect(() => {
    if (i18n.language === 'fa') {
      document.documentElement.setAttribute('dir', 'rtl');
    } else {
      document.documentElement.setAttribute('dir', 'ltr');
    }
  }, [i18n.language]);

  return (
    <ThemeProvider>
      <Router>
        <Header />
        <Routes>
          <Route path="/" element={
            <>
              <Hero />
              <About />
              <WhyUs />
              <Stats />
              <Menu />
              <Testimonials />
              <Events />
              <Chefs />
              <ReservationForm />
              <Gallery />
              <Contact />
            </>
          } />
          <Route path="/login" element={<AuthForm />} />
          <Route path="/email-verified" element={<EmailVerified />} />
        </Routes>
        <Footer />
      </Router>
    </ThemeProvider>
  );
}

export default App;
