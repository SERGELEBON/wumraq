#!/bin/bash
OUT=/home/z/my-project/site/ai-img
mkdir -p "$OUT"
Q="no text, no letters, no logo, no watermark, photorealistic, professional corporate photography, high quality, detailed, West Africa Ghana context"

z-ai image -p "Road construction engineering site with asphalt paver machine laying fresh asphalt, workers in high visibility vests and white helmets, road roller, Ghana highway project, sunny day, $Q" -o "$OUT/service_road.png" -s 1024x1024
z-ai image -p "Building construction site with reinforced concrete structure, scaffolding, tower crane and blockwork walls, African construction workers with helmets, daylight, $Q" -o "$OUT/service_building.png" -s 1024x1024
z-ai image -p "Interior renovation works: African craftsmen painting a wall with rollers and installing floor tiles in a modern office under refurbishment, ladder and tools, bright natural light, $Q" -o "$OUT/service_renovation.png" -s 1024x1024
z-ai image -p "Large yellow excavator doing earthmoving and site clearing works, dump truck being loaded with red laterite soil, African site workers in helmets and hi-vis, dust, sunny day, $Q" -o "$OUT/service_civil.png" -s 1024x1024
z-ai image -p "Security operations control room with wall of CCTV monitors showing camera feeds, African supervisor in dark green uniform jacket standing and monitoring screens, modern equipment, $Q" -o "$OUT/about.png" -s 1024x1024
z-ai image -p "Wide panoramic dusk skyline banner of an African city business district with modern towers, construction cranes and a main road with light trails, dark green and deep teal color grading, moody cinematic lighting, $Q" -o "$OUT/crumb.png" -s 1440x720
z-ai image -p "Group of private security guards in dark green uniforms during outdoor training drill in Ghana, instructor demonstrating procedures, they stand in line listening, daytime, $Q" -o "$OUT/news.png" -s 1344x768
z-ai image -p "Professional portrait of a confident Ghanaian businessman in his forties wearing an elegant dark green suit with white shirt, standing in a modern office, warm smile, studio quality headshot, $Q" -o "$OUT/staff.png" -s 864x1152
echo "BATCH2 DONE"; ls -la "$OUT" | wc -l
