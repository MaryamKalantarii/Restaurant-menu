import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { useTranslation } from 'react-i18next';

function Dashboard() {
  const navigate = useNavigate();
  const [reservations, setReservations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [userData, setUserData] = useState({});  // اطلاعات پروفایل
  const [reservationData, setReservationData] = useState({ name: '', email: '', phone_number: '' });
  const { t } = useTranslation();

  useEffect(() => {
    const token = localStorage.getItem('access');
    if (!token) {
      navigate('/login');
    } else {
      // گرفتن رزروهای کاربر
      axios
      
        .get('http://127.0.0.1:8000/reservations/api/V1/user-reservations/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((res) => {
          setReservations(res.data);
          setLoading(false);
        })
        .catch((err) => {
          console.error('Error fetching reservations:', err);
          setLoading(false);
        });

      // گرفتن اطلاعات پروفایل کاربر
      axios
        .get('http://127.0.0.1:8000/accounts/api/V1/profile/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((res) => {
          setUserData(res.data);
          // پر کردن فیلدهای فرم پروفایل با اطلاعات کاربر
          setReservationData({
            name: res.data.first_name || '',
            email: res.data.email || '',
            phone_number: res.data.phone_number || '',
          });
        })
        .catch((err) => {
          console.error('Error fetching user profile:', err);
        });
    }
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    navigate('/login');
  };

  const handleProfileUpdate = async (e) => {
    e.preventDefault();
    try {
      await axios.put(
        'http://127.0.0.1:8000/accounts/api/V1/profile/',
        userData,
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access')}`,
          },
        }
      );
      alert('پروفایل با موفقیت ذخیره شد.');
    } catch (error) {
      alert('خطا در ذخیره پروفایل.');
      console.error(error);
    }
  };

  const handleReservationChange = (e) => {
    setReservationData({
      ...reservationData,
      [e.target.name]: e.target.value,
    });
  };

  const handleReservationSubmit = (e) => {
  e.preventDefault();

  axios.post('http://127.0.0.1:8000/reservations/api/V1/', reservationData, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('access')}`,
    },
  })
  .then(response => {
    alert('رزرو با موفقیت ثبت شد');
    setReservationData({ name: '', email: '', phone_number: '' }); // پاک کردن فیلدهای فرم پس از ارسال
  })
  .catch(error => {
    console.error('خطا در ثبت رزرو:', error.response || error.message);
    if (error.response) {
      // نمایش پیام خطا
      const errorMessage = error.response.data.detail || error.response.statusText || 'خطای ناشناخته';
      alert(`خطا در ثبت رزرو: ${errorMessage}`);
    } else {
      alert('خطا در اتصال به سرور');
    }
  });
};


  return (
    <div className="container mt-5 mb-5">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="fw-bold" style={{ color: '#6f4e37' }}>{t('dashboard.welcome')}</h2>
        <button className="btn btn-outline-danger" onClick={handleLogout}>
          {t('dashboard.logout')}
        </button>
      </div>

     

      {/* نمایش رزروها */}
      {loading ? (
        <div className="text-center my-5">
          <div className="spinner-border text-brown" style={{ width: '4rem', height: '4rem', color: '#6f4e37' }} role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3 text-muted">{t('dashboard.loading')}</p>
        </div>
      ) : reservations.length > 0 ? (
        <div className="row">
          {reservations.map((reservation, index) => (
            <div className="col-md-6 col-lg-4 mb-4" key={reservation.id}>
              <div className="card p-4 shadow border-0" style={{
                background: 'linear-gradient(135deg, rgba(255, 0, 0, 0.62), rgb(66, 66, 66))',
                borderRadius: '20px',
                color: '#4e342e',
              }}>
                <div className="card-body">
                  <h5 className="card-title mb-3">{t('dashboard.reservation')} #{index + 1}</h5>
                  <p className="card-text">{t('dashboard.date')}: <strong>{reservation.date}</strong></p>
                  <p className="card-text">{t('dashboard.time')}: <strong>{reservation.time}</strong></p>
                  <p className="card-text">{t('dashboard.people')}: <strong>{reservation.people}</strong></p>
                  <hr />
                  <p className="card-text small text-muted">
                    {t('dashboard.createdAt')}: {new Date(reservation.created_date).toLocaleString('en-US')}
                  </p>
                  <p className="card-text small text-muted">{t('dashboard.email')}: {reservation.email}</p>
                  {reservation.phone && (
                    <p className="card-text small text-muted">{t('dashboard.phone')}: {reservation.phone}</p>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <p className="text-muted">{t('dashboard.noReservations')}</p>
      )}
    </div>
  );
}

export default Dashboard;
