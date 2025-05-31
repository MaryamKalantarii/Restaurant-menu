import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay, Pagination } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/pagination';

const galleryImages = [
    'gallery-1.jpg',
    'gallery-2.jpg',
    'gallery-3.jpg',
    'gallery-4.jpg',
    'gallery-5.jpg',
    'gallery-6.jpg',
    'gallery-7.jpg',
    'gallery-8.jpg',
];

function Gallery() {
    return (
        <section id="gallery" className="gallery section light-background">
            <div className="container section-title" data-aos="fade-up">
                <h2>Gallery</h2>
                <p>
                    <span>Check</span> <span className="description-title">Our Gallery</span>
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
                    centeredSlides={true}
                    breakpoints={{
                        320: { slidesPerView: 1, spaceBetween: 0 },
                        768: { slidesPerView: 3, spaceBetween: 20 },
                        1200: { slidesPerView: 5, spaceBetween: 20 },
                    }}
                >
                    {galleryImages.map((img, index) => (
                        <SwiperSlide key={index} className="align-items-center">
                            <a
                                className="glightbox"
                                data-gallery="images-gallery"
                                href={`/assets/img/gallery/${img}`}
                            >
                                <img
                                    src={`/assets/img/gallery/${img}`}
                                    className="img-fluid"
                                    alt={`Gallery ${index + 1}`}
                                />
                            </a>
                        </SwiperSlide>
                    ))}
                </Swiper>
                <div className="swiper-pagination"></div>
            </div>
        </section>
    );
}

export default Gallery;