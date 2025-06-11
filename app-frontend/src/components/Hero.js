import { useTranslation } from 'react-i18next';

function Hero() {
  const { t } = useTranslation();

  return (
    <section id="hero" className="hero section light-background">
      <div className="container">
        <div className="row gy-4 justify-content-center justify-content-lg-between">
          <div className="col-lg-5 order-2 order-lg-1 d-flex flex-column justify-content-center">
            <h1>{t('hero.title')}</h1>
            <p>{t('hero.subtitle')}</p>
            <div className="d-flex">
              <a href="#book-a-table" className="btn-get-started">{t('bookTable')}</a>
              <a href="https://www.youtube.com/watch?v=Y7f98aduVJ8" className="glightbox btn-watch-video d-flex align-items-center">
                <i className="bi bi-play-circle"></i><span>{t('hero.watchVideo')}</span>
              </a>
            </div>
          </div>
          <div className="col-lg-5 order-1 order-lg-2 hero-img">
            <img src="/assets/img/hero-img.png" className="img-fluid animated" alt="hero" />
          </div>
        </div>
      </div>
    </section>
  );
}

export default Hero;
