import React from 'react';
import { useTranslation } from 'react-i18next';

function About() {
  const { t } = useTranslation();

  return (
    <section id="about" className="about section">
      <div className="container section-title" data-aos="fade-up">
        <h2>{t('about.title')}</h2>
        <p><span>{t('about.learnMore')}</span> <span className="description-title">{t('about.title')}</span></p>
      </div>

      <div className="container">
        <div className="row gy-4">
          <div className="col-lg-7" data-aos="fade-up" data-aos-delay="100">
            <img src="/assets/img/about.jpg" className="img-fluid mb-4" alt="about" />
            <div className="book-a-table">
              <h3>{t('bookTable')}</h3>
              <p>+1 5589 55488 55</p>
            </div>
          </div>

          <div className="col-lg-5" data-aos="fade-up" data-aos-delay="250">
            <div className="content ps-0 ps-lg-5">
              <p className="fst-italic">
                {t('about.paragraph1')}
              </p>
              <ul>
                <li><i className="bi bi-check-circle-fill"></i> {t('about.list1')}</li>
                <li><i className="bi bi-check-circle-fill"></i> {t('about.list2')}</li>
                <li><i className="bi bi-check-circle-fill"></i> {t('about.list3')}</li>
              </ul>
              <p>{t('about.paragraph2')}</p>

              <div className="position-relative mt-4">
                <img src="/assets/img/about-2.jpg" className="img-fluid" alt="about-2" />
                <a href="https://www.youtube.com/watch?v=Y7f98aduVJ8" className="glightbox pulsating-play-btn"></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default About;
