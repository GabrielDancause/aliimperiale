import re

def get_snippet(filename, start_marker, end_marker=None, include_end=True):
    with open(filename, 'r') as f:
        content = f.read()

    start_idx = content.find(start_marker)
    if start_idx == -1:
        return ""

    if end_marker:
        end_idx = content.find(end_marker, start_idx)
        if end_idx == -1:
            return ""
        if include_end:
            return content[start_idx:end_idx + len(end_marker)]
        else:
            return content[start_idx:end_idx]
    else:
        return content[start_idx:]

with open('index.html', 'r') as f:
    index_content = f.read()

# Extract parts
nav_match = re.search(r'<nav class="site-nav">.*?</nav>', index_content, re.DOTALL)
nav_html = nav_match.group(0) if nav_match else ""

footer_match = re.search(r'<footer class="site-footer">.*?</footer>', index_content, re.DOTALL)
footer_html = footer_match.group(0) if footer_match else ""

# Extract style for .site-nav
nav_style_match = re.search(r'\.site-nav\s*\{.*?\}(?=\s*\n\s*\.)', index_content, re.DOTALL)
nav_style_1 = nav_style_match.group(0) if nav_style_match else ""

nav_links_match = re.search(r'\.nav-links\s*\{.*?\}(?=\s*\n\s*\.)', index_content, re.DOTALL)
nav_links_style = nav_links_match.group(0) if nav_links_match else ""

nav_links_li_match = re.search(r'\.nav-links li\s*\{.*?\}(?=\s*\n\s*\.)', index_content, re.DOTALL)
nav_links_li_style = nav_links_li_match.group(0) if nav_links_li_match else ""

nav_links_a_match = re.search(r'\.nav-links a\s*\{.*?\}(?=\s*\n\s*@|\s*\n\s*\.)', index_content, re.DOTALL)
nav_links_a_style = nav_links_a_match.group(0) if nav_links_a_match else ""

base_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-G86C7NJG3F"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-G86C7NJG3F');</script>
  <script src="consent.js" defer></script>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Best Sex Education Apps & Digital Tools 2026 | Ali Imperiale</title>
  <meta name="description" content="A comprehensive review and comparison of the best sexual wellness and education apps for 2026, including period tracking, kink education, relationships, and more.">

  <!-- Open Graph -->
  <meta property="og:title" content="Best Sex Education Apps & Digital Tools 2026 | Ali Imperiale">
  <meta property="og:description" content="A comprehensive review and comparison of the best sexual wellness and education apps for 2026, including period tracking, kink education, relationships, and more.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://aliimperiale.com/best-sex-education-apps-2026.html">
  <meta property="og:image" content="https://aliimperiale.com/avatar-pro.jpg">
  <meta property="og:image:width" content="400">
  <meta property="og:image:height" content="400">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="Best Sex Education Apps 2026">
  <meta name="twitter:description" content="A comprehensive review and comparison of the best sexual wellness and education apps for 2026.">
  <meta name="twitter:image" content="https://aliimperiale.com/avatar-pro.jpg">

  <!-- Fonts & Styles -->
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap"></noscript>
  <link rel="stylesheet" href="shared.css">

  <style>
    /* Site Nav Styles inherited from index.html */
    .site-nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 2rem;
      background: var(--color-bg);
      position: sticky;
      top: 0;
      z-index: 100;
      border-bottom: 1px solid rgba(46, 62, 36, 0.1);
    }}
    .nav-logo {{
      height: 32px;
      width: auto;
      display: block;
    }}
    .nav-links {{
      display: flex;
      list-style: none;
      gap: 2rem;
      margin: 0;
      padding: 0;
      align-items: center;
    }}
    .nav-links a {{
      color: var(--color-text);
      text-decoration: none;
      font-weight: 500;
      font-size: 0.95rem;
      transition: color 0.2s ease;
    }}
    .nav-links a:hover,
    .nav-links a.active {{
      color: var(--color-accent);
    }}

    @media (max-width: 768px) {{
      .nav-links {{
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: var(--color-bg);
        flex-direction: column;
        padding: 1rem;
        gap: 1rem;
        border-bottom: 1px solid rgba(46, 62, 36, 0.1);
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
      }}
      .nav-links.show {{
        display: flex;
      }}
    }}
  </style>
</head>
<body>
  {nav_html.replace('class="active"', '')}

  <!-- CONTENT_PLACEHOLDER -->

  {footer_html}
  <script src="mobile-nav.js"></script>
</body>
</html>
"""

with open('best-sex-education-apps-2026.html', 'w') as f:
    f.write(base_html)

print("Created best-sex-education-apps-2026.html")
