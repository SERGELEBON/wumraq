"use client";

import React, { useState } from "react";
import { useSite } from "./site-context";
import { SITE } from "@/lib/site-data";
import { SERVICES, SERVICES_PAGE_ORDER } from "@/lib/site-data";

export default function Footer() {
  const { navigate } = useSite();
  const [email, setEmail] = useState("");
  const [subState, setSubState] = useState<"idle" | "sending" | "ok" | "err">(
    "idle"
  );

  const go = (to: string) => (e: React.MouseEvent) => {
    e.preventDefault();
    navigate(to);
  };

  const subscribe = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email.trim()) return;
    setSubState("sending");
    try {
      const res = await fetch("/api/newsletter", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });
      if (!res.ok) throw new Error("failed");
      setSubState("ok");
      setEmail("");
    } catch {
      setSubState("err");
    }
  };

  return (
    <footer className="sn-footer">
      <section className="top-footer" id="footer">
        <div className="container">
          <div className="row">
            <div className="footer-content col-sm-12">
              <div className="contact-banner d-flex align-items-center rounded-4 overflow-hidden mb-4">
                <div className="contact-logo px-4 py-3">
                  <img
                    src="/img/images/logo.png"
                    alt="Wumraq Security Services Limited"
                    style={{ height: 100 }}
                  />
                </div>
                <div className="d-flex flex-wrap justify-content-between align-items-center flex-grow-1 px-4 py-3 contact-details">
                  <div className="d-flex align-items-center me-4 mb-2">
                    <div className="icon-circle me-2">
                      <i className="bx bx-phone" aria-hidden="true" />
                    </div>
                    <div>
                      <small>phone number</small>
                      <h5>
                        {SITE.phones[0]}
                        <br /> {SITE.phones[1]}
                      </h5>
                    </div>
                  </div>
                  <div className="d-flex align-items-center me-4 mb-2">
                    <div className="icon-circle me-2">
                      <i className="bx bx-envelope" aria-hidden="true" />
                    </div>
                    <div>
                      <small>email address</small>
                      <h5>{SITE.email}</h5>
                    </div>
                  </div>
                  <div className="d-flex align-items-center mb-2">
                    <div className="icon-circle me-2">
                      <i className="bx bx-map" aria-hidden="true" />
                    </div>
                    <div>
                      <small>location</small>
                      <h5>
                        {SITE.locationLine1}
                        <br /> {SITE.locationLine2}
                        <br /> {SITE.locationLine3}
                      </h5>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="row footer">
            <div className="col-sm-12">
              <div className="item-wrap">
                <div className="row">
                  <div className="col-sm-4">
                    <h3 className="text-uppercase mb-4">About Us</h3>
                    <div className="details my-4">{SITE.aboutShort}</div>
                    <div className="mt-4 social-foot">
                      <a
                        href="https://www.linkedin.com/"
                        title="linkedin"
                        target="_blank"
                        rel="noreferrer"
                      >
                        <i className="bx bxl-linkedin icon" aria-hidden="true" />
                      </a>
                      <a
                        href="https://www.instagram.com/"
                        title="instagram"
                        target="_blank"
                        rel="noreferrer"
                      >
                        <i
                          className="bx bxl-instagram icon"
                          aria-hidden="true"
                        />
                      </a>
                      <div className="clear-fix" />
                    </div>
                  </div>

                  <div className="col-sm-2">
                    <div className="content-wrap pe-4">
                      <h3 className="text-uppercase mb-4">Quick Links</h3>
                      <a href="#/2/about-us" onClick={go("/2/about-us")}>
                        <h5 className="mb-4 text-capitalize"> About Us</h5>
                      </a>
                      <a href="#/5/team" onClick={go("/5/team")}>
                        <h5 className="mb-4 text-capitalize">Team</h5>
                      </a>
                      <a href="#/6/news" onClick={go("/6/news")}>
                        <h5 className="mb-4 text-capitalize">News</h5>
                      </a>
                      <a href="#/20/contacts" onClick={go("/20/contacts")}>
                        <h5 className="mb-4 text-capitalize">Contacts</h5>
                      </a>
                      <a href="#/7/our-clients" onClick={go("/7/our-clients")}>
                        <h5 className="mb-4 text-capitalize">Our Clients</h5>
                      </a>
                    </div>
                  </div>

                  <div className="col-sm-3">
                    <div className="content-wrap pe-4">
                      <h3 className="text-uppercase mb-4">
                        Professional Security Services in Ghana
                      </h3>
                      {SERVICES_PAGE_ORDER.map((slug) => {
                        const s = SERVICES.find((x) => x.slug === slug)!;
                        const to = `/3/${s.id}/${s.slug}`;
                        return (
                          <a href={`#${to}`} onClick={go(to)} key={slug}>
                            <h5 className="mb-4 text-capitalize">{s.title}</h5>
                          </a>
                        );
                      })}
                    </div>
                  </div>

                  <div className="col-sm-3">
                    <div className="content-wrap subscribe">
                      <h3 className="text-uppercase mb-4">Subscribe</h3>
                      <div className="details mb-4">
                        Stay updated with the latest security trends offers by
                        subscribing to our newsletter.
                      </div>
                      <form
                        className="newsletter-form mt-4"
                        onSubmit={subscribe}
                      >
                        {subState === "ok" && (
                          <div className="alert alert-success mb-2 w-100">
                            Thank you for subscribing!
                          </div>
                        )}
                        {subState === "err" && (
                          <div className="alert alert-danger mb-2 w-100">
                            Subscription failed. Please try again.
                          </div>
                        )}
                        <input
                          type="email"
                          className="form-control"
                          placeholder="Your email address"
                          value={email}
                          onChange={(e) => setEmail(e.target.value)}
                          required
                          aria-label="Email address"
                        />
                        <button
                          type="submit"
                          className="btn btn-primary border-0"
                          disabled={subState === "sending"}
                        >
                          {subState === "sending" ? "..." : "Subscribe"}
                        </button>
                      </form>
                    </div>
                  </div>
                </div>

                <div className="bot-menu">
                  <p className="dev mb-0 py-4">{SITE.copyright}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </footer>
  );
}
