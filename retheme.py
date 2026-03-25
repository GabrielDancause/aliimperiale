#!/usr/bin/env python3
"""Batch retheme all Ali Imperiale pages to terra/cream design."""
import os, re, glob

# Pages to skip (already redesigned or special)
SKIP = {
    'index.html',
    'index-backup-20260325.html',
    'index-redesign.html',
    '404.html',
    'blog/index.html',
    'blog/oral-sex-positions-that-wont-make-her-orgasm.html',
}

# Color replacements for inline styles
COLOR_MAP = {
    '#FAF8EB': '#faf6f0',
    '#faf8eb': '#faf6f0',
    '#2E3E24': '#1a1510',
    '#2e3e24': '#1a1510',
    '#AD9846': '#c0603a',
    '#ad9846': '#c0603a',
    '#C6C8BB': '#e8c4a8',
    '#c6c8bb': '#e8c4a8',
    '#555549': '#7a6a5a',
    '#444438': '#7a6a5a',
    '#422626': '#1a1510',
    '#c4ad52': '#9e4626',
    '#8a8a7a': '#7a6a5a',
    '#e65100': '#c0603a',
}

# Font replacement
FONT_LINK_OLD = "https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap"
FONT_LINK_OLD2 = "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap"
FONT_LINK_NEW = "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Serif+Display:ital@0;1&display=swap"

# New bar HTML
BAR_HTML = '<div class="bar">\n  ✨ Exclusive content, early access & real talk — <a href="https://www.patreon.com/c/aliimperiale">Join the Patreon</a>\n</div>\n\n'

def get_depth(filepath):
    """How many dirs deep from root (for ../ prefix)."""
    parts = filepath.replace('\\', '/').split('/')
    return len(parts) - 1  # e.g. blog/foo.html = 1

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    depth = get_depth(filepath)
    prefix = '../' * depth
    
    # 1. Replace Google Fonts link
    content = content.replace(FONT_LINK_OLD, FONT_LINK_NEW)
    content = content.replace(FONT_LINK_OLD2, FONT_LINK_NEW)
    
    # 2. Replace colors in inline <style> blocks and inline style attributes
    for old_color, new_color in COLOR_MAP.items():
        content = content.replace(old_color, new_color)
    
    # 3. Replace font family references in inline styles
    content = content.replace("font-family: 'Montserrat'", "font-family: 'DM Sans'")
    content = content.replace("font-family: 'New Standard'", "font-family: 'Playfair Display'")
    content = content.replace("font-family: 'The Bloomington'", "font-family: 'DM Serif Display'")
    content = content.replace("font-family:'Montserrat'", "font-family:'DM Sans'")
    content = content.replace("font-family:'New Standard'", "font-family:'Playfair Display'")
    content = content.replace("font-family:'The Bloomington'", "font-family:'DM Serif Display'")
    # Also in CSS strings with , sans-serif etc
    content = content.replace("'Montserrat', sans-serif", "'DM Sans', sans-serif")
    content = content.replace("'New Standard', Georgia, serif", "'Playfair Display', Georgia, serif")
    content = content.replace("'The Bloomington', cursive", "'DM Serif Display', serif")
    content = content.replace("Montserrat, sans-serif", "'DM Sans', sans-serif")
    
    # 4. Add bar + fix nav if not already present
    if '<div class="bar">' not in content:
        # Insert bar right after <body> tag
        content = re.sub(
            r'(<body[^>]*>)',
            r'\1\n\n' + BAR_HTML,
            content,
            count=1
        )
    
    # 5. Fix nav background color that was overridden inline
    # Replace old nav background with transparent (shared.css handles it)
    content = re.sub(
        r'(\.nav\s*\{[^}]*?)background(?:-color)?:\s*#1a1510\s*;',
        r'\1background: rgba(250,246,240,.93);',
        content
    )
    content = re.sub(
        r'(nav\s*\{[^}]*?)background(?:-color)?:\s*#1a1510\s*;',
        r'\1background: rgba(250,246,240,.93);',
        content
    )
    
    # 6. Fix CTA section backgrounds that got wrong-mapped
    # The CTA section should stay dark (ink)
    # Already mapped #2E3E24 -> #1a1510, which is correct for dark sections
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Collect all HTML files
all_files = []
for f in glob.glob('*.html'):
    if f not in SKIP:
        all_files.append(f)
for f in glob.glob('blog/*.html'):
    rel = f.replace('\\', '/')
    if rel not in SKIP:
        all_files.append(rel)

print(f"Processing {len(all_files)} files...")

changed = 0
for filepath in sorted(all_files):
    try:
        if process_file(filepath):
            changed += 1
    except Exception as e:
        print(f"  ERROR {filepath}: {e}")

print(f"Done! {changed}/{len(all_files)} files updated.")
