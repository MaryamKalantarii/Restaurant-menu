import { useSearchParams, useNavigate } from 'react-router-dom';
import { useEffect } from 'react';

function EmailVerified() {
  const [params] = useSearchParams();
  const navigate = useNavigate();
  const status = params.get('status');

  useEffect(() => {
    const timer = setTimeout(() => {
      navigate('/login');
    }, 3000);
    return () => clearTimeout(timer);
  }, [navigate]);

  return (
    <div className="container mt-5 text-center">
      {status === 'success' ? (
        <h3 className="text-success">✅ ایمیل شما تأیید شد. اکنون می‌توانید وارد شوید.</h3>
      ) : (
        <h3 className="text-danger">❌ توکن معتبر نیست یا منقضی شده است.</h3>
      )}
      <p>در حال انتقال به صفحه ورود...</p>
    </div>
  );
}

export default EmailVerified;
