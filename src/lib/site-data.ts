// ============================================================
// WUMRAQ SECURITY SERVICES LIMITED — contenu intégral du site
// Établi d'après le fichier joint (panneaux WUMRAQ) :
//   • WUMRAQ SECURITY SERVICES LIMITED — 24HRS SECURITY GUARD,
//     GUARD DOG SERVICES, SECURITY SERVICES TO OFFICES / HOMES /
//     WAREHOUSE
//   • WUMRAQ LIMITED — ROAD AND BUILDING ENGINEERING
//     Call: 0246029009 / 0264019009
// Design / template : identique à safenetsecuritygh.com (inchangé)
// ============================================================

export const SITE = {
  name: "Wumraq Security Services Limited",
  phones: ["0246029009", "0264019009"],
  email: "info@wumraqsecurity.com",
  locationLine1: "Accra",
  locationLine2: "Greater Accra Region",
  locationLine3: "Ghana",
  aboutShort:
    "WUMRAQ Security Services Limited is a licensed and registered private security company based in Accra, Ghana. We provide dependable, professional and affordable security for individuals, homes, offices, businesses and warehouses — 24 hours a day, 7 days a...",
  copyright: "2026 © Wumraq Security Services Limited | All Rights Reserved",
};

export const HERO_ABOUT = {
  badge: "About Us",
  title: "WUMRAQ Security Services | Trusted Security & Protection in Ghana",
  details:
    "WUMRAQ Security Services Limited is a licensed and registered private security company based in Accra, Ghana. We provide dependable, professional and affordable protection for individuals, homes, offices, businesses and warehouses — day and night. At WUMRAQ, we believe security is more than presence — it is trust, vigilance and rapid response. That’s why every engagement...",
};

export const HOME_VALUES = [
  {
    title: "Our Vision",
    text: "To become Ghana’s most trusted and dependable security services provider, known for vigilance, integrity and round-the-clock...",
  },
  {
    title: "Our Mission",
    text: "To protect lives, property and assets through disciplined guards, trained guard dogs and rapid response — every hour of every...",
  },
  {
    title: "Core Values",
    text: "Integrity: We operate with honesty, transparency, and accountability. Trust is the cornerstone of our client...",
  },
];

export interface Service {
  id: number;
  slug: string;
  title: string;
  image: string;
  short: string;
  /** corps complet de la page détail : paragraphes (p) ou puces (li) */
  body: Array<{ type: "p" | "li"; text: string }>;
}

