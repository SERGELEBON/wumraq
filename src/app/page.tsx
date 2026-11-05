"use client";

import React, { useEffect } from "react";
import { SiteProvider, useSite } from "@/components/site/site-context";
import Header from "@/components/site/header";
import Footer from "@/components/site/footer";
import QuoteModal from "@/components/site/quote-modal";
import {
  ScrollTopButton,
  CustomCursor,
  WhatsAppFloat,
} from "@/components/site/effects";
import {
  HomePage,
  AboutPage,
  ServicesPage,
  ServiceDetailPage,
  TeamPage,
  TeamMemberPage,
  NewsPage,
  NewsArticlePage,
  ClientsPage,
  ContactsPage,
  NotFoundPage,
} from "@/components/site/pages";

function Router() {
  const { route } = useSite();

  useEffect(() => {
    window.scrollTo({ top: 0 });
  }, [route]);

  // /3/{id}/{slug} — pages détail services
  const serviceMatch = route.match(/^\/3\/(\d+)\/([a-z0-9-]+)$/);
  // /5/1/5/{slug} — fiche membre de l'équipe
  const memberMatch = route.match(/^\/5\/1\/5\/([a-z0-9-]+)$/);
  // /6/2/{slug} — article de news
  const articleMatch = route.match(/^\/6\/2\/([a-z0-9-]+)$/);

  let page: React.ReactNode;
  if (route === "/" || route === "") page = <HomePage />;
  else if (route === "/2/about-us") page = <AboutPage />;
  else if (route === "/3/professional-security-services-in-ghana")
    page = <ServicesPage />;
  else if (serviceMatch) page = <ServiceDetailPage slug={serviceMatch[2]} />;
  else if (route === "/5/team") page = <TeamPage />;
  else if (memberMatch) page = <TeamMemberPage slug={memberMatch[1]} />;
  else if (route === "/6/news") page = <NewsPage />;
  else if (articleMatch) page = <NewsArticlePage slug={articleMatch[1]} />;
  else if (route === "/7/our-clients") page = <ClientsPage />;
  else if (route === "/20/contacts") page = <ContactsPage />;
  else page = <NotFoundPage />;

  return (
    <>
      <Header />
      <main>{page}</main>
      <Footer />
      <QuoteModal />
      <ScrollTopButton />
      <WhatsAppFloat />
      <CustomCursor />
    </>
  );
}

export default function Page() {
  return (
    <SiteProvider>
      <Router />
    </SiteProvider>
  );
}
