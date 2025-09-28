import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { useTranslation } from 'react-i18next';

function Dashboard() {
  const navigate = useNavigate();
  const [reservations, setReservations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [userData, setUserData] = useState({});
  const { t } = useTranslation();

  useEffect(() => {
    const token = localStorage.getItem('access');
    if (!token) {
      navigate('/login');
    } else {
      // گرفتن رزروها
      axios.get('http://127.0.0.1:8000/reservations/api/V1/user-reservations/', {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((res) => {
        setReservations(res.data);
        setLoading(false);
      })
      .catch(() => setLoading(false));

      // گرفتن پروفایل
      axios.get('http://127.0.0.1:8000/accounts/api/V1/profile/', {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((res) => {
        setUserData(res.data);
      })
      .catch((err) => console.error(err));
    }
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    navigate('/login');
  };

  return (
    <div className="container mt-5 mb-5">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="fw-bold" style={{ color: '#6f4e37' }}>{t('dashboard.welcome')}</h2>
        <button className="btn btn-outline-danger" onClick={handleLogout}>
          {t('dashboard.logout')}
        </button>
      </div>

      <div className="d-flex">
        {/* 👇 کارت پروفایل سمت چپ ثابت */}
        <div className="me-4" style={{ minWidth: '300px', position: 'sticky', top: '80px', height: 'fit-content' }}>
          <div className="card shadow border-0 rounded-4"
               style={{
                 background: 'linear-gradient(145deg, #3d0000, #1a1a1a)',
                 color: '#ff4d4d',
                 padding: '1.5rem',
                 fontFamily: 'Arial, sans-serif',
                 border: '2px solid #ff4d4d',
                 transition: '0.3s'
               }}
               onMouseEnter={e => e.currentTarget.style.boxShadow = '0 0 20px #ff4d4d'}
               onMouseLeave={e => e.currentTarget.style.boxShadow = '0 0 10px #000'}
          >
            <div className="card-body d-flex flex-column align-items-center">
              <h5 className="fw-bold mb-4" style={{ textTransform: 'uppercase', fontSize: '1.4rem' }}>
                User Profile
              </h5>

              <div className="rounded-circle d-flex align-items-center justify-content-center mb-4"
                   style={{
                     width: '100px',
                     height: '100px',
                     background: '#1a1a1a',
                     border: '2px solid #ff4d4d'
                   }}>
                <i className="bi bi-person fs-1" style={{ color: '#ff4d4d' }}></i>
              </div>

              <div className="w-100">
                <div className="mb-3">
                  <label className="form-label" style={{ color: '#ff4d4d' }}>First Name</label>
                  <input type="text" className="form-control bg-dark text-white border-secondary" value={userData.first_name || ''} />
                </div>
                <div className="mb-3">
                  <label className="form-label" style={{ color: '#ff4d4d' }}>Last Name</label>
                  <input type="text" className="form-control bg-dark text-white border-secondary" value={userData.last_name || ''} />
                </div>
                <div className="mb-3">
                  <label className="form-label" style={{ color: '#ff4d4d' }}>Email</label>
                  <input type="email" className="form-control bg-dark text-white border-secondary" value={userData.email || ''} />
                </div>
                <div className="mb-3">
                  <label className="form-label" style={{ color: '#ff4d4d' }}>Phone</label>
                  <input type="tel" className="form-control bg-dark text-white border-secondary" value={userData.phone_number || ''} />
                </div>
              </div>

              <div className="d-flex justify-content-between w-100 mt-3">
                <button className="btn btn-outline-light w-45">Cancel</button>
                <button className="btn btn-danger w-45">Save Changes</button>
              </div>
            </div>
          </div>
        </div>

        {/* 👇 رزروها سمت راست */}
        <div className="flex-grow-1">
          {loading ? (
            <div className="text-center my-5">
              <div className="spinner-border text-brown" style={{ width: '4rem', height: '4rem', color: '#6f4e37' }} role="status">
                <span className="visually-hidden">Loading...</span>
              </div>
              <p className="mt-3 text-muted">{t('dashboard.loading')}</p>
            </div>
          ) : reservations.length > 0 ? (
            <div className="row g-4">
              {reservations.map((reservation, index) => (
                <div className="col-md-6 col-lg-6 mb-4" key={reservation.id}>
                  <div className="card p-4 shadow border-0" style={{
                    background: 'linear-gradient(135deg, rgba(255, 0, 0, 0.62), rgb(66, 66, 66))',
                    borderRadius: '20px',
                    color: '#fff',
                  }}>
                    <div className="card-body">
                      <h5 className="card-title mb-3">{t('dashboard.reservation')} #{index + 1}</h5>
                      <p className="card-text">{t('dashboard.date')}: <strong>{reservation.date}</strong></p>
                      <p className="card-text">{t('dashboard.time')}: <strong>{reservation.time}</strong></p>
                      <p className="card-text">{t('dashboard.people')}: <strong>{reservation.people}</strong></p>
                      <hr />
                      <p className="card-text small text-light">
                        {t('dashboard.createdAt')}: {new Date(reservation.created_date).toLocaleString('en-US')}
                      </p>
                      <p className="card-text small text-light">{t('dashboard.email')}: {reservation.email}</p>
                      {reservation.phone && (
                        <p className="card-text small text-light">{t('dashboard.phone')}: {reservation.phone}</p>
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
      </div>
    </div>
  );
}

export default Dashboard;
