import React from 'react';
import { useTranslation } from 'react-i18next';

function ReservationForm() {
  const { t } = useTranslation();

  return (
    <section id="book-a-table" className="book-a-table section">
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
            <form className="php-email-form" onSubmit={(e) => e.preventDefault()}>
              <div className="row gy-4">
                <div className="col-lg-4 col-md-6">
                  <input type="text" name="name" className="form-control" id="name" placeholder={t('reservation.name')} required />
                </div>
                <div className="col-lg-4 col-md-6">
                  <input type="email" name="email" className="form-control" id="email" placeholder={t('reservation.email')} required />
                </div>
                <div className="col-lg-4 col-md-6">
                  <input type="text" name="phone" className="form-control" id="phone" placeholder={t('reservation.phone')} required />
                </div>
                <div className="col-lg-4 col-md-6">
                  <input type="date" name="date" className="form-control" id="date" placeholder={t('reservation.date')} required />
                </div>
                <div className="col-lg-4 col-md-6">
                  <input type="time" name="time" className="form-control" id="time" placeholder={t('reservation.time')} required />
                </div>
                <div className="col-lg-4 col-md-6">
                  <input type="number" name="people" className="form-control" id="people" placeholder={t('reservation.people')} required />
                </div>
              </div>

              <div className="form-group mt-3">
                <textarea name="message" className="form-control" rows="5" placeholder={t('reservation.message')}></textarea>
              </div>

              <div className="text-center mt-3">
                <div className="loading">{t('reservation.loading')}</div>
                <div className="error-message"></div>
                <div className="sent-message">
                  {t('reservation.sentMessage')}
                </div>
                <button type="submit">{t('reservation.button')}</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  );
}

export default ReservationForm;
