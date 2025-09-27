import { useSearchParams, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import '../styles/styles.css';


function EmailVerified() {
  const [params] = useSearchParams();
  const navigate = useNavigate();
  const status = params.get('status');
  const [count, setCount] = useState(5);

  useEffect(() => {
    const timer = setTimeout(() => setCount(prev => prev - 1), 1000);
    if (count === 0) navigate('/login');
    return () => clearTimeout(timer);
  }, [count, navigate]);

  const isSuccess = status === 'success';

  return (
    <div className="email-verified-wrapper">
      <div className="email-verified-box">
        <div className={`email-verified-icon ${isSuccess ? 'success' : 'error'}`}>
          {isSuccess ? '✅' : '❌'}
        </div>
        <h3 className="email-verified-title">
          {isSuccess ? 'ایمیل شما تأیید شد!' : 'توکن معتبر نیست یا منقضی شده است.'}
        </h3>
        <p className="email-verified-message">
          {isSuccess ? 'اکنون می‌توانید وارد شوید.' : 'لطفاً دوباره تلاش کنید.'}
        </p>
        <p className="email-verified-count">
          در حال انتقال به صفحه ورود... ({count})
        </p>
      </div>
    </div>
  );
}

export default EmailVerified;
