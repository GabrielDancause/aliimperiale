import re

with open('blog/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix spacing between the two links
content = content.replace("</div>\n    </a>\n<a href=\"i-tried-a", "</div>\n    </a>\n\n    <a href=\"i-tried-a")

with open('blog/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Formatted blog/index.html successfully")
