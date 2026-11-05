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
})();
