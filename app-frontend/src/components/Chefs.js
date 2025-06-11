import React from "react";
import { useTranslation } from 'react-i18next'; // ایمپورت useTranslation

function Chefs() {
  const { t } = useTranslation(); // استفاده از useTranslation

  return (
    <section id="chefs" className="chefs section">
      <div className="container section-title" data-aos="fade-up">
        <h2>{t('chefs.title')}</h2> {/* ترجمه عنوان Chefs */}
        <p><span>{t('chefs.our')}</span> <span className="description-title">{t('chefs.professional')}</span></p>
      </div>

      <div className="container">
        <div className="row gy-4">
          <div className="col-lg-4 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="100">
            <div className="team-member">
              <div className="member-img">
                <img src="assets/img/chefs/chefs-1.jpg" className="img-fluid" alt="" />
                <div className="social">
                  <a href=""><i className="bi bi-twitter-x"></i></a>
                  <a href=""><i className="bi bi-facebook"></i></a>
                  <a href=""><i className="bi bi-instagram"></i></a>
                  <a href=""><i className="bi bi-linkedin"></i></a>
                </div>
              </div>
              <div className="member-info">
                <h4>{t('chefs.walter')}</h4> {/* ترجمه نام Chef */}
                <span>{t('chefs.masterChef')}</span> {/* ترجمه سمت */}
                <p>{t('chefs.walterDescription')}</p> {/* ترجمه توضیحات */}
              </div>
            </div>
          </div>

          <div className="col-lg-4 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="200">
            <div className="team-member">
              <div className="member-img">
                <img src="assets/img/chefs/chefs-2.jpg" className="img-fluid" alt="" />
                <div className="social">
                  <a href=""><i className="bi bi-twitter-x"></i></a>
                  <a href=""><i className="bi bi-facebook"></i></a>
                  <a href=""><i className="bi bi-instagram"></i></a>
                  <a href=""><i className="bi bi-linkedin"></i></a>
                </div>
              </div>
              <div className="member-info">
                <h4>{t('chefs.sarah')}</h4> {/* ترجمه نام Chef */}
                <span>{t('chefs.patissier')}</span> {/* ترجمه سمت */}
                <p>{t('chefs.sarahDescription')}</p> {/* ترجمه توضیحات */}
              </div>
            </div>
          </div>

          <div className="col-lg-4 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="300">
            <div className="team-member">
              <div className="member-img">
                <img src="assets/img/chefs/chefs-3.jpg" className="img-fluid" alt="" />
                <div className="social">
                  <a href=""><i className="bi bi-twitter-x"></i></a>
                  <a href=""><i className="bi bi-facebook"></i></a>
                  <a href=""><i className="bi bi-instagram"></i></a>
                  <a href=""><i className="bi bi-linkedin"></i></a>
                </div>
              </div>
              <div className="member-info">
                <h4>{t('chefs.william')}</h4> {/* ترجمه نام Chef */}
                <span>{t('chefs.cook')}</span> {/* ترجمه سمت */}
                <p>{t('chefs.williamDescription')}</p> {/* ترجمه توضیحات */}
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
}

export default Chefs;
