#!/bin/bash
# Batch 1 : sliders + services securite
OUT=/home/z/my-project/site/ai-img
mkdir -p "$OUT"
Q="no text, no letters, no logo, no watermark, photorealistic, professional corporate photography, high quality, detailed, West Africa Ghana context"

z-ai image -p "Team of five confident uniformed security guards standing in formation in front of a modern corporate office building entrance in Accra Ghana, dark green uniforms with dark berets, one supervisor giving briefing, morning light, $Q" -o "$OUT/slider1.png" -s 1024x1024
z-ai image -p "Road construction site in West Africa with yellow motor grader and steamroller compacting fresh asphalt, workers in orange high visibility vests and helmets, clear blue sky, $Q" -o "$OUT/slider2.png" -s 1024x1024
z-ai image -p "Professional security dog handler in dark green uniform walking with an alert German shepherd guard dog on leash, patrolling along a fence line of an industrial warehouse yard at dusk, warm lights, $Q" -o "$OUT/slider3.png" -s 1024x1024
z-ai image -p "Uniformed security guard in dark green uniform standing watch at the gatehouse of a modern corporate compound in Accra Ghana, checkpoint barrier, daylight, vigilant posture, $Q" -o "$OUT/service_24h.png" -s 1024x1024
z-ai image -p "Professional security dog handler in dark green uniform with a German shepherd guard dog beside a fenced construction site, daytime, strong visible deterrence, $Q" -o "$OUT/service_dog.png" -s 1024x1024
z-ai image -p "Smart security officer in dark green uniform at the reception desk of a modern glass office lobby, welcoming corporate visitors, polished floor, daytime, $Q" -o "$OUT/service_office.png" -s 1024x1024
z-ai image -p "Friendly uniformed security guard in dark green uniform at the gate of a residential estate with houses and palm trees behind, checking a visitor list on a clipboard, Ghana, daylight, $Q" -o "$OUT/service_residential.png" -s 1024x1024
z-ai image -p "Security officer in dark green uniform and reflective vest inspecting a large warehouse loading bay with stacked pallets and a forklift, industrial interior, bright lights, $Q" -o "$OUT/service_warehouse.png" -s 1024x1024
echo "BATCH1 DONE"; ls -la "$OUT"
