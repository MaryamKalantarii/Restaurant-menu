import React from "react";

function Chefs() {

  return (

    <section id="chefs" className="chefs section">


      <div className="container section-title" data-aos="fade-up">
        <h2>chefs</h2>
        <p><span>Our</span> <span className="description-title">Proffesional Chefs</span></p>
      </div>

      <div className="container">

        <div className="row gy-4">

          <div className="col-lg-4 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="100">
            <div className="team-member">
              <div className="member-img">
                <img src="assets/img/chefs/chefs-1.jpg" className="img-fluid" alt="" />
                <div className="social">
                  <a href=""><i className="bi bi-twitter-x"></i></a>
                  <a href=""><i className="bi bi-facebook"></i></a>
                  <a href=""><i className="bi bi-instagram"></i></a>
                  <a href=""><i className="bi bi-linkedin"></i></a>
                </div>
              </div>
              <div className="member-info">
                <h4>Walter White</h4>
                <span>Master Chef</span>
                <p>Velit aut quia fugit et et. Dolorum ea voluptate vel tempore tenetur ipsa quae aut. Ipsum exercitationem iure minima enim corporis et voluptate.</p>
              </div>
            </div>
          </div>

          <div className="col-lg-4 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="200">
            <div className="team-member">
              <div className="member-img">
                <img src="assets/img/chefs/chefs-2.jpg" className="img-fluid" alt="" />
                <div className="social">
                  <a href=""><i className="bi bi-twitter-x"></i></a>
                  <a href=""><i className="bi bi-facebook"></i></a>
                  <a href=""><i className="bi bi-instagram"></i></a>
                  <a href=""><i className="bi bi-linkedin"></i></a>
                </div>
              </div>
              <div className="member-info">
                <h4>Sarah Jhonson</h4>
                <span>Patissier</span>
                <p>Quo esse repellendus quia id. Est eum et accusantium pariatur fugit nihil minima suscipit corporis. Voluptate sed quas reiciendis animi neque sapiente.</p>
              </div>
            </div>
          </div>

          <div className="col-lg-4 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="300">
            <div className="team-member">
              <div className="member-img">
                <img src="assets/img/chefs/chefs-3.jpg" className="img-fluid" alt="" />
                <div className="social">
                  <a href=""><i className="bi bi-twitter-x"></i></a>
                  <a href=""><i className="bi bi-facebook"></i></a>
                  <a href=""><i className="bi bi-instagram"></i></a>
                  <a href=""><i className="bi bi-linkedin"></i></a>
                </div>
              </div>
              <div className="member-info">
                <h4>William Anderson</h4>
                <span>Cook</span>
                <p>Vero omnis enim consequatur. Voluptas consectetur unde qui molestiae deserunt. Voluptates enim aut architecto porro aspernatur molestiae modi.</p>
              </div>
            </div>
          </div>

        </div>

      </div>

    </section>




  );
}

export default Chefs;