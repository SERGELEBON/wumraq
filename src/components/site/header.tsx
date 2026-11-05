"use client";

import React, { useEffect, useState } from "react";
import { useSite } from "./site-context";

const NAV = [
  { label: "Home", to: "/" },
  { label: "About Us", to: "/2/about-us" },
  { label: "Services", to: "/3/professional-security-services-in-ghana" },
  { label: "News", to: "/6/news" },
  { label: "Our Clients", to: "/7/our-clients" },
  { label: "Team", to: "/5/team" },
];

export default function Header() {
  const { route, navigate } = useSite();
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 60);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    document.body.style.overflow = menuOpen ? "hidden" : "";
    return () => {
      document.body.style.overflow = "";
    };
  }, [menuOpen]);

  const go = (to: string) => (e: React.MouseEvent) => {
    e.preventDefault();
    setMenuOpen(false);
    navigate(to);
  };

  const isActive = (to: string) =>
    to === "/" ? route === "/" : route.startsWith(to);

  return (
    <>
      <header className={`sn-header${scrolled ? " black" : ""}`}>
        <div className="container">
          <nav className="navbar navbar-dark">
            <a className="navbar-brand" href="#/" onClick={go("/")}>
              <img
                className="img-fluid"
                src="/img/images/logo.png"
                width={140}
                alt="Wumraq Security Services Limited logo"
              />
            </a>

            <button
              className="navbar-toggler mobile-toggler"
              type="button"
              onClick={() => setMenuOpen(true)}
              aria-controls="offcanvasNavbar"
              aria-label="Ouvrir le menu"
            >
              <span
                className="menu-label"
                style={{
                  fontSize: "1rem",
                  color: "#fff",
                  bottom: "0.8rem",
                  position: "relative",
                  textTransform: "uppercase",
                }}
              >
                Menu
              </span>
              <i className="bx bx-menu-alt-left" />
            </button>

            {/* Navigation desktop */}
            <div className="desktop-nav ms-auto">
              <ul
                className="navbar-nav"
                style={{ display: "flex", gap: 0, margin: 0, listStyle: "none" }}
              >
                {NAV.map((n) => (
                  <li
                    className="nav-item"
                    key={n.to}
                    style={{ position: "relative" }}
                  >
                    <a
                      className={`nav-link${isActive(n.to) ? " active" : ""}`}
                      href={`#${n.to}`}
                      onClick={go(n.to)}
                    >
                      {n.label}
                    </a>
                    {isActive(n.to) && (
                      <div className="triangle d-none d-sm-block" />
                    )}
                  </li>
                ))}
                <li className="navbar-item" style={{ display: "flex", alignItems: "center" }}>
                  <a
                    href="#/20/contacts"
                    onClick={go("/20/contacts")}
                    className="btn btn-primary border-0 text-uppercase mt-1 ms-3"
                  >
                    <i className="bx bx-customize" aria-hidden="true" /> Contact Us
                  </a>
                </li>
              </ul>
            </div>

            {/* Offcanvas mobile */}
            {menuOpen && (
              <>
                <div
                  className={`sn-offcanvas-backdrop${menuOpen ? " show" : ""}`}
                  onClick={() => setMenuOpen(false)}
                  aria-hidden="true"
                />
                <div
                  className={`sn-offcanvas${menuOpen ? " show" : ""}`}
                  role="dialog"
                  aria-modal="true"
                  aria-label="Menu de navigation"
                >
                  <div className="offcanvas-header">
                    <h5 className="offcanvas-title">
                      <img
                        src="/img/images/logo.png"
                        alt="Wumraq Security Services Limited logo"
                        style={{ height: 80 }}
                      />
                    </h5>
                    <button
                      type="button"
                      className="btn-close"
                      aria-label="Fermer"
                      onClick={() => setMenuOpen(false)}
                    />
                  </div>
                  <div className="offcanvas-body">
                    <ul className="navbar-nav" style={{ listStyle: "none" }}>
                      {NAV.map((n) => (
                        <li className="nav-item" key={n.to}>
                          <a
                            className={`nav-link${isActive(n.to) ? " active" : ""}`}
                            href={`#${n.to}`}
                            onClick={go(n.to)}
                          >
                            {n.label}
                          </a>
                        </li>
                      ))}
                      <li className="navbar-item">
                        <a
                          href="#/20/contacts"
                          onClick={go("/20/contacts")}
                          className="btn btn-primary border-0 text-uppercase mt-1 ms-3"
                        >
                          <i className="bx bx-customize" aria-hidden="true" /> Contact Us
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
              </>
            )}
          </nav>
        </div>
      </header>
    </>
  );
}
