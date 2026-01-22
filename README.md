# Ali Imperiale Website

Repository for the Ali Imperiale landing page.

---

## 📦 Project Structure

```text
/
├── OpenLinks.json         # Main config (profile, links, theme, etc)
├── themes.ts              # Available themes
├── src/
│   ├── components/        # Reusable Astro components
│   ├── layouts/           # Main layout
│   ├── lib/               # Utilities (e.g. getTheme)
│   ├── pages/             # Astro pages
│   └── styles/            # Global styles and Tailwind
├── public/                # Static files (icons, fonts, avatar)
├── astro.config.mjs       # Astro + Tailwind config
├── package.json           # Dependencies and scripts
└── README.md
```

---

## ⚙ Configuration

- **Profile & links:** All managed in [`OpenLinks.json`](OpenLinks.json).
- **Themes:** Set the `"theme"` value in the JSON to any available in [`themes.ts`](themes.ts): `default`, `ocean`, `forest`, `sunrise`, `ness`, `arctic`, `cherry`, `brutalism`.
- **Icons:** Place your SVGs in `public/icons/` and reference the path in each link.

---

## 📝 How to Edit `OpenLinks.json`

All your profile information, links, and theme settings are managed in the `OpenLinks.json` file at the root of the project. Here’s how to customize it:

### Example Structure

```json
{
  "name": "Your Name",
  "description": "Short bio or description.",
  "avatar": "/avatar.png",
  "theme": "ocean",
  "links": [
    {
      "title": "GitHub",
      "url": "https://github.com/yourusername",
      "icon": "/icons/github.svg"
    },
    {
      "title": "Twitter",
      "url": "https://twitter.com/yourusername",
      "icon": "/icons/twitter.svg"
    }
  ],
  "adultContent": false
}
```

### Fields

- **name:** Your display name.
- **description:** A short description or tagline.
- **avatar:** Path to your profile image (place it in the `public/` folder).
- **theme:** Choose a theme from those available in `themes.ts`.
- **links:** An array of your links. Each link can have:
  - `title`: The label shown on your page.
  - `url`: The destination URL.
  - `icon`: Path to an SVG icon (place SVGs in `public/icons/`).
- **adultContent:** Set to `true` to show a +18 warning banner.

### Customizing

- Add, remove, or edit links as needed.
- Change the theme by updating the `"theme"` value.
- Update your avatar or bio at any time.

After saving changes to `OpenLinks.json`, your site will update automatically in development mode.

---

## 🛠 Available Scripts

| Command            | Action                                         |
|--------------------|------------------------------------------------|
| `npm run dev`      | Start the development server                   |
| `npm run build`    | Build the site for production in `/dist`       |
| `npm run preview`  | Preview the production build locally           |
| `npm run astro`    | Run Astro CLI commands                         |

---

© 2026 Gab Ventures. All Rights Reserved. Content and branding are proprietary. Theme based on OpenLinks.
