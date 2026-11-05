import { NextResponse } from "next/server";
import { db } from "@/lib/db";

// Accepts both JSON (programmatic) and HTML form posts (footer newsletter).
// Form posts are redirected back to the site with ?subscribed=1.
export async function POST(req: Request) {
  try {
    const ct = req.headers.get("content-type") ?? "";
    let email = "";
    let isForm = false;

    if (ct.includes("multipart/form-data") || ct.includes("application/x-www-form-urlencoded")) {
      isForm = true;
      const form = await req.formData();
      email = String(form.get("email") ?? "");
    } else {
      const body = await req.json();
      email = String(body?.email ?? "");
    }

    if (!email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
      if (isForm) return NextResponse.redirect(new URL("/", req.url), 303);
      return NextResponse.json({ error: "Adresse email invalide." }, { status: 400 });
    }

    await db.newsletterSubscriber.upsert({
      where: { email: email.toLowerCase() },
      update: {},
      create: { email: email.toLowerCase() },
    });

    if (isForm) return NextResponse.redirect(new URL("/?subscribed=1", req.url), 303);
    return NextResponse.json({ ok: true });
  } catch {
    return NextResponse.json({ error: "Erreur lors de l'abonnement." }, { status: 500 });
  }
}
