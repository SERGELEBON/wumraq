import { NextResponse } from "next/server";
import { db } from "@/lib/db";

// Accepts both JSON (programmatic) and HTML form posts (static site forms).
// Form posts are redirected back to the site with ?sent=1.
export async function POST(req: Request) {
  try {
    const ct = req.headers.get("content-type") ?? "";
    let name = "", phone = "", email = "", subject_title = "", message = "";
    let isForm = false;

    if (ct.includes("multipart/form-data") || ct.includes("application/x-www-form-urlencoded")) {
      isForm = true;
      const form = await req.formData();
      name = String(form.get("name") ?? "");
      phone = String(form.get("phone") ?? "");
      email = String(form.get("email") ?? "");
      subject_title = String(form.get("subject_title") ?? "");
      message = String(form.get("message") ?? "");
    } else {
      const body = await req.json();
      name = String(body?.name ?? "");
      phone = String(body?.phone ?? "");
      email = String(body?.email ?? "");
      subject_title = String(body?.subject_title ?? "");
      message = String(body?.message ?? "");
    }

    if (!name || !phone || !email || !subject_title || !message) {
      if (isForm) return NextResponse.redirect(new URL("/20/contacts", req.url), 303);
      return NextResponse.json({ error: "Tous les champs sont requis." }, { status: 400 });
    }

    const saved = await db.contactMessage.create({
      data: {
        name,
        phone,
        email,
        subjectTitle: subject_title,
        message,
      },
    });

    if (isForm) return NextResponse.redirect(new URL("/20/contacts?sent=1", req.url), 303);
    return NextResponse.json({ ok: true, id: saved.id });
  } catch {
    return NextResponse.json({ error: "Erreur lors de l'enregistrement." }, { status: 500 });
  }
}
