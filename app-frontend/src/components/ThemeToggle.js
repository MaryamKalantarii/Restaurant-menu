import { useContext } from 'react';
import { ThemeContext } from '../context/ThemeContext';

const ThemeToggle = () => {
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
 <button 
  onClick={toggleTheme} 
  className={`theme-toggle-btn m-3 mt-1 ${theme === 'dark' ? 'btn-dark' : 'btn-light'}`}
>
  <span style={{ fontSize: '17px', color: theme === 'dark' ? 'white' : 'gray' }}>
    {theme === 'dark' ? 'DarkMode' : 'LightMode'}
  </span>
</button>

  );
};

export default ThemeToggle;
