import React from "react";
import { useTranslation } from "react-i18next";

function Contact() {
  const { t } = useTranslation();

  return (
    <section id="contact" className="contact section">
      <div className="container section-title" data-aos="fade-up">
        <h2>{t("contact.title")}</h2>
        <p>
          <span>{t("contact.needHelp")}</span>{" "}
          <span className="description-title">{t("contact.contactUs")}</span>
        </p>
      </div>

      <div className="container" data-aos="fade-up" data-aos-delay="100">
        <div className="mb-5">
          <iframe
            style={{ width: "100%", height: "400px" }}
            src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12097.433213460943!2d-74.0062269!3d40.7101282!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xb89d1fe6bc499443!2sDowntown+Conference+Center!5e0!3m2!1smk!2sbg!4v1539943755621"
            frameBorder="0"
            allowFullScreen
            title="Google Map"
          ></iframe>
        </div>

        <div className="row gy-4">
          <div className="col-md-6">
            <div className="info-item d-flex align-items-center" data-aos="fade-up" data-aos-delay="200">
              <i className="icon bi bi-geo-alt flex-shrink-0"></i>
              <div>
                <h3>{t("contact.addressTitle")}</h3>
                <p>{t("contact.address")}</p>
              </div>
            </div>
          </div>

          <div className="col-md-6">
            <div className="info-item d-flex align-items-center" data-aos="fade-up" data-aos-delay="300">
              <i className="icon bi bi-telephone flex-shrink-0"></i>
              <div>
                <h3>{t("contact.callUs")}</h3>
                <p>{t("contact.phone")}</p>
              </div>
            </div>
          </div>

          <div className="col-md-6">
            <div className="info-item d-flex align-items-center" data-aos="fade-up" data-aos-delay="400">
              <i className="icon bi bi-envelope flex-shrink-0"></i>
              <div>
                <h3>{t("contact.emailUs")}</h3>
                <p>{t("contact.email")}</p>
              </div>
            </div>
          </div>

          <div className="col-md-6">
            <div className="info-item d-flex align-items-center" data-aos="fade-up" data-aos-delay="500">
              <i className="icon bi bi-clock flex-shrink-0"></i>
              <div>
                <h3>{t("contact.openingHoursTitle")}</h3>
                <p>
                  <strong>{t("contact.openingDays")}:</strong> {t("contact.openingHours")};{" "}
                  <strong>{t("contact.closedDay")}:</strong> {t("contact.closedText")}
                </p>
              </div>
            </div>
          </div>
        </div>

        <form className="php-email-form" data-aos="fade-up" data-aos-delay="600" onSubmit={(e) => e.preventDefault()}>
          <div className="row gy-4">
            <div className="col-md-6">
              <input type="text" name="name" className="form-control" placeholder={t("contact.form.name")} required />
            </div>

            <div className="col-md-6">
              <input type="email" name="email" className="form-control" placeholder={t("contact.form.email")} required />
            </div>

            <div className="col-md-12">
              <input type="text" name="subject" className="form-control" placeholder={t("contact.form.subject")} required />
            </div>

            <div className="col-md-12">
              <textarea name="message" className="form-control" rows="6" placeholder={t("contact.form.message")} required></textarea>
            </div>

            <div className="col-md-12 text-center">
              <div className="loading">{t("contact.loading")}</div>
              <div className="error-message"></div>
              <div className="sent-message">{t("contact.sentMessage")}</div>

              <button type="submit">{t("contact.sendBtn")}</button>
            </div>
          </div>
        </form>
      </div>
    </section>
  );
}

export default Contact;
