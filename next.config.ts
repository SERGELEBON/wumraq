import type { NextConfig } from "next";
import fs from "fs";
import path from "path";

// The WUMRAQ website is a full static clone (design of safenetsecuritygh.com
// preserved 100%) served from /public. Every page lives in its own folder as
// index.html so that clean URLs like /2/about-us resolve naturally.
// We derive a rewrite table from the filesystem at config load time:
//   /2/about-us  ->  /2/about-us/index.html
const PUBLIC_DIR = path.join(process.cwd(), "public");

function collectPageRewrites(): { source: string; destination: string }[] {
  const rewrites: { source: string; destination: string }[] = [
    { source: "/", destination: "/index.html" },
  ];
  const walk = (dir: string, rel: string) => {
    let entries: fs.Dirent[] = [];
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }
    if (entries.some((e) => e.isFile() && e.name === "index.html") && rel) {
      rewrites.push({
        source: "/" + rel,
        destination: "/" + rel + "/index.html",
      });
    }
    for (const e of entries) {
      if (e.isDirectory()) {
        walk(path.join(dir, e.name), rel ? rel + "/" + e.name : e.name);
      }
    }
  };
  walk(PUBLIC_DIR, "");
  return rewrites;
}

const nextConfig: NextConfig = {
  output: "standalone",
  typescript: {
    ignoreBuildErrors: true,
  },
  reactStrictMode: false,
  async rewrites() {
    return {
      beforeFiles: collectPageRewrites(),
      afterFiles: [],
      fallback: [],
    };
  },
};

export default nextConfig;
