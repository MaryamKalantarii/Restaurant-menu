import React, { useEffect, useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { useTranslation } from 'react-i18next';

function Dashboard() {
  const navigate = useNavigate();
  const [reservations, setReservations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [userData, setUserData] = useState({});
  const [profileImage, setProfileImage] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);
  const fileInputRef = useRef(null);
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
      axios.get('http://127.0.0.1:8000/dashboard/api/V1/my-profile/', {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((res) => {
        setUserData(res.data);
        if (res.data.image) {
          // اضافه کردن URL کامل برای نمایش عکس
          setProfileImage(res.data.image);
        }
      })
      .catch((err) => console.error(err));
    }
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    navigate('/login');
  };

  const handleChange = (e) => {
    setUserData({
      ...userData,
      [e.target.name]: e.target.value
    });
  };

  const handleCancel = () => {
    setUserData({
      first_name: "",
      last_name: "",
      phone_number: ""
    });
    setProfileImage(null);
    setSelectedFile(null);
  };

  const handleAvatarClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedFile(file);
      setProfileImage(URL.createObjectURL(file));
    }
  };

  const handleSave = () => {
    const token = localStorage.getItem('access');
    if (!token) return;

    const formData = new FormData();
    formData.append('first_name', userData.first_name || '');
    formData.append('last_name', userData.last_name || '');
    formData.append('phone_number', userData.phone_number || '');
    if (selectedFile) {
      formData.append('image', selectedFile);
    }

    axios
      .patch('http://127.0.0.1:8000/dashboard/api/V1/my-profile/', formData, {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'multipart/form-data',
        },
      })
      .then((res) => {
        setUserData(res.data);
        if (res.data.image) {
          setProfileImage(res.data.image);
        }
        alert('✅ پروفایل با موفقیت به‌روزرسانی شد!');
      })
      .catch((err) => {
        console.error(err);
        alert('❌ خطا در به‌روزرسانی پروفایل.');
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

      <div className="d-flex">
        {/* کارت پروفایل */}
        <div className="me-4" style={{ minWidth: '300px', position: 'sticky', top: '80px', height: 'fit-content' }}>
          <div
            className="card shadow border-0 rounded-4"
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

              {/* عکس پروفایل */}
              <div
                className="rounded-circle position-relative d-flex align-items-center justify-content-center mb-4"
                style={{
                  width: "120px",
                  height: "120px",
                  background: "#1a1a1a",
                  border: "2px solid #ff4d4d",
                  cursor: "pointer",
                  overflow: "hidden"
                }}
                onClick={handleAvatarClick}
              >
                {profileImage ? (
                  <img 
                    src={profileImage} 
                    alt="Profile" 
                    style={{ width: "100%", height: "100%", objectFit: "cover" }} 
                  />
                ) : (
                  <i className="bi bi-person fs-1" style={{ color: '#ff4d4d' }}></i>
                )}

                {/* آیکون دوربین */}
                <span
                  className="position-absolute bottom-0 end-0 bg-danger rounded-circle p-2 avatar-camera"
                  style={{ fontSize: '0.8rem', cursor: 'pointer' }}
                >
                  <i className="bi bi-camera text-white"></i>
                </span>

                {/* دکمه حذف عکس */}
                {profileImage && (
                  <span
                    className="position-absolute top-0 end-0 bg-dark rounded-circle p-1 avatar-delete"
                    style={{ cursor: "pointer", zIndex: 2 }}
                    onClick={(e) => {
                      e.stopPropagation();
                      setProfileImage(null);
                      setSelectedFile(null);
                    }}
                  >
                    <i className="bi bi-x text-white"></i>
                  </span>
                )}
              </div>

              <input
                type="file"
                accept="image/*"
                ref={fileInputRef}
                style={{ display: 'none' }}
                onChange={handleFileChange}
              />

              <div className="w-100">
                <div className="mb-3">
                  <label className="form-label" style={{ color: '#ff4d4d' }}>First Name</label>
                  <input 
                    type="text" 
                    name="first_name"
                    className="form-control bg-dark text-white border-secondary input-glow" 
                    value={userData.first_name || ''} 
                    onChange={handleChange}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label" style={{ color: '#ff4d4d' }}>Last Name</label>
                  <input 
                    type="text" 
                    name="last_name"
                    className="form-control bg-dark text-white border-secondary input-glow" 
                    value={userData.last_name || ''} 
                    onChange={handleChange}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label" style={{ color: '#ff4d4d' }}>Phone</label>
                  <input 
                    type="tel" 
                    name="phone_number"
                    className="form-control bg-dark text-white border-secondary input-glow" 
                    value={userData.phone_number || ''} 
                    onChange={handleChange}
                  />
                </div>
              </div>

              <div className="d-flex justify-content-between w-100 mt-3">
                <button className="btn btn-outline-light w-45 rounded-pill" onClick={handleCancel}>Cancel</button>
                <button 
                  className="btn w-45 rounded-pill" 
                  style={{
                    background: "linear-gradient(90deg, #ff4d4d, #ff8080)",
                    border: "none",
                    color: "#fff",
                    fontWeight: "bold"
                  }}
                  onClick={handleSave}
                >
                  Save Changes
                </button>
              </div>
            </div>
          </div>
        </div>
      

        {/* رزروها سمت راست */}
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

      {/* استایل glow و hover */}
      <style>{`
        .input-glow:focus {
          box-shadow: 0 0 8px #ff4d4d;
          border-color: #ff4d4d !important;
        }
        .avatar-camera:hover {
          transform: scale(1.2);
          transition: 0.2s;
        }
        .avatar-delete:hover {
          transform: scale(1.2);
          transition: 0.2s;
          background: #ff4d4d !important;
        }
      `}</style>
    </div>
  );
}

export default Dashboard;
