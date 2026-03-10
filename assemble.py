import re

with open('blog/best-vibrators-for-beginners.html', 'r') as f:
    template = f.read()

with open('draft.html', 'r') as f:
    draft = f.read()

# Make changes to the template
# 1. Update title and meta tags
template = re.sub(r'<title>.*?</title>', '<title>The Modern Dating App Landscape: A 2026 Analysis | Ali Imperiale</title>', template)
template = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="A data-driven study on 2026 dating app trends, success rates, demographics, and best practices for every age group.">', template)
template = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="The Modern Dating App Landscape: A 2026 Analysis">', template)
template = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="A data-driven study on 2026 dating app trends, success rates, demographics, and best practices for every age group.">', template)
template = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://aliimperiale.com/dating-app-analysis-2026.html">', template)
template = re.sub(r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="The Modern Dating App Landscape: A 2026 Analysis">', template)
template = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://aliimperiale.com/dating-app-analysis-2026.html">', template)

# Update paths since it's in root directory
template = template.replace('href="../', 'href="')
template = template.replace('src="../', 'src="')
template = template.replace('href="/blog/"', 'href="/blog/"')
template = template.replace('href="/about.html"', 'href="/about.html"')

# Update JSON-LD schema
article_schema = """
[
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "The Modern Dating App Landscape: A 2026 Analysis",
    "author": {
      "@type": "Person",
      "name": "Ali Imperiale",
      "url": "https://aliimperiale.com"
    },
    "publisher": {
      "@type": "Person",
      "name": "Ali Imperiale",
      "url": "https://aliimperiale.com"
    },
    "url": "https://aliimperiale.com/dating-app-analysis-2026.html",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://aliimperiale.com/dating-app-analysis-2026.html"
    },
    "description": "A data-driven study on 2026 dating app trends, success rates, demographics, and best practices for every age group.",
    "image": {
      "@type": "ImageObject",
      "url": "https://aliimperiale.com/avatar-pro.jpg",
      "width": 1280,
      "height": 720
    },
    "datePublished": "2026-03-10",
    "dateModified": "2026-03-10"
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Are dating apps still working in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, but the way we use them has changed. Blind swiping is down, and intentional dating (using apps with longer profiles and voice prompts) is seeing the highest retention and success rates."
        }
      },
      {
        "@type": "Question",
        "name": "What is the best dating app for serious relationships right now?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Based on 2026 data, apps that require more upfront effort like Hinge tend to yield the highest long-term success rates for users seeking serious relationships, especially in the 25-40 age demographic."
        }
      },
      {
        "@type": "Question",
        "name": "How important are voice notes and video calls before a first date?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Crucial. Over 60% of successful matches in 2026 involve a voice note exchange or a quick video call before meeting in person. It’s the best way to vibe-check someone and ensure safety before committing to a date."
        }
      },
      {
        "@type": "Question",
        "name": "Is it safe to use dating apps?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Safety standards have improved significantly. Look for apps with AI-powered photo verification, in-app calling (so you don't share your number), and harassment filters. Always share your location with a friend and meet in a public place."
        }
      }
    ]
  }
]
"""
template = re.sub(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">\n' + article_schema + '\n</script>', template, flags=re.DOTALL)

# Breadcrumb
breadcrumb = """
  <div class="breadcrumb">
    <a href="/">Home</a><span>&rsaquo;</span><a href="/blog/">Blog</a><span>&rsaquo;</span> The Modern Dating App Landscape: A 2026 Analysis
  </div>
"""
template = re.sub(r'<div class="breadcrumb">.*?</div>', breadcrumb, template, flags=re.DOTALL)

# Header
header = """
  <header class="article-header">
    <p class="article-date">March 10, 2026</p>
    <h1>The Modern Dating App Landscape: A 2026 Analysis</h1>
    <p class="article-subtitle">Data-driven insights on trends, success rates, and how to navigate online dating without losing your mind.</p>
  </header>
"""
template = re.sub(r'<header class="article-header">.*?</header>', header, template, flags=re.DOTALL)

# Add FAQ HTML visually
faq_html = """
      <h2>Frequently Asked Questions</h2>
      <div class="faq-section">
          <h3>Are dating apps still working in 2026?</h3>
          <p>Yes, but the way we use them has changed. Blind swiping is down, and intentional dating (using apps with longer profiles and voice prompts) is seeing the highest retention and success rates.</p>

          <h3>What is the best dating app for serious relationships right now?</h3>
          <p>Based on 2026 data, apps that require more upfront effort like Hinge tend to yield the highest long-term success rates for users seeking serious relationships, especially in the 25-40 age demographic.</p>

          <h3>How important are voice notes and video calls before a first date?</h3>
          <p>Crucial. Over 60% of successful matches in 2026 involve a voice note exchange or a quick video call before meeting in person. It’s the best way to vibe-check someone and ensure safety before committing to a date.</p>

          <h3>Is it safe to use dating apps?</h3>
          <p>Safety standards have improved significantly. Look for apps with AI-powered photo verification, in-app calling (so you don't share your number), and harassment filters. Always share your location with a friend and meet in a public place.</p>
      </div>
"""

# Replace the article body
template = re.sub(r'<article class="article-body">.*?</article>', f'<article class="article-body">\n{draft}\n{faq_html}\n</article>', template, flags=re.DOTALL)


# Update email capture
template = re.sub(r'data-post-slug=".*?"', 'data-post-slug="dating-app-analysis-2026"', template)

# Write out the new file
with open('dating-app-analysis-2026.html', 'w') as f:
    f.write(template)

print("Assembled dating-app-analysis-2026.html")
