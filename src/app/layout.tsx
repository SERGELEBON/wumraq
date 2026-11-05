import type { Metadata } from "next";
import { Poppins } from "next/font/google";
import "./globals.css";
import "boxicons/css/boxicons.min.css";

const poppins = Poppins({
  variable: "--font-poppins",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

export const metadata: Metadata = {
  title:
    "Wumraq Security Services Limited - Trusted Security Company in Ghana | 24HRS Guards, Guard Dog Services, Office, Home & Warehouse Security, Road and Building Engineering.",
  description:
    "WUMRAQ Security Services Limited - Licensed private security company in Accra, Ghana. 24hrs security guards, guard dog services, security for offices, homes and warehouses, plus road and building engineering works. Call 0246029009 / 0264019009.",
  keywords: [
    "wumraq",
    "security",
    "services",
    "security company ghana",
    "security services ghana",
    "security guards accra",
    "security company Accra",
    "24hrs security guard ghana",
    "guard dog services ghana",
    "security services to offices",
    "security services to homes",
    "security services to warehouse",
    "road and building engineering ghana",
    "Integrity",
    "Vigilance",
    "Reliability",
  ],
  authors: [{ name: "Wumraq Security Services Limited" }],
  robots: "index, follow",
  openGraph: {
    siteName: "Wumraq Security Services Limited",
    type: "website",
  },
  icons: {
    icon: "/img/favicon/favicon.png",
    apple: "/img/favicon/apple-touch-icon-144-precomposed.png",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="sn-site" suppressHydrationWarning>
      <body className={`${poppins.variable} antialiased`}>{children}</body>
    </html>
  );
}
