import React, { useState } from 'react';
import axios from 'axios';

function AuthForm() {
  const [isLogin, setIsLogin] = useState(true);
  const [formData, setFormData] = useState({ email: '', password: '', password_confirm: '' });
  const [message, setMessage] = useState('');

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const toggleForm = () => {
    setIsLogin(!isLogin);
    setFormData({ email: '', password: '', password_confirm: '' });
    setMessage('');
  };

  const handleSubmit = async e => {
    e.preventDefault();

    try {
      if (isLogin) {
        // login
        const response = await axios.post('http://127.0.0.1:8000/api/token/', {
          email: formData.email,
          password: formData.password,
        });
        const token = response.data.access;
        localStorage.setItem('token', token);
        setMessage('✅ Logged in successfully');
      } else {
        // register
        await axios.post('http://127.0.0.1:8000/accounts/api/V1/register/', {
          email: formData.email,
          password: formData.password,
          password_confirm: formData.password_confirm,
        });
        setMessage('✅ Check your email to verify your account.');
      }
    } catch (err) {
      setMessage('❌ ' + (err.response?.data?.detail || 'An error occurred.'));
    }
  };

  return (
    <div className="auth-form container mt-5">
      <h2>{isLogin ? 'Login' : 'Register'}</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          name="email"
          placeholder="Email"
          className="form-control mb-2"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          className="form-control mb-2"
          value={formData.password}
          onChange={handleChange}
          required
        />
        {!isLogin && (
          <input
            type="password"
            name="password_confirm"
            placeholder="Confirm Password"
            className="form-control mb-2"
            value={formData.password_confirm}
            onChange={handleChange}
            required
          />
        )}
        <button type="submit" className="btn btn-primary w-100">
          {isLogin ? 'Login' : 'Register'}
        </button>
      </form>
      <p className="mt-3 text-muted">{message}</p>
      <button className="btn btn-link" onClick={toggleForm}>
        {isLogin ? 'Need an account? Register' : 'Have an account? Login'}
      </button>
    </div>
  );
}

export default AuthForm;
