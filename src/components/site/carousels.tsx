"use client";

import React, { useCallback, useEffect, useRef, useState } from "react";
import useEmblaCarousel from "embla-carousel-react";
import { SERVICES, HOME_SERVICES_ORDER, CLIENTS } from "@/lib/site-data";
import { useSite } from "./site-context";

const HERO_SLIDES = [
  "/img/sliders/wumraq-1.jpg",
  "/img/sliders/wumraq-2.jpg",
  "/img/sliders/wumraq-3.jpg",
];

/** Slider hero — reproduit le Revolution Slider (transition fade, 6s) */
export function HeroSlider() {
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const t = setInterval(
      () => setIndex((i) => (i + 1) % HERO_SLIDES.length),
      6000
    );
    return () => clearInterval(t);
  }, []);

  return (
    <div className="slider">
      <div className="fullwidthbanner-container">
        <div className="fullwidthbanner position-relative overflow-hidden">
          <ul style={{ margin: 0 }}>
            {HERO_SLIDES.map((src, i) => (
              <li
                key={src}
                className="hero-slide first-slide"
                style={{
                  opacity: i === index ? 1 : 0,
                  transition: "opacity 1.2s ease",
                }}
                aria-hidden={i !== index}
              >
                <img
                  src={src}
                  data-fullwidthcentering="on"
                  alt="WUMRAQ Security Services slide"
                />
                <div className="cover" />
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

type EmblaHook = ReturnType<typeof useEmblaCarousel>;

/** Carousel des services (accueil) — Owl Carousel 3/2/1 items + autoplay 5s */
export function ServicesCarousel() {
  const { navigate } = useSite();
  const [emblaRef, emblaApi] = (useEmblaCarousel({
    loop: true,
    align: "start",
    skipSnaps: false,
  }) as unknown) as EmblaHook;
  const [selected, setSelected] = useState(0);
  const [snaps, setSnaps] = useState<number[]>([]);

  useEffect(() => {
    if (!emblaApi) return;
    const onReInit = () => setSnaps(emblaApi.scrollSnapList());
    const onSelect = () => setSelected(emblaApi.selectedScrollSnap());
    emblaApi.on("reInit", onReInit);
    emblaApi.on("select", onSelect);
    // synchronisation initiale hors du corps synchrone de l'effet
    const t = setTimeout(() => {
      setSnaps(emblaApi.scrollSnapList());
      setSelected(emblaApi.selectedScrollSnap());
    }, 0);
    return () => {
      emblaApi.off("reInit", onReInit);
      emblaApi.off("select", onSelect);
      clearTimeout(t);
    };
  }, [emblaApi]);

  useEffect(() => {
    if (!emblaApi) return;
    const t = setInterval(() => emblaApi.scrollNext(), 5000);
    return () => clearInterval(t);
  }, [emblaApi]);

  const ordered = HOME_SERVICES_ORDER.map(
    (slug) => SERVICES.find((s) => s.slug === slug)!
  );

  return (
    <div>
      <div className="sn-embla" ref={emblaRef}>
        <div className="sn-embla__container">
          {ordered.map((s) => (
            <div className="sn-embla__slide" key={s.slug}>
              <div className="content-wrap">
                <a
                  href={`#/3/${s.id}/${s.slug}`}
                  onClick={(e) => {
                    e.preventDefault();
                    navigate(`/3/${s.id}/${s.slug}`);
                  }}
                >
                  <div className="img-wrapper">
                    <img
                      src={s.image}
                      className="img-fluid inner-img"
                      alt={` ${s.title}`}
                    />
                  </div>
                </a>
                <div className="item-wrapper p-4">
                  <a
                    href={`#/3/${s.id}/${s.slug}`}
                    onClick={(e) => {
                      e.preventDefault();
                      navigate(`/3/${s.id}/${s.slug}`);
                    }}
                  >
                    <h4 className="text-capitalize"> {s.title}</h4>
                  </a>
                  <div className="details mb-2">{s.short}</div>
                  <div className="d-flex justify-content-end">
                    <a
                      className="text-end"
                      href={`#/3/${s.id}/${s.slug}`}
                      onClick={(e) => {
                        e.preventDefault();
                        navigate(`/3/${s.id}/${s.slug}`);
                      }}
                      aria-label={`Voir ${s.title}`}
                    >
                      <i className="bx bx-arrow-back" aria-hidden="true" />
                    </a>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
      <div className="sn-owl-dots" role="tablist" aria-label="Navigation carousel">
        {snaps.map((_, i) => (
          <button
            key={i}
            className={i === selected ? "active" : ""}
            onClick={() => emblaApi?.scrollTo(i)}
            aria-label={`Aller au groupe ${i + 1}`}
          />
        ))}
      </div>
    </div>
  );
}

/** Carousel des clients — Owl 6/5/4/3/2 items + autoplay 4s */
export function ClientsCarousel() {
  const [emblaRef, emblaApi] = (useEmblaCarousel({
    loop: true,
    align: "start",
  }) as unknown) as EmblaHook;

  useEffect(() => {
    if (!emblaApi) return;
    const t = setInterval(() => emblaApi.scrollNext(), 4000);
    return () => clearInterval(t);
  }, [emblaApi]);

  return (
    <div className="sn-embla sn-embla--clients py-4" ref={emblaRef}>
      <div className="sn-embla__container">
        {CLIENTS.map((c) => (
          <div className="sn-embla__slide" key={c.name}>
            <div className="item-wrap text-center">
              <img
                src={c.image}
                className="img-fluid"
                alt="Client Logo"
                style={{ maxHeight: 120, margin: "0 auto" }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

/** Grille "Browse Other services" des pages détail (autres services, ordre original) */
export function BrowseOtherServices({ excludeSlug }: { excludeSlug: string }) {
  const { navigate } = useSite();
  const others = SERVICES.filter((s) => s.slug !== excludeSlug);

  return (
    <div className="category-menu">
      <h2 className="mb-2 text-uppercase">Browse Other services</h2>
      <div className="row">
        {others.map((s) => (
          <div className="col-sm-3 my-4" key={s.slug}>
            <div className="content-wrap">
              <a
                href={`#/3/${s.id}/${s.slug}`}
                onClick={(e) => {
                  e.preventDefault();
                  navigate(`/3/${s.id}/${s.slug}`);
                }}
              >
                <div className="img-item-wrap overflow-hidden">
                  <img src={s.image} className="img-fluid inner-img" alt={s.title} />
                </div>
              </a>
              <div className="item-wrapper p-4">
                <a
                  href={`#/3/${s.id}/${s.slug}`}
                  onClick={(e) => {
                    e.preventDefault();
                    navigate(`/3/${s.id}/${s.slug}`);
                  }}
                >
                  <h4 className="text-capitalize"> {s.title}</h4>
                </a>
                <div className="details mb-2">{s.short}</div>
                <div className="d-flex justify-content-end">
                  <a
                    className="text-end"
                    href={`#/3/${s.id}/${s.slug}`}
                    onClick={(e) => {
                      e.preventDefault();
                      navigate(`/3/${s.id}/${s.slug}`);
                    }}
                    aria-label={`Voir ${s.title}`}
                  >
                    <i className="bx bx-arrow-back" aria-hidden="true" />
                  </a>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
