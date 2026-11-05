"use client";

import React, {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useState,
} from "react";

/**
 * Routeur interne du clone — reproduit les URL de l'original :
 *   /  |  /2/about-us  |  /3/professional-security-services-in-ghana
 *   /3/{id}/{slug}  |  /5/team  |  /5/1/5/{slug}  |  /6/news
 *   /6/2/{slug}  |  /7/our-clients  |  /20/contacts
 * Navigation par hash pour rester sur la route unique "/" de l'aperçu.
 */
interface SiteCtx {
  route: string;
  navigate: (to: string) => void;
  quoteOpen: boolean;
  setQuoteOpen: (v: boolean) => void;
}

const Ctx = createContext<SiteCtx>({
  route: "/",
  navigate: () => {},
  quoteOpen: false,
  setQuoteOpen: () => {},
});

export const useSite = () => useContext(Ctx);

function currentHash(): string {
  if (typeof window === "undefined") return "/";
  const h = window.location.hash.replace(/^#/, "");
  return h === "" ? "/" : h;
}

export function SiteProvider({ children }: { children: React.ReactNode }) {
  const [route, setRoute] = useState("/");
  const [quoteOpen, setQuoteOpen] = useState(false);

  useEffect(() => {
    const onHash = () => setRoute(currentHash());
    onHash();
    window.addEventListener("hashchange", onHash);
    return () => window.removeEventListener("hashchange", onHash);
  }, []);

  const navigate = useCallback((to: string) => {
    const target = to.startsWith("/") ? to : `/${to}`;
    if (currentHash() === target) {
      window.scrollTo({ top: 0, behavior: "smooth" });
      return;
    }
    window.location.hash = target;
    window.scrollTo({ top: 0 });
  }, []);

  return (
    <Ctx.Provider value={{ route, navigate, quoteOpen, setQuoteOpen }}>
      {children}
    </Ctx.Provider>
  );
}
