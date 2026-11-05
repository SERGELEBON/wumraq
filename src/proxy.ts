import { NextResponse, type NextRequest } from "next/server";

// The static WUMRAQ site posts its forms to plain page URLs
// (action="/" or action="/20/contacts" ...), exactly like the original
// safenetsecuritygh.com CMS did. We intercept those POSTs and route them
// to the API routes that persist the data (SQLite via Prisma):
//   - modal "Request A Service"  -> /api/quote      (has "location" field)
//   - contacts "Send Us a Message" -> /api/contact  (has "subject_title" field)
//   - footer newsletter          -> /api/newsletter (only "email" field)
export async function proxy(req: NextRequest) {
  if (req.method !== "POST") return NextResponse.next();

  const ct = req.headers.get("content-type") ?? "";
  if (!ct.includes("multipart/form-data") && !ct.includes("application/x-www-form-urlencoded")) {
    return NextResponse.next();
  }

  let form: FormData;
  try {
    form = await req.formData();
  } catch {
    return NextResponse.next();
  }

  let target = "/api/newsletter";
  if (form.has("subject_title")) target = "/api/contact";
  else if (form.has("location")) target = "/api/quote";

  return NextResponse.rewrite(new URL(target, req.url));
}

export const config = {
  matcher: ["/", "/((?!_next|api|css|js|vendor|img|fonts|elements).*)"],
};
