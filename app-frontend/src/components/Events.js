import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay, Pagination } from 'swiper/modules';
import { useTranslation } from 'react-i18next';
import 'swiper/css';
import 'swiper/css/pagination';

function Events() {
  const { t } = useTranslation();

  const slides = [
    {
      title: t('events.customParties.title'),
      price: t('events.customParties.price'),
      img: '/assets/img/events-1.jpg',
      description: t('events.customParties.description'),
    },
    {
      title: t('events.privateParties.title'),
      price: t('events.privateParties.price'),
      img: '/assets/img/events-2.jpg',
      description: t('events.privateParties.description'),
    },
    {
      title: t('events.birthdayParties.title'),
      price: t('events.birthdayParties.price'),
      img: '/assets/img/events-3.jpg',
      description: t('events.birthdayParties.description'),
    },
    {
      title: t('events.weddingParties.title'),
      price: t('events.weddingParties.price'),
      img: '/assets/img/events-4.jpg',
      description: t('events.weddingParties.description'),
    },
  ];

  return (
    <section id="events" className="events section">
      <div className="container-fluid" data-aos="fade-up" data-aos-delay="100">
        <Swiper
          modules={[Autoplay, Pagination]}
          autoplay={{ delay: 5000 }}
          pagination={{ clickable: true }}
          loop={true}
          speed={600}
          breakpoints={{
            320: { slidesPerView: 1, spaceBetween: 40 },
            1200: { slidesPerView: 3, spaceBetween: 1 },
          }}
        >
          {slides.map((slide, index) => (
            <SwiperSlide key={index}>
              <div
                className="swiper-slide event-item d-flex flex-column justify-content-end"
                style={{ backgroundImage: `url(${slide.img})` }}
              >
                <h3>{slide.title}</h3>
                <div className="price align-self-start">{slide.price}</div>
                <p className="description">{slide.description}</p>
              </div>
            </SwiperSlide>
          ))}
        </Swiper>
      </div>
    </section>
  );
}

export default Events;