export const SERVICES: Service[] = [
  {
    id: 1,
    slug: "24hrs-security-guard",
    title: "24HRS Security Guard",
    image: "/img/services/24hrs_security_guard.jpg",
    short:
      "Our trained security guards keep your premises protected around the clock — day and night, every day of the...",
    body: [
      {
        type: "p",
        text: "WUMRAQ provides vigilant, uniformed security guards for 24-hour protection of your property, staff and visitors. Our guards work in structured day and night shifts so your site is never left unattended. Our 24hrs security guard services cover:",
      },
      { type: "li", text: "Gatehouse duties, access control and visitor management." },
      { type: "li", text: "Regular internal and perimeter patrols, day and night." },
      { type: "li", text: "Monitoring of alarms, CCTV and unusual activity." },
      { type: "li", text: "Incident reporting and rapid escalation to supervisors and police." },
      {
        type: "p",
        text: "Whether it is a private residence, a shop, an office, a yard or an event, our guards are trained to be alert, courteous and professional at every hour — giving you complete peace of mind.",
      },
    ],
  },
  {
    id: 2,
    slug: "guard-dog-services",
    title: "Guard Dog Services",
    image: "/img/services/guard_dog_services.jpg",
    short:
      "Highly trained guard dogs and licensed handlers provide a powerful visual and physical deterrent for your...",
    body: [
      {
        type: "p",
        text: "WUMRAQ deploys trained guard dogs with professional handlers to strengthen the protection of high-risk sites. A trained dog detects intruders long before a human can and provides a powerful visual deterrent. Our guard dog services include:",
      },
      { type: "li", text: "Perimeter and fence-line patrols with licensed dog handlers." },
      { type: "li", text: "Night protection for warehouses, yards, farms and construction sites." },
      { type: "li", text: "Detection of intruders in dark or large open areas." },
      { type: "li", text: "Controlled response on command — safe for staff, clients and visitors." },
      {
        type: "p",
        text: "All our dogs are trained, healthy and handled only by experienced, uniformed handlers, making this one of the most effective deterrents against burglary and vandalism.",
      },
    ],
  },
  {
    id: 3,
    slug: "security-services-to-offices",
    title: "Security Services to Offices",
    image: "/img/services/security_services_to_offices.jpg",
    short:
      "Professional guards for office premises — reception control, visitor management and protection of staff and...",
    body: [
      {
        type: "p",
        text: "WUMRAQ secures offices, corporate buildings, shops and business premises with smart, presentable and well-trained guards who protect your people, property and image. Our office security services cover:",
      },
      { type: "li", text: "Reception and front-desk security presence." },
      { type: "li", text: "Access control for staff, visitors and deliveries." },
      { type: "li", text: "Protection of equipment, documents and assets after hours." },
      { type: "li", text: "Weekend, holiday and after-hours cover on request." },
      {
        type: "p",
        text: "Our officers combine firmness with courtesy, ensuring your office remains a safe, welcoming and well-ordered environment for staff and clients alike.",
      },
    ],
  },
  {
    id: 4,
    slug: "security-services-to-homes",
    title: "Security Services to Homes",
    image: "/img/services/security_services_to_homes.jpg",
    short:
      "Dedicated guards for private residences and estates — protecting your family, home and property around the...",
    body: [
      {
        type: "p",
        text: "Your home is where your family should feel safest. WUMRAQ provides trusted, vetted guards for private residences, estates and gated communities across Accra and beyond. Our home security services include:",
      },
      { type: "li", text: "24-hour guarding at your gate and compound." },
      { type: "li", text: "Control of visitors, domestic deliveries and service providers." },
      { type: "li", text: "Night patrols of the compound and surrounding walls." },
      { type: "li", text: "Guard dog options for added protection of the property." },
      {
        type: "p",
        text: "Every residential guard is vetted, trained and supervised, so your family, home and possessions are in safe and reliable hands.",
      },
    ],
  },
  {
    id: 5,
    slug: "security-services-to-warehouse",
    title: "Security Services to Warehouse",
    image: "/img/services/security_services_to_warehouse.jpg",
    short:
      "Robust protection for warehouses, factories and storage yards — against theft, pilferage and unlawful...",
    body: [
      {
        type: "p",
        text: "Warehouses, factories and storage yards are prime targets for theft, pilferage and unlawful entry. WUMRAQ delivers robust industrial security to keep your goods and equipment safe. Our warehouse security services include:",
      },
      { type: "li", text: "Gate control of vehicles, cargo and documentation." },
      { type: "li", text: "Perimeter, yard and rack-area patrols — day and night." },
      { type: "li", text: "Loading and off-loading supervision to prevent losses." },
      { type: "li", text: "Guard dog teams for large yards and high-risk sites." },
      {
        type: "p",
        text: "Our supervisors carry out spot checks and detailed handover reports, so management always knows exactly what happened on site on every shift.",
      },
    ],
  },
  {
    id: 6,
    slug: "road-and-building-engineering",
    title: "Road And Building Engineering",
    image: "/img/services/road_and_building_engineering.jpg",
    short:
      "Through WUMRAQ Limited we also undertake road and building engineering works — executed with quality and...",
    body: [
      {
        type: "p",
        text: "Through our engineering arm, WUMRAQ Limited, we also undertake road and building engineering works for private and corporate clients. Our engineering services cover:",
      },
      { type: "li", text: "Road construction, reshaping and maintenance works." },
      { type: "li", text: "Building construction — residential, commercial and industrial." },
      { type: "li", text: "Compound walls, gates and security infrastructure." },
      { type: "li", text: "Renovation, civil works and site development." },
      {
        type: "p",
        text: "All works are executed by experienced engineers and skilled artisans, with proper supervision, quality materials and respect for agreed timelines. Call us for a site visit and quotation.",
      },
    ],
  },
];

/** Ordre du carousel de la page d'accueil (ordre du fichier joint) */
export const HOME_SERVICES_ORDER = [
  "24hrs-security-guard",
  "guard-dog-services",
  "security-services-to-offices",
  "security-services-to-homes",
  "security-services-to-warehouse",
  "road-and-building-engineering",
];

/** Ordre de la grille page Services (identique) */
export const SERVICES_PAGE_ORDER = HOME_SERVICES_ORDER;

export const PROJECTS_SECTION = {
  badge: "Our Clients",
  title: "Reliable protection for homes, offices and warehouses",
  details:
    "At our core, we are dedicated to delivering trusted security services that give peace of mind to homes, offices, warehouses and businesses alike. From 24-hour guards to trained guard dogs, our teams keep your property safe.\n\nWe know every site is different, which is why we offer tailored solutions designed to meet your specific needs. Our guards are vetted, trained and supervised to deliver reliable protection...",
  callLabel: "Call For Any Kind Of Services",
  image: "/img/contents/what-we-image.jpg",
};

