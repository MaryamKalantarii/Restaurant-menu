import React from 'react';
import CountUp from 'react-countup';
import { useTranslation } from 'react-i18next';

const stats = [
  { end: 232, label: 'clients' },   // تغییر نام‌ها به کلیدهای ترجمه
  { end: 521, label: 'projects' },
  { end: 1453, label: 'hoursOfSupport' },
  { end: 32, label: 'workers' },
];

function Stats() {
  const { t } = useTranslation(); // برای استفاده از ترجمه‌ها

  return (
    <section id="stats" className="stats section dark-background">
      <img src="/assets/img/stats-bg.jpg" alt="" data-aos="fade-in" />

      <div className="container position-relative" data-aos="fade-up" data-aos-delay="100">
        <div className="row gy-4">
          {stats.map((item, index) => (
            <div key={index} className="col-lg-3 col-md-6">
              <div className="stats-item text-center w-100 h-100">
                <span className="purecounter">
                  <CountUp end={item.end} duration={1.5} />
                </span>
                <p>{t(`stats.${item.label}`)}</p>  {/* استفاده از کلید ترجمه */}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Stats;
