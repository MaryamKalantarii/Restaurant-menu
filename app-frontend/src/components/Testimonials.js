import React from 'react';
import { useTranslation } from 'react-i18next';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay, Pagination } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/pagination';

const testimonials = [
  {
    nameKey: 'testimonial_1_name',
    titleKey: 'testimonial_1_title',
    textKey: 'testimonial_1_text',
    image: '/assets/img/testimonials/testimonials-1.jpg',
  },
  {
    nameKey: 'testimonial_2_name',
    titleKey: 'testimonial_2_title',
    textKey: 'testimonial_2_text',
    image: '/assets/img/testimonials/testimonials-2.jpg',
  },
  {
    nameKey: 'testimonial_3_name',
    titleKey: 'testimonial_3_title',
    textKey: 'testimonial_3_text',
    image: '/assets/img/testimonials/testimonials-3.jpg',
  },
  {
    nameKey: 'testimonial_4_name',
    titleKey: 'testimonial_4_title',
    textKey: 'testimonial_4_text',
    image: '/assets/img/testimonials/testimonials-4.jpg',
  },
];

function Testimonials() {
  const { t } = useTranslation();

  return (
    <section id="testimonials" className="testimonials section light-background">
      <div className="container section-title" data-aos="fade-up">
        <h2>{t('testimonials')}</h2>
        <p>
          {t('whatTheySay')} <span className="description-title">{t('sayingAboutUs')}</span>
        </p>
      </div>

      <div className="container" data-aos="fade-up" data-aos-delay="100">
        <Swiper
          modules={[Autoplay, Pagination]}
          autoplay={{ delay: 5000 }}
          pagination={{ clickable: true }}
          loop={true}
          speed={600}
          slidesPerView="auto"
        >
          {testimonials.map((item, index) => (
            <SwiperSlide key={index}>
              <div className="testimonial-item">
                <div className="row gy-4 justify-content-center">
                  <div className="col-lg-6">
                    <div className="testimonial-content">
                      <p>
                        <i className="bi bi-quote quote-icon-left"></i>
                        <span>{t(item.textKey)}</span>
                        <i className="bi bi-quote quote-icon-right"></i>
                      </p>
                      <h3>{t(item.nameKey)}</h3>
                      <h4>{t(item.titleKey)}</h4>
                      <div className="stars">
                        {[...Array(5)].map((_, i) => (
                          <i className="bi bi-star-fill" key={i}></i>
                        ))}
                      </div>
                    </div>
                  </div>
                  <div className="col-lg-2 text-center">
                    <img src={item.image} className="img-fluid testimonial-img" alt={t(item.nameKey)} />
                  </div>
                </div>
              </div>
            </SwiperSlide>
          ))}
        </Swiper>
        <div className="swiper-pagination"></div>
      </div>
    </section>
  );
}

export default Testimonials;
