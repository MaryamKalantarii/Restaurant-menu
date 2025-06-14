import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';

function AuthForm() {
  const { t } = useTranslation();
  const [isLogin, setIsLogin] = useState(true);
  const [formData, setFormData] = useState({ email: '', password: '', password_confirm: '' });
  const [message, setMessage] = useState('');
  const [messageType, setMessageType] = useState(''); // برای تعیین نوع پیام
  const navigate = useNavigate();

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
        // ✅ لاگین
        const response = await axios.post('http://127.0.0.1:8000/accounts/api/V1/token/login/', {
          email: formData.email,
          password: formData.password,
        });

        const { access, refresh } = response.data;
        console.log('Login Response:', response.data);
        localStorage.setItem('access', access);
        localStorage.setItem('refresh', refresh);
        console.log('Token saved in localStorage:', localStorage.getItem('access'));
        setMessage(t('auth.message.loginSuccess'));
        setMessageType('success'); // نوع پیام موفقیت

        navigate('/'); // ریدایرکت به داشبورد
      } else {
        // ✅ ثبت‌نام
        await axios.post('http://127.0.0.1:8000/accounts/api/V1/registration/', {
          email: formData.email,
          password: formData.password,
          password_confirm: formData.password_confirm,
        });
        setMessage(t('auth.message.registrationSuccess'));
        setMessageType('success'); // نوع پیام موفقیت
      }
    } catch (err) {
      setMessage(t('auth.message.error') + ' ' + (err.response?.data?.detail || 'خطا در عملیات.'));
      setMessageType('error'); // نوع پیام خطا
    }
  };

  return (
    <div className="auth-form container mt-5">
      <h2>{isLogin ? t('auth.login') : t('auth.register')}</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          name="email"
          placeholder={t('auth.email')}
          className="form-control mb-2"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder={t('auth.password')}
          className="form-control mb-2"
          value={formData.password}
          onChange={handleChange}
          required
        />
        {!isLogin && (
          <input
            type="password"
            name="password_confirm"
            placeholder={t('auth.confirmPassword')}
            className="form-control mb-2"
            value={formData.password_confirm}
            onChange={handleChange}
            required
          />
        )}
        <button type="submit" className="btn btn-primary w-100">
          {isLogin ? t('auth.login') : t('auth.register')}
        </button>
      </form>
      
     {message && (
  <div className={`message ${messageType}`}>
    {message}
  </div>
)}

      
      <button className="btn btn-link" onClick={toggleForm}>
        {isLogin ? t('auth.toggleForm.needAccount') : t('auth.toggleForm.haveAccount')}
      </button>
    </div>
  );
}

export default AuthForm;
