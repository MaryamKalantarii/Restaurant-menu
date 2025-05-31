import React from 'react';
import CountUp from 'react-countup';

const stats = [
  { end: 232, label: 'Clients' },
  { end: 521, label: 'Projects' },
  { end: 1453, label: 'Hours Of Support' },
  { end: 32, label: 'Workers' },
];

function Stats() {
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
                <p>{item.label}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Stats;