export const CLIENTS = [
  { name: "Residential Estates", image: "/img/clients/residential-estates.png" },
  { name: "Logistics & Warehousing", image: "/img/clients/logistics-warehousing.png" },
  { name: "Corporate Offices", image: "/img/clients/corporate-offices.png" },
  { name: "Retail & Commerce", image: "/img/clients/retail-commerce.png" },
];

export const ABOUT = {
  title: "WUMRAQ Security Services | Trusted Security & Protection in Ghana",
  paragraphs: [
    "WUMRAQ Security Services Limited is a licensed and registered private security company based in Accra, Ghana. We provide dependable, professional and affordable security services to individuals, homes, offices, businesses and warehouses — day and night, 24 hours a day.",
    "At WUMRAQ, we believe security is more than presence — it is trust, vigilance and rapid response. That’s why every engagement begins with a proper assessment of your site, your risks and your specific needs, so we can deploy the right number of guards, dogs and supervision for your environment.",
    "From 24-hour security guards and trained guard dogs to dedicated protection for offices, homes and warehouses — and road and building engineering works through WUMRAQ Limited — we deliver peace of mind backed by integrity, discipline and client satisfaction.",
  ],
  image: "/img/contents/about-team.jpg",
};

export const VISION_MISSION = [
  {
    title: "Our Vision",
    text: "To become Ghana’s most trusted and dependable private security provider, known for vigilance, integrity, rapid response and exceptional client service.",
  },
  {
    title: "Our Mission",
    text: "To protect lives, property and assets through disciplined guards, trained guard dogs and responsive supervision — delivering high-quality security solutions every hour of every day.",
  },
];

export const ABOUT_VALUES = [
  {
    title: "Integrity",
    text: "We operate with honesty, transparency, and accountability. Trust is the cornerstone of our client relationships.",
  },
  {
    title: "Professionalism",
    text: "From appearance and conduct to reporting and response, we hold our guards and staff to the highest standards of discipline and efficiency.",
  },
  {
    title: "Vigilance",
    text: "Our guards stay alert at every hour of the day and night, watching for risks before they become problems.",
  },
  {
    title: "Reliability",
    text: "We show up on time, every time. Our clients depend on us for uninterrupted 24-hour protection, and we deliver it.",
  },
  {
    title: "Rapid Response",
    text: "When something goes wrong, our supervisors react fast — with clear escalation to management and the police where needed.",
  },
  {
    title: "Respect",
    text: "We treat every client, employee and community with dignity and fairness, regardless of status or background.",
  },
];

export const TEAM = {
  board: [
    {
      slug: "kwame-mensah",
      name: "Kwame Mensah",
      role: "Managing Director",
      image: "/img/staff/kwame_mensah.jpg",
      bio: [
        "Kwame Mensah is the Managing Director of WUMRAQ Security Services Limited. He leads the company’s operations, client relations and growth strategy, ensuring every client receives dependable protection at every hour of the day.",
        "Under his leadership, WUMRAQ has built a reputation for disciplined guards, well-trained dog teams and hands-on supervision across homes, offices and warehouses in Accra and beyond.",
        "He works closely with supervisors and clients to maintain the company’s standards of integrity, vigilance and rapid response on every site.",
      ],
    },
    {
      slug: "abena-owusu",
      name: "Abena Owusu",
      role: "Operations Manager",
      image: "/img/staff/abena_owusu.jpg",
      bio: [
        "Abena Owusu oversees the daily operations of WUMRAQ Security Services Limited — from guard deployment and shift planning to supervision and client support.",
        "She coordinates the rota of guards and dog handlers across all sites, making sure every post is covered 24 hours a day, 7 days a week.",
        "Her hands-on approach and quick response to incidents keep our clients’ properties protected and our standards consistently high.",
      ],
    },
    {
      slug: "yaw-boakye",
      name: "Yaw Boakye",
      role: "Chief Security Supervisor",
      image: "/img/staff/yaw_boakye.jpg",
      bio: [
        "Yaw Boakye is the Chief Security Supervisor of WUMRAQ Security Services Limited. He trains and disciplines our guards and dog handlers to deliver professional, alert and courteous service on every post.",
        "He carries out unannounced night spot checks across client sites, ensuring our 24-hour promise is kept in practice — not just on paper.",
        "His experience in guard dog handling and site supervision makes him a key pillar of the company’s operational strength.",
      ],
    },
    {
      slug: "akosua-danso",
      name: "Akosua Danso",
      role: "Administration Manager",
      image: "/img/staff/akosua_danso.jpg",
      bio: [
        "Akosua Danso manages the administration of WUMRAQ Security Services Limited — personnel records, client contracts, payroll and compliance.",
        "She ensures every guard deployed to a client site is properly vetted, documented and equipped before their first shift.",
        "Her careful management keeps the company running smoothly behind the scenes, so our guards can focus on protecting clients.",
      ],
    },
  ],
  staff: [] as Array<{ slug: string; name: string; role: string; image: string; bio: string[] }>,
};

