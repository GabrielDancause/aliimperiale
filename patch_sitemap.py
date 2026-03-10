import re

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()

new_entry = """  <url>
    <loc>https://aliimperiale.com/blog/dating-app-fatigue.html</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>"""

content = content.replace("  <url>", new_entry, 1)

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched sitemap.xml successfully")
