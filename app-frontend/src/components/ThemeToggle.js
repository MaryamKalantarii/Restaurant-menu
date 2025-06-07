import { useContext } from 'react';
import { ThemeContext } from '../context/ThemeContext';

const ThemeToggle = () => {
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <button 
      onClick={toggleTheme} 
      className={`theme-toggle-btn m-3 ${theme === 'dark' ? 'btn-dark' : 'btn-light'}`}
    >
      {theme === 'dark' ? '☀' : '🌙'}
    </button>
  );
};

export default ThemeToggle;
