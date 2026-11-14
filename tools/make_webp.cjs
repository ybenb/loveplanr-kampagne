#!/usr/bin/env node
/* Wandelt Website-Bilder in WebP um (assets/pins/*-500.jpg, assets/img/*.jpg). Braucht das Paket sharp.
   Die Pins in voller Grösse bleiben JPG, weil Pinterest PNG und JPEG verlangt.
   hero-900.jpg bleibt zusätzlich als Vorschaubild für geteilte Links. */
const sharp = require('sharp'), fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..');
(async () => {
  for (const [dir, test, q] of [['assets/pins', /-500\.jpg$/, 74], ['assets/img', /\.jpg$/, 68]]) {
    for (const f of fs.readdirSync(path.join(root, dir)).filter(n => test.test(n))) {
      const src = path.join(root, dir, f);
      await sharp(src).webp({ quality: q }).toFile(src.replace(/\.jpg$/, '.webp'));
      if (f !== 'hero-900.jpg') fs.unlinkSync(src);
    }
  }
  /* Kleine Pin-Varianten für das Handy und das Raster (srcset), aus den Pins in voller Grösse */
  for (const f of fs.readdirSync(path.join(root, 'assets/pins')).filter(n => /^\d\d-.*\.jpg$/.test(n) && !/-500\.jpg$/.test(n))) {
    const src = path.join(root, 'assets/pins', f);
    await sharp(src).resize({ width: 300 }).webp({ quality: 72 }).toFile(src.replace(/\.jpg$/, '-300.webp'));
  }
})();
