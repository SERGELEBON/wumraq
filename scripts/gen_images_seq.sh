#!/bin/bash
# WUMRAQ image generation - sequential with retry/backoff to avoid 429
DIR=/home/z/my-project/scripts/gen-images
mkdir -p $DIR
cd $DIR

gen() {
  local out="$1"; local prompt="$2"; local size="$3"
  for attempt in 1 2 3 4 5; do
    if z-ai image -p "$prompt" -o "$out" -s "$size" >/dev/null 2>&1; then
      if [ -f "$out" ]; then echo "OK $out (attempt $attempt)"; return 0; fi
    fi
    echo "RETRY $out (attempt $attempt failed)"; sleep $((attempt*10))
  done
  echo "FAIL $out"; return 1
}

gen logo-emblem.png "Professional circular security company emblem badge logo, round crest with a bold eagle with spread wings above a shield, deep teal green and white color palette, clean flat vector logo style, crisp edges, centered on pure white background, no text, no letters, high quality" 1024x1024; sleep 3

gen slider-1.jpg "Two professional African security guards in dark teal green uniforms with berets standing at the entrance of a modern corporate office building in Accra Ghana, daytime, confident posture, photorealistic professional corporate photography, high quality, detailed" 1344x768; sleep 3

gen slider-2.jpg "Professional African security guard in dark green uniform walking with a German Shepherd guard dog on a leash during night patrol around an industrial premises, floodlights, dramatic lighting, photorealistic professional photography, high quality" 1344x768; sleep 3

gen slider-3.jpg "African security officer in dark teal green uniform at the gate of a warehouse facility directing a vehicle at a boom barrier, daytime, photorealistic professional photography, high quality, detailed" 1344x768; sleep 3

gen about-team.jpg "Group photo of an African security company team in Ghana, eight guards in dark teal green uniforms standing in two rows with a manager in a suit in front of their company office building, daylight, photorealistic professional corporate photography, high quality" 1344x768; sleep 3

gen svc-24hr.jpg "Security guard in dark teal green uniform inside a small guard post at the gated compound entrance at dusk, warm floodlight glowing, 24 hours security concept, photorealistic, high quality, detailed" 1024x1024; sleep 3

gen svc-dog.jpg "Professional security dog handler with a German Shepherd guard dog patrolling along the perimeter fence line of a commercial property in Ghana, daytime, photorealistic, high quality" 1024x1024; sleep 3

gen svc-offices.jpg "Professional African security officer in dark teal uniform standing at the reception lobby of a modern office building, corporate environment, photorealistic, high quality, detailed" 1024x1024; sleep 3

gen svc-homes.jpg "Security guard at the entrance gate of an upscale residential estate in Ghana, boom barrier and white guard house, palm trees, daytime, photorealistic, high quality" 1024x1024; sleep 3

gen svc-warehouse.jpg "Security guard holding a flashlight patrolling between large storage racks inside a warehouse at night, industrial security, photorealistic, high quality, detailed" 1024x1024; sleep 3

gen svc-engineering.jpg "Road construction site in Ghana with a yellow excavator and workers in helmets and reflective vests building a new road, civil engineering works, daytime, photorealistic, high quality, detailed" 1024x1024; sleep 3

gen what-we.jpg "Security operations control room with a wall of CCTV monitors showing camera feeds, two African security staff monitoring the screens, dark room with teal screen glow, photorealistic, high quality" 1024x1024; sleep 3

gen crumb.jpg "Wide dark moody banner photo, silhouettes of security guards standing in a line at dusk, deep dark teal green tone, very dark background suitable for white text overlay, professional photography, high quality" 1440x720; sleep 3

gen team-1.jpg "Professional corporate portrait of a confident Ghanaian woman in her forties, managing director of a security company, wearing an elegant dark teal blazer, modern office background, photorealistic, studio lighting, high quality" 864x1152; sleep 3

gen team-2.jpg "Professional corporate portrait of a Ghanaian man in his fifties, operations manager of a security company, wearing a dark green suit and tie, modern office background, photorealistic, studio lighting, high quality" 864x1152; sleep 3

gen team-3.jpg "Professional portrait of a young Ghanaian male security supervisor in a dark teal security uniform with epaulettes and beret, neutral light background, photorealistic, studio lighting, high quality" 864x1152; sleep 3

gen team-4.jpg "Professional corporate portrait of a Ghanaian woman in her thirties, administration manager of a security company, smart business attire, modern office background, photorealistic, studio lighting, high quality" 864x1152; sleep 3

gen news-1.jpg "Security guards training drill at an outdoor training ground in Ghana, instructor demonstrating techniques to a line of guards in dark green uniforms, photorealistic, high quality, detailed" 1344x768; sleep 3

gen news-2.jpg "White security patrol vehicle with amber beacon lights parked at an industrial facility at dusk, African security guards walking nearby, photorealistic, high quality" 1344x768; sleep 3

gen news-3.jpg "Close-up of a security officer hands holding a two-way radio at a warehouse gate at night, dark teal uniform sleeve, photorealistic, high quality, detailed" 1344x768

echo "=== ALL DONE ==="
ls -la $DIR
