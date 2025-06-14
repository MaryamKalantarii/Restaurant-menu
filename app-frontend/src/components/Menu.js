import React, { useEffect, useState } from "react";
import axios from "axios";
import { useTranslation } from "react-i18next";

function Menu() {
  const { t } = useTranslation();
  const [menuItems, setMenuItems] = useState([]);
  const [activeCategory, setActiveCategory] = useState("starters");

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/menu/api/V1/menu-items/")
      .then((response) => {
        setMenuItems(response.data);
      })
      .catch((error) => {
        console.error("❌ خطا در دریافت منو:", error);
      });
  }, []);

  const groupedItems = menuItems.reduce((acc, item) => {
    item.category.forEach((cat) => {
      if (!acc[cat.slug]) acc[cat.slug] = [];
      acc[cat.slug].push(item);
    });
    return acc;
  }, {});

  const categories = Object.keys(groupedItems);

  return (
    <section id="menu" className="menu section">
      <div className="container section-title" data-aos="fade-up">
        <h2>{t("ourMenu")}</h2>
        <p>
          <span>{t("checkOur")}</span>{" "}
          <span className="description-title">{t("yummyMenu")}</span>
        </p>
      </div>

      <div className="container">
        <ul className="nav nav-tabs d-flex justify-content-center" data-aos="fade-up" data-aos-delay="100">
          {categories.map((slug) => (
            <li className="nav-item" key={slug}>
              <button
                className={`nav-link ${activeCategory === slug ? "active show" : ""}`}
                onClick={() => setActiveCategory(slug)}
              >
               <h4>{t(`categories.${slug}`)}</h4>

              </button>
            </li>
          ))}
        </ul>

        <div className="tab-content" data-aos="fade-up" data-aos-delay="200">
          <div className="tab-pane fade active show">
            <div className="tab-header text-center">
              <p>{t("menu")}</p>
             <h3>{t(`categories.${activeCategory}`)}</h3>

            </div>

            <div className="row gy-5">
              {groupedItems[activeCategory]?.map((item) => (
                <div className="col-lg-4 menu-item" key={item.id}>
                  <a href={item.image} className="glightbox">
                    <img src={item.image} className="menu-img img-fluid" alt={item.title} />
                  </a>
                  <h4>{item.title}</h4>
                  <p className="ingredients">{item.description}</p>
                  <p className="price">{item.get_price} {t("currency")}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Menu;
