import React from 'react';

function About() {
  return (
   
      <section id="about" className="about section">
        <div className="container section-title" data-aos="fade-up">
          <h2>About Us</h2>
          <p><span>Learn More</span> <span className="description-title">About Us</span></p>
        </div>

        <div className="container">
          <div className="row gy-4">
            <div className="col-lg-7" data-aos="fade-up" data-aos-delay="100">
              <img src="/assets/img/about.jpg" className="img-fluid mb-4" alt="about" />
              <div className="book-a-table">
                <h3>Book a Table</h3>
                <p>+1 5589 55488 55</p>
              </div>
            </div>

            <div className="col-lg-5" data-aos="fade-up" data-aos-delay="250">
              <div className="content ps-0 ps-lg-5">
                <p className="fst-italic">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                </p>
                <ul>
                  <li><i className="bi bi-check-circle-fill"></i> Ullamco laboris nisi ut aliquip ex ea commodo consequat.</li>
                  <li><i className="bi bi-check-circle-fill"></i> Duis aute irure dolor in reprehenderit in voluptate velit.</li>
                  <li><i className="bi bi-check-circle-fill"></i> Reprehenderit in voluptate trideta storacalaperda mastiro dolore.</li>
                </ul>
                <p>
                  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                </p>

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