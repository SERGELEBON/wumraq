"use client";

import React, { useEffect, useState } from "react";
import { SERVICE_OPTIONS } from "@/lib/site-data";

/** Modal "Request A Service" — formulaire identique à l'original (quoteModal) */
export default function QuoteModal() {
  const [open, setOpen] = useState(false);
  const [status, setStatus] = useState<"idle" | "sending" | "ok" | "err">(
    "idle"
  );
  const [form, setForm] = useState({
    name: "",
    phone: "",
    email: "",
    location: "",
    title: "",
    message: "",
  });

  // Ouverture via l'événement global (déclenché par les boutons "Request A Service")
  useEffect(() => {
    const handler = () => setOpen(true);
    window.addEventListener("open-quote-modal", handler);
    return () => window.removeEventListener("open-quote-modal", handler);
  }, []);

  // Fermeture par Échap
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") setOpen(false);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  const set = (k: keyof typeof form) => (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
  ) => setForm((f) => ({ ...f, [k]: e.target.value }));

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus("sending");
    try {
      const res = await fetch("/api/quote", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      if (!res.ok) throw new Error("failed");
      setStatus("ok");
      setForm({ name: "", phone: "", email: "", location: "", title: "", message: "" });
      setTimeout(() => {
        setOpen(false);
        setStatus("idle");
      }, 2500);
    } catch {
      setStatus("err");
    }
  };

  if (!open) return null;

  return (
    <div
      className="sn-modal-backdrop show"
      role="dialog"
      aria-modal="true"
      aria-labelledby="quoteModalLabel"
      onClick={(e) => {
        if (e.target === e.currentTarget) setOpen(false);
      }}
    >
      <div className="sn-modal show">
        <div className="modal-header">
          <h1 className="modal-title" id="quoteModalLabel">
            Request A Service
          </h1>
          <button
            type="button"
            className="btn-close"
            aria-label="Close"
            onClick={() => setOpen(false)}
          />
        </div>
        <div className="modal-body">
          {status === "ok" && (
            <div className="alert alert-success rounded-0 mb-0">
              Your request has been sent successfully. We will contact you
              shortly.
            </div>
          )}
          {status === "err" && (
            <div className="alert alert-danger rounded-0 mb-0">
              Sending failed. Please try again or call us directly.
            </div>
          )}
          <form action="/" method="POST" onSubmit={submit}>
            <div className="row">
              <div className="form-group col-sm-6 mb-2">
                <input
                  type="text"
                  className="form-control p-3"
                  name="name"
                  value={form.name}
                  onChange={set("name")}
                  placeholder="Full Name"
                  required
                />
              </div>
              <div className="form-group col-sm-6 mb-2">
                <input
                  type="tel"
                  className="form-control p-3"
                  name="phone"
                  value={form.phone}
                  onChange={set("phone")}
                  placeholder="Phone Number"
                  pattern="[0-9]{10}"
                  required
                />
              </div>
            </div>
            <div className="row">
              <div className="form-group col-sm-6 mb-2">
                <input
                  type="text"
                  className="form-control p-3"
                  name="email"
                  value={form.email}
                  onChange={set("email")}
                  placeholder="Email"
                  required
                />
              </div>
              <div className="form-group col-sm-6 mb-2">
                <input
                  type="text"
                  className="form-control p-3"
                  name="location"
                  value={form.location}
                  onChange={set("location")}
                  placeholder="Location"
                  required
                />
              </div>
            </div>
            <div className="form-group mb-2">
              <select
                name="title"
                required
                className="form-control p-3"
                value={form.title}
                onChange={set("title")}
              >
                <option value="">Select Product services</option>
                {SERVICE_OPTIONS.map((s) => (
                  <option key={s} value={s}>
                    {s}
                  </option>
                ))}
              </select>
            </div>
            <div className="form-group mb-2">
              <textarea
                className="form-control p-3"
                name="message"
                rows={5}
                required
                placeholder="Leave us a message..."
                value={form.message}
                onChange={set("message")}
              />
            </div>
            <div className="row text-center">
              <div className="form-group col-md-7 mt-2">
                {/* reCAPTCHA v2 — même clé de site que l'original */}
                <div
                  className="g-recaptcha"
                  data-sitekey="6LeBpIQrAAAAAIpK4xfgSSM6DqYQXS3PwcEoEUGD"
                />
              </div>
              <div className="form-group col-md-5 mt-2">
                <button
                  type="submit"
                  name="Feedback"
                  className="btn btn-danger p-4 border-0 rounded-0"
                  disabled={status === "sending"}
                >
                  SUBMIT MESSAGE
                </button>
              </div>
            </div>
          </form>
        </div>
        <div className="modal-footer">
          <button
            type="button"
            className="btn btn-secondary"
            onClick={() => setOpen(false)}
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}

/** Bouton utilitaire qui ouvre le modal (événement global) */
export function openQuoteModal() {
  window.dispatchEvent(new Event("open-quote-modal"));
}
