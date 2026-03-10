import re

with open('blog/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_card = """
    <a href="dating-app-fatigue.html" class="blog-card" data-category="relationships">
      <div class="info">
        <div class="card-date">March 10, 2026</div>
        <div class="card-title">Dating App Fatigue Is Real &mdash; Here's How to Actually Meet Someone</div>
        <div class="card-excerpt">Exhausted by dating apps? Let's talk about why swiping is burning you out, algorithm tricks, and how to actually meet someone in real life without the dread.</div>
      </div>
    </a>
"""

content = re.sub(r'<div class="blog-grid">\s*', f'<div class="blog-grid">\n{new_card}', content, count=1)

with open('blog/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched blog/index.html successfully")
