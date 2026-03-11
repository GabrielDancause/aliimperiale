import xml.etree.ElementTree as ET
try:
    ET.parse('sitemap.xml')
    print("Sitemap XML is valid.")
except Exception as e:
    print("Invalid XML:", e)
