import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
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
function App() {
  return (
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
      </Routes>
    <Footer />

    
    </Router>



  );
}

export default App;