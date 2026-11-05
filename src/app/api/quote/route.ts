import { NextResponse } from "next/server";
import { db } from "@/lib/db";

// Accepts both JSON (programmatic) and HTML form posts ("Request A Service" modal).
// Form posts are redirected back to the site with ?sent=1.
export async function POST(req: Request) {
  try {
    const ct = req.headers.get("content-type") ?? "";
    let name = "", phone = "", email = "", location = "", title = "", message = "";
    let isForm = false;

    if (ct.includes("multipart/form-data") || ct.includes("application/x-www-form-urlencoded")) {
      isForm = true;
      const form = await req.formData();
      name = String(form.get("name") ?? "");
      phone = String(form.get("phone") ?? "");
      email = String(form.get("email") ?? "");
      location = String(form.get("location") ?? "");
      title = String(form.get("title") ?? "");
      message = String(form.get("message") ?? "");
    } else {
      const body = await req.json();
      name = String(body?.name ?? "");
      phone = String(body?.phone ?? "");
      email = String(body?.email ?? "");
      location = String(body?.location ?? "");
      title = String(body?.title ?? "");
      message = String(body?.message ?? "");
    }

    if (!name || !phone || !email || !location || !title || !message) {
      if (isForm) return NextResponse.redirect(new URL("/", req.url), 303);
      return NextResponse.json({ error: "Tous les champs sont requis." }, { status: 400 });
    }

    const saved = await db.quoteRequest.create({
      data: { name, phone, email, location, service: title, message },
    });

    if (isForm) return NextResponse.redirect(new URL("/?sent=1", req.url), 303);
    return NextResponse.json({ ok: true, id: saved.id });
  } catch {
    return NextResponse.json({ error: "Erreur lors de l'enregistrement." }, { status: 500 });
  }
}
