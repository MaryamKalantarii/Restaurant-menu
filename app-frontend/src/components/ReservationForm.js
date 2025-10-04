// ReservationForm.jsx
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

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/accounts/api/V1/profile/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access')}`,
      },
    })
      .then(res => {
        setUserData(res.data);
        setFormData(prev => ({
          ...prev,
          name: res.data.first_name || '',
        }));
      })
      .catch(err => {
        console.log(err);
      });
  }, []);

  const handleChange = (e) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

const handleSubmit = async (e) => {
  e.preventDefault();

  try {
    setLoading(true);

    console.log('در حال ارسال فرم با داده‌ها:', formData); // لاگ برای بررسی داده‌های فرم

    const response = await axios.post(
      'http://127.0.0.1:8000/reservations/api/V1/reserve/',
      formData,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`,
          'Content-Type': 'application/json',
        },
      }
    );

    toast.success('رزرو با موفقیت انجام شد!');
    setFormData({ date: '', time: '', people: '', message: ''});

  } catch (err) {
    console.error('خطا در ارسال رزرو:', err);

    if (err.response) {
      console.error('پاسخ سرور:', err.response.data);
      toast.error(`خطا: ${JSON.stringify(err.response.data)}`);
    } else {
      toast.error('مشکلی در ارتباط با سرور پیش آمد.');
    }
  } finally {
    setLoading(false);
  }
};


  return (
    <>
      <ToastContainer position="bottom-right" autoClose={5000} hideProgressBar rtl theme="dark" style={{ zIndex: 9999 }} />
      <section id="book-a-table" className="book-a-table section">
        <div className="container section-title" data-aos="fade-up">
          <h2>{t('reservation.title')}</h2>
          <p>
            <span>{t('reservation.bookYour')}</span>{' '}
            <span className="description-title">{t('reservation.stayWithUs')}<br /></span>
          </p>
        </div>
        <div className="container">
          <div className="row g-0" data-aos="fade-up" data-aos-delay="100">
            <div className="col-lg-4 reservation-img" style={{ backgroundImage: 'url(/assets/img/reservation.jpg)' }}></div>
            <div className="col-lg-8 d-flex align-items-center reservation-form-bg" data-aos="fade-up" data-aos-delay="200">
              <form className="php-email-form" onSubmit={handleSubmit}>
                <div className="row gy-4">
                  
                   
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
    </>
  );
}

export default ReservationForm;
