import { defineConfig } from 'astro/config';

/* import data from "./OpenLinks.json"; */


import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://aliimperiale.com',
  base: '/',
  vite: {
    plugins: [tailwindcss()]
  }
});