export const NEWS = {
  posts: [
    {
      slug: "why-your-business-needs-24hr-security",
      title: "Why your business needs 24hr security",
      author: "WUMRAQ Security Team",
      date: "12th Sep 2025",
      source: "WUMRAQ News",
      hits: 342,
      image: "/img/news/24hr-security-training.jpg",
      excerpt:
        "Crime does not keep office hours. From break-ins at dawn to after-hours theft, here is why round-the-clock guarding has become essential for businesses in Ghana...",
      paragraphs: [
        "Crime does not keep office hours. A large share of break-ins, theft and vandalism at business premises in Ghana happen at night, at weekends and during holidays — exactly when premises are empty and unwatched.",
        "A 24-hour security presence changes that. Trained guards on site around the clock deter intruders before they act, control access for visitors and deliveries, detect fire and flood risks early, and respond immediately when alarms go off.",
        "At WUMRAQ Security Services Limited, our guards work in structured day and night shifts with regular supervisor spot checks, so your business is never left unattended. Combined with guard dog patrols for high-risk sites, 24-hour guarding remains the single most effective investment a business can make in its own protection.",
      ],
    },
    {
      slug: "guard-dogs-in-modern-security",
      title: "The role of guard dogs in modern security",
      author: "WUMRAQ Security Team",
      date: "18th Aug 2025",
      source: "WUMRAQ News",
      hits: 287,
      image: "/img/news/guard-dog-patrol.jpg",
      excerpt:
        "A trained guard dog can hear, smell and detect an intruder long before any human can. Here is how our dog sections strengthen the protection of yards and warehouses...",
      paragraphs: [
        "Technology is useful, but nothing replaces the nose and ears of a trained guard dog. A dog can detect an intruder hiding in a dark yard, behind a wall or inside a parked vehicle long before a human guard — or a camera — would notice anything.",
        "Beyond detection, the presence of a dog section is one of the strongest visual deterrents against burglary, vandalism and unlawful entry. Would-be intruders simply move on to easier targets.",
        "WUMRAQ deploys healthy, trained dogs only with licensed, uniformed handlers, and only on command — making our guard dog services safe for staff, clients and visitors while providing powerful protection for warehouses, yards, farms and construction sites.",
      ],
    },
    {
      slug: "choosing-security-for-your-warehouse",
      title: "Choosing the right security for your warehouse",
      author: "WUMRAQ Security Team",
      date: "2nd Jul 2025",
      source: "WUMRAQ News",
      hits: 198,
      image: "/img/news/warehouse-patrol.jpg",
      excerpt:
        "Warehouses and storage yards face unique risks — from cargo theft to pilferage during loading. Here is a practical checklist to secure your facility properly...",
      paragraphs: [
        "Warehouses, factories and storage yards hold valuable goods spread over large areas — which makes them attractive targets for theft, pilferage and unlawful entry, often from exactly the people you least expect.",
        "Effective warehouse security starts with controlled gates: every vehicle, driver and document checked and recorded. It continues with perimeter and yard patrols day and night, supervision of loading and off-loading, and detailed shift handover reports that management can actually rely on.",
        "For large or high-risk sites, WUMRAQ combines 24-hour guards with trained guard dog teams and unannounced supervisor spot checks. The result is a facility where losses drop, staff comply with the rules, and management always knows what happened on every shift.",
      ],
    },
  ],
};

export const CONTACT_HOURS =
  "Official working hours between 8am and 6pm Monday to Friday.";

/** Position Google Maps de la page contacts (Accra, Ghana) */
export const MAP = {
  lat: 5.6037,
  lng: -0.187,
  zoom: 12,
};

export const SERVICE_OPTIONS = [
  "24HRS Security Guard",
  "Guard Dog Services",
  "Security Services to Offices",
  "Security Services to Homes",
  "Security Services to Warehouse",
  "Road And Building Engineering",
];
