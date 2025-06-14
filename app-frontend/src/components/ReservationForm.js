import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useTranslation } from 'react-i18next';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function ReservationForm() {
  const { t } = useTranslation();
  const [formData, setFormData] = useState({
    name: '',
    date: '',
    time: '',
    people: '',
    message: '',
  });

  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(false);

  // گرفتن اطلاعات کاربر
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/dashboard/api/V1/profile_customer/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access')}`  // فرض بر اینه JWT استفاده می‌کنی
      }
    })
    .then(res => {
      if (!res.data.is_profile_complete) {
        toast.error('پروفایل شما کامل نیست. لطفاً شماره تلفن خود را وارد کنید.');
      }
      setUserData(res.data);
    })
    .catch(err => {
      toast.error('برای رزرو باید وارد شوید.');
    });
  }, []);

  const handleChange = (e) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!userData?.is_profile_complete) {
      return toast.error('لطفاً ابتدا پروفایل خود را کامل کنید.');
    }

    try {
      setLoading(true);

      await axios.post('/api/reservations/', {
        ...formData
      }, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`
        }
      });

      toast.success('رزرو با موفقیت انجام شد!');
      setFormData({ name: '', date: '', time: '', people: '', message: '' });

    } catch (err) {
      toast.error('خطا در ثبت رزرو. لطفاً دوباره تلاش کنید.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <section id="book-a-table" className="book-a-table section">
      <ToastContainer />
      <div className="container section-title" data-aos="fade-up">
        <h2>{t('reservation.title')}</h2>
        <p><span>{t('reservation.bookYour')}</span> <span className="description-title">{t('reservation.stayWithUs')}<br /></span></p>
      </div>

      <div className="container">
        <div className="row g-0" data-aos="fade-up" data-aos-delay="100">
          <div
            className="col-lg-4 reservation-img"
            style={{ backgroundImage: 'url(/assets/img/reservation.jpg)' }}
          ></div>

          <div
            className="col-lg-8 d-flex align-items-center reservation-form-bg"
            data-aos="fade-up"
            data-aos-delay="200"
          >
            <form className="php-email-form" onSubmit={handleSubmit}>
              <div className="row gy-4">
                <div className="col-lg-4 col-md-6">
                  <input
                    type="text"
                    name="name"
                    className="form-control"
                    value={formData.name}
                    onChange={handleChange}
                    placeholder={t('reservation.name')}
                    required
                  />
                </div>

                <div className="col-lg-4 col-md-6">
                  <input
                    type="email"
                    className="form-control"
                    value={userData?.email || ''}
                    placeholder={t('reservation.email')}
                    disabled
                  />
                </div>

                <div className="col-lg-4 col-md-6">
                  <input
                    type="text"
                    className="form-control"
                    value={userData?.phone || ''}
                    placeholder={t('reservation.phone')}
                    disabled
                  />
                </div>

                <div className="col-lg-4 col-md-6">
                  <input
                    type="date"
                    name="date"
                    className="form-control"
                    value={formData.date}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="col-lg-4 col-md-6">
                  <input
                    type="time"
                    name="time"
                    className="form-control"
                    value={formData.time}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="col-lg-4 col-md-6">
                  <input
                    type="number"
                    name="people"
                    className="form-control"
                    value={formData.people}
                    onChange={handleChange}
                    placeholder={t('reservation.people')}
                    required
                  />
                </div>
              </div>

              <div className="form-group mt-3">
                <textarea
                  name="message"
                  className="form-control"
                  rows="5"
                  value={formData.message}
                  onChange={handleChange}
                  placeholder={t('reservation.message')}
                ></textarea>
              </div>

              <div className="text-center mt-3">
                <button type="submit" disabled={loading}>
                  {loading ? t('reservation.loading') : t('reservation.button')}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  );
}

export default ReservationForm;
