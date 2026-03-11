import xml.etree.ElementTree as ET
from datetime import datetime

# Update lists.html
with open('lists.html', 'r') as f:
    lists_content = f.read()

new_card = """
    <a href="/best-sex-education-apps-2026.html" class="category-card">
      <span class="card-tag">Curated List</span>
      <h3>Best Sex Education Apps & Digital Tools 2026</h3>
      <p>Detailed reviews, pricing comparisons, privacy assessments, and feature matrices for the top sexual wellness and education apps.</p>
    </a>"""

lists_content = lists_content.replace('<div class="category-grid">', f'<div class="category-grid">\n{new_card}')

with open('lists.html', 'w') as f:
    f.write(lists_content)
print("Updated lists.html")

# Update sitemap.xml
ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
tree = ET.parse('sitemap.xml')
root = tree.getroot()

ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

# Check if URL already exists
exists = False
for url in root.findall('sm:url', ns):
    loc = url.find('sm:loc', ns)
    if loc is not None and loc.text == 'https://aliimperiale.com/best-sex-education-apps-2026.html':
        exists = True
        break

if not exists:
    new_url = ET.Element('url')
    loc = ET.SubElement(new_url, 'loc')
    loc.text = 'https://aliimperiale.com/best-sex-education-apps-2026.html'
    lastmod = ET.SubElement(new_url, 'lastmod')
    lastmod.text = datetime.now().strftime('%Y-%m-%d')
    changefreq = ET.SubElement(new_url, 'changefreq')
    changefreq.text = 'monthly'
    priority = ET.SubElement(new_url, 'priority')
    priority.text = '0.8'

    root.append(new_url)
    tree.write('sitemap.xml', encoding='utf-8', xml_declaration=True)
    print("Updated sitemap.xml")
else:
    print("URL already exists in sitemap.xml")
