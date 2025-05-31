import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay, Pagination } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/pagination';

function Events() {
  const slides = [
    {
      title: "Custom Parties",
      price: "$99",
      img: "/assets/img/events-1.jpg",
      description: "Quo corporis voluptas ea ad. Consectetur inventore sapiente ipsum voluptas eos omnis facere. Enim facilis veritatis id est rem repudiandae nulla expedita quas.",
    },
    {
      title: "Private Parties",
      price: "$289",
      img: "/assets/img/events-2.jpg",
      description: "In delectus sint qui et enim. Et ab repudiandae inventore quaerat doloribus...",
    },
    {
      title: "Birthday Parties",
      price: "$499",
      img: "/assets/img/events-3.jpg",
      description: "Laborum aperiam atque omnis minus omnis est qui assumenda quos...",
    },
    {
      title: "Wedding Parties",
      price: "$899",
      img: "/assets/img/events-4.jpg",
      description: "Esse quisquam ducimus officia ipsum ut quibusdam maxime. Non enim perspiciatis.",
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