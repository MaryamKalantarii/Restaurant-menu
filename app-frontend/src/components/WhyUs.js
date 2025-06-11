import React from 'react';
import { useTranslation } from 'react-i18next';

function WhyUs() {
  const { t } = useTranslation();

  return (
    <section id="why-us" className="why-us section light-background">
      <div className="container">
        <div className="row gy-4">
          <div className="col-lg-4" data-aos="fade-up" data-aos-delay="100">
            <div className="why-box">
              <h3>{t('whyUs.title')}</h3>
              <span className="why-us-description">{t('whyUs.description')}</span>
              <div className="text-center">
                <a href="#" className="more-btn">
                  <span>{t('whyUs.learnMore')}</span> <i className="bi bi-chevron-right"></i>
                </a>
              </div>
            </div>
          </div>

          <div className="col-lg-8 d-flex align-items-stretch">
            <div className="row gy-4" data-aos="fade-up" data-aos-delay="200">
              {t('whyUs.iconBoxes', { returnObjects: true }).map((box, index) => (
                <div className="col-xl-4" key={index} data-aos="fade-up" data-aos-delay={index * 100 + 300}>
                  <div className="icon-box d-flex flex-column justify-content-center align-items-center">
                    <i className={`bi bi-${index === 0 ? 'clipboard-data' : index === 1 ? 'gem' : 'inboxes'}`}></i>
                    <h4>{box.title}</h4>
                    <span className="icon-box-description">{box.description}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default WhyUs;
