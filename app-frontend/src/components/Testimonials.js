import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay, Pagination } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/pagination';

const testimonials = [
  {
    name: 'Saul Goodman',
    title: 'Ceo & Founder',
    text: 'Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus...',
    image: '/assets/img/testimonials/testimonials-1.jpg',
  },
  {
    name: 'Sara Wilsson',
    title: 'Designer',
    text: 'Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid...',
    image: '/assets/img/testimonials/testimonials-2.jpg',
  },
  {
    name: 'Jena Karlis',
    title: 'Store Owner',
    text: 'Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam...',
    image: '/assets/img/testimonials/testimonials-3.jpg',
  },
  {
    name: 'John Larson',
    title: 'Entrepreneur',
    text: 'Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat...',
    image: '/assets/img/testimonials/testimonials-4.jpg',
  },
];

function Testimonials() {
  return (
    <section id="testimonials" className="testimonials section light-background">
      <div className="container section-title" data-aos="fade-up">
        <h2>TESTIMONIALS</h2>
        <p>What Are They <span className="description-title">Saying About Us</span></p>
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
                        <span>{item.text}</span>
                        <i className="bi bi-quote quote-icon-right"></i>
                      </p>
                      <h3>{item.name}</h3>
                      <h4>{item.title}</h4>
                      <div className="stars">
                        {[...Array(5)].map((_, i) => (
                          <i className="bi bi-star-fill" key={i}></i>
                        ))}
                      </div>
                    </div>
                  </div>
                  <div className="col-lg-2 text-center">
                    <img src={item.image} className="img-fluid testimonial-img" alt={item.name} />
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