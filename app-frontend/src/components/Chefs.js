import React from "react";
import { useTranslation } from 'react-i18next';

function Chefs() {
  const { t } = useTranslation();

  return (
    <section id="chefs" className="chefs section">
      <div className="container section-title" data-aos="fade-up">
        <h2>{t('chefs.title')}</h2>
        <p>
          <span>{t('chefs.our')}</span>
          <span className="description-title">{t('chefs.professional')}</span>
        </p>
      </div>

      <div className="container">
        <div className="row gy-4">

          {/* Chef 1 */}
          <div className="col-lg-4 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="100">
            <div className="team-member">
              <div className="member-img">
                <img src="assets/img/chefs/chefs-1.jpg" className="img-fluid" alt="Chef Walter" />
                <div className="social">
                  <button type="button" aria-label="Twitter" className="icon-button">
                    <i className="bi bi-twitter-x"></i>
                  </button>
                  <button type="button" aria-label="Facebook" className="icon-button">
                    <i className="bi bi-facebook"></i>
                  </button>
                  <button type="button" aria-label="Instagram" className="icon-button">
                    <i className="bi bi-instagram"></i>
                  </button>
                  <button type="button" aria-label="LinkedIn" className="icon-button">
                    <i className="bi bi-linkedin"></i>
                  </button>
                </div>
              </div>
              <div className="member-info">
                <h4>{t('chefs.walter')}</h4>
                <span className="chef-role">{t('chefs.masterChef')}</span>
                <p>{t('chefs.walterDescription')}</p>
              </div>
            </div>
          </div>

          {/* Chef 2 */}
          <div className="col-lg-4 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="200">
            <div className="team-member">
              <div className="member-img">
                <img src="assets/img/chefs/chefs-2.jpg" className="img-fluid" alt="Chef Sarah" />
                <div className="social">
                  <button type="button" aria-label="Twitter" className="icon-button">
                    <i className="bi bi-twitter-x"></i>
                  </button>
                  <button type="button" aria-label="Facebook" className="icon-button">
                    <i className="bi bi-facebook"></i>
                  </button>
                  <button type="button" aria-label="Instagram" className="icon-button">
                    <i className="bi bi-instagram"></i>
                  </button>
                  <button type="button" aria-label="LinkedIn" className="icon-button">
                    <i className="bi bi-linkedin"></i>
                  </button>
                </div>
              </div>
              <div className="member-info">
                <h4>{t('chefs.sarah')}</h4>
                <span className="chef-role">{t('chefs.patissier')}</span>
                <p>{t('chefs.sarahDescription')}</p>
              </div>
            </div>
          </div>

          {/* Chef 3 */}
          <div className="col-lg-4 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="300">
            <div className="team-member">
              <div className="member-img">
                <img src="assets/img/chefs/chefs-3.jpg" className="img-fluid" alt="Chef William" />
                <div className="social">
                  <button type="button" aria-label="Twitter" className="icon-button">
                    <i className="bi bi-twitter-x"></i>
                  </button>
                  <button type="button" aria-label="Facebook" className="icon-button">
                    <i className="bi bi-facebook"></i>
                  </button>
                  <button type="button" aria-label="Instagram" className="icon-button">
                    <i className="bi bi-instagram"></i>
                  </button>
                  <button type="button" aria-label="LinkedIn" className="icon-button">
                    <i className="bi bi-linkedin"></i>
                  </button>
                </div>
              </div>
              <div className="member-info">
                <h4>{t('chefs.william')}</h4>
                <span className="chef-role">{t('chefs.cook')}</span>
                <p>{t('chefs.williamDescription')}</p>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
}

export default Chefs;
