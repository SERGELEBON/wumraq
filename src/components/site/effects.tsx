"use client";

import React, { useEffect, useRef, useState } from "react";
import { SITE } from "@/lib/site-data";

/** Bouton scroll-to-top (#button de l'original, avec la flèche SVG exacte) */
export function ScrollTopButton() {
  const [show, setShow] = useState(false);

  useEffect(() => {
    const onScroll = () => setShow(window.scrollY > 350);
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <a
      id="button"
      role="button"
      aria-label="Retour en haut"
      className={show ? "show" : ""}
      onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        x="0px"
        y="0px"
        viewBox="0 0 100 100"
        style={{ enableBackground: "new 0 0 100 100" }}
      >
        <g>
          <path d="M83.7,91.3c-19.7,0-36.3-19.2-38.5-38.3l26.9,13c0.4,0.1,0.7,0.2,1.1,0.2c0.9,0,1.6-0.4,2.2-1c0.9-0.9,1-2.2,0.5-3.3 L46.7,4c-0.5-1-1.5-1.6-2.6-1.6H44h-0.1c-1.1,0-2.1,0.6-2.6,1.6l-29,58c-0.5,1.1-0.4,2.5,0.5,3.3c0.6,0.6,1.4,1,2.2,1 c0.4,0,0.7-0.1,1.1-0.2l15.1-6c1.5-0.6,2.2-2.3,1.6-3.8s-2.3-1.4-3.8-0.8l-11.8,5.2L43.9,8.5l26.7,51.8L45.1,48.7 c-0.4-0.1-0.9-0.2-1.2-0.2h-0.1c-1.6,0-3,1.4-3,3c0,24.5,19.8,44.3,44.3,44.3c1.6,0,3-1.4,3-3C88,91.1,85.3,91.3,83.7,91.3z" />
          <path d="M53.2,89.9c-12.8-5.3-15.4-18-15.4-23.5c0-1.6,0.2-3.2-1.4-3.2l0,0c-1.6,0-3,1.4-3,3c0,4.8,2.5,10.1,5.2,14.8 c3.6,6,8,10.7,14.5,13.5c0.4,0.1,0.7,0.2,1.1,0.2c1.1,0,2.2-0.7,2.7-1.8C57.7,91.4,54.7,90.5,53.2,89.9z" />
        </g>
      </svg>
    </a>
  );
}

/** Curseur personnalisé rouge (mousecursor.js de l'original) */
export function CustomCursor() {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    if (window.matchMedia("(pointer: coarse)").matches) return; // pas sur mobile

    let raf = 0;
    let tx = -100, ty = -100, cx = -100, cy = -100;
    const onMove = (e: MouseEvent) => {
      tx = e.clientX;
      ty = e.clientY;
    };
    const loop = () => {
      cx += (tx - cx) * 0.35;
      cy += (ty - cy) * 0.35;
      el.style.transform = `translate(${cx}px, ${cy}px)`;
      raf = requestAnimationFrame(loop);
    };
    const onOver = (e: MouseEvent) => {
      const t = e.target as HTMLElement;
      el.classList.toggle(
        "hover",
        !!t.closest("a, button, input, textarea, select, .btn")
      );
    };
    window.addEventListener("mousemove", onMove);
    window.addEventListener("mouseover", onOver);
    raf = requestAnimationFrame(loop);
    return () => {
      window.removeEventListener("mousemove", onMove);
      window.removeEventListener("mouseover", onOver);
      cancelAnimationFrame(raf);
    };
  }, []);

  return <div ref={ref} className="sn-cursor" aria-hidden="true" />;
}

/**
 * Animation d'apparition façon WOW.js — applique la même classe
 * (slideInLeft, slideInRight, fadeInDown...) à l'entrée dans le viewport.
 */
export function Reveal({
  as: Tag = "div",
  anim,
  className = "",
  children,
  ...rest
}: {
  as?: keyof React.JSX.IntrinsicElements;
  anim: string;
  className?: string;
  children: React.ReactNode;
  [key: string]: unknown;
}) {
  const ref = useRef<HTMLElement | null>(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const obs = new IntersectionObserver(
      (entries) => {
        entries.forEach((en) => {
          if (en.isIntersecting) {
            setVisible(true);
            obs.disconnect();
          }
        });
      },
      { threshold: 0.12 }
    );
    obs.observe(el);
    return () => obs.disconnect();
  }, []);

  const Comp = Tag as React.ElementType;
  return (
    <Comp
      ref={ref}
      className={`sn-anim ${anim}${visible ? " animated" : ""} ${className}`}
      {...rest}
    >
      {children}
    </Comp>
  );
}

/** Widget WhatsApp flottant (équivalent du chat Elfsight de l'original) */
export function WhatsAppFloat() {
  const phone = SITE.phones[0].replace(/[^0-9]/g, "");
  return (
    <a
      className="sn-whatsapp"
      href={`https://wa.me/233${phone}`}
      target="_blank"
      rel="noreferrer"
      aria-label="Discuter sur WhatsApp"
      title="WhatsApp Chat"
    >
      <i className="bx bxl-whatsapp" aria-hidden="true" />
    </a>
  );
}

/** Bouton flottant qui ouvre le modal "Request A Service" (quoteModal) */
export function RequestServiceFloat() {
  return (
    <button
      type="button"
      className="sn-request-btn"
      onClick={() => window.dispatchEvent(new Event("open-quote-modal"))}
      aria-haspopup="dialog"
    >
      <i className="bx bx-customize" aria-hidden="true" />
      <span>Request A Service</span>
    </button>
  );
}
