import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { useTranslation } from 'react-i18next';

function Dashboard() {
  const navigate = useNavigate();
  const [reservations, setReservations] = useState([]);
  const [loading, setLoading] = useState(true);
  const { t } = useTranslation();

  useEffect(() => {
    const token = localStorage.getItem('access');
    if (!token) {
      navigate('/login');
    } else {
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
              <div
                className="card p-4 shadow border-0"
                style={{
                  background: 'linear-gradient(135deg, rgba(255, 0, 0, 0.62), rgb(66, 66, 66))',
                  borderRadius: '20px',
                  color: '#4e342e',
                }}
              >
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
