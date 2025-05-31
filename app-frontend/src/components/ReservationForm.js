import React from 'react';

function ReservationForm() {
  return (
    <section id="book-a-table" className="book-a-table section">
      <div className="container section-title" data-aos="fade-up">
        <h2>Book A Table</h2>
        <p><span>Book Your</span> <span className="description-title">Stay With Us<br /></span></p>
      </div>

      <div className="container">
        <div className="row g-0" data-aos="fade-up" data-aos-delay="100">
          <div
            className="col-lg-4 reservation-img"
            style={{ backgroundImage: 'url(/assets/img/reservation.jpg)' }}
          ></div>

          <div
            className="col-lg-8 d-flex align-items-center reservation-form-bg"
            data-aos="fade-up"
            data-aos-delay="200"
          >
            <form className="php-email-form" onSubmit={(e) => e.preventDefault()}>
              <div className="row gy-4">
                <div className="col-lg-4 col-md-6">
                  <input type="text" name="name" className="form-control" id="name" placeholder="Your Name" required />
                </div>
                <div className="col-lg-4 col-md-6">
                  <input type="email" name="email" className="form-control" id="email" placeholder="Your Email" required />
                </div>
                <div className="col-lg-4 col-md-6">
                  <input type="text" name="phone" className="form-control" id="phone" placeholder="Your Phone" required />
                </div>
                <div className="col-lg-4 col-md-6">
                  <input type="date" name="date" className="form-control" id="date" placeholder="Date" required />
                </div>
                <div className="col-lg-4 col-md-6">
                  <input type="time" name="time" className="form-control" id="time" placeholder="Time" required />
                </div>
                <div className="col-lg-4 col-md-6">
                  <input type="number" name="people" className="form-control" id="people" placeholder="# of people" required />
                </div>
              </div>

              <div className="form-group mt-3">
                <textarea name="message" className="form-control" rows="5" placeholder="Message"></textarea>
              </div>

              <div className="text-center mt-3">
                {/* پیام‌ها به صورت ظاهری فقط برای قالب هستند */}
                <div className="loading">Loading</div>
                <div className="error-message"></div>
                <div className="sent-message">
                  Your booking request was sent. We will call back or send an Email to confirm your reservation. Thank you!
                </div>
                <button type="submit">Book a Table</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  );
}

export default ReservationForm;