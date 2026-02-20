import React from "react";
import "./ContactPage.css";
import { FiPhone, FiMail, FiUser } from "react-icons/fi";
const ContactPage = () => {
  return (
    <div className="page-container">
      <h1 className="contact-title">Contact Us</h1>

      <div className="contact-layout">
        <div className="contact-info">
          <div className="my-info">
            <h2>Julian Oksimowicz</h2>
            <p>
              Phone:{" "}
              <a href="tel:+48796429229">+48 796 429 229</a>
            </p>
            <p>
              <a href="mailto:julowicz@gmail.com">
                julowicz@gmail.com
              </a>
            </p>

            <p className="contact-description">
           Contact Me
            </p>
          </div>
        </div>

        <div className="contact-form-card">
          <h2>Send a message</h2>

          <form className="contact-form">
            <div className="form-group">
              <label>Name</label>
              <input type="text" className="input" />
            </div>
           
            <div className="form-group">
              <label>Surname</label>
              <input type="text" className="input" />
            </div>

             <div className="form-group">
              <label>Phone Number</label>
              <input type="tel" className="input" />
            </div>

            <div className="form-group">
              <label>Email</label>
              <input type="email" className="input" />
            </div>

            <div className="form-group">
              <label>Message</label>
              <textarea rows="5" className="input" />
            </div>

            <button type="submit" className="btn-primary">
              Send Message
            </button>
          </form>
        </div>

      </div>

    </div>
  );
};

export default ContactPage;