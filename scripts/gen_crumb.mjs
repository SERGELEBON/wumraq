import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

async function main() {
  const zai = await ZAI.create();
  const prompt = "Wide panoramic dusk skyline of an African city business district with modern towers, construction cranes and a main road with car light trails, dark green and deep teal color grading, moody cinematic lighting, no text, no letters, no logo, no watermark, photorealistic, high quality";
  try {
    const response = await zai.images.generations.create({ prompt, size: '1856x512' });
    fs.writeFileSync('/home/z/my-project/site/ai-img/crumb.png', Buffer.from(response.data[0].base64, 'base64'));
    console.log('OK 1856x512');
  } catch (e) {
    console.error('1856x512 failed:', e.message);
    const r2 = await zai.images.generations.create({ prompt, size: '1440x720' });
    fs.writeFileSync('/home/z/my-project/site/ai-img/crumb.png', Buffer.from(r2.data[0].base64, 'base64'));
    console.log('OK fallback');
  }
}
main().catch(e => { console.error(e); process.exit(1); });
