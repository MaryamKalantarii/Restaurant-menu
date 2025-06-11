import { useContext } from 'react';
import { ThemeContext } from '../context/ThemeContext';

const ThemeToggle = () => {
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <button 
      onClick={toggleTheme} 
      className={`theme-toggle-btn m-3 ${theme === 'dark' ? 'btn-dark' : 'btn-light'}`}
    >
      <span style={{ color: theme === 'dark' ? 'yellow' : 'gray' }}>
        {theme === 'dark' ? '🌕' : '🌙'}
      </span>
    </button>
  );
};

export default ThemeToggle;
