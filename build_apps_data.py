import json

app_data = [
    {
        "id": "app-omgyes",
        "name": "OMGyes",
        "categoryId": "sex-education",
        "categoryName": "Sex Education & Wellness",
        "priceId": "paid",
        "priceName": "One-time Purchase ($49/season)",
        "platformId": "web",
        "platforms": ["Web App", "Mobile Web"],
        "privacy": "Excellent. Does not require app download (no App Store tracking). Data is encrypted and not sold to third parties.",
        "pros": ["Science-backed research on actual pleasure", "Explicit, educational videos with real people", "Interactive touch screen elements"],
        "cons": ["Web-based only (no native app)", "High upfront cost per season"],
        "review": "OMGyes remains the gold standard for pleasure-based sex education. Instead of vague advice, it relies on extensive research from thousands of women to map out specific techniques that actually work. The interactive interface allows users to practice techniques on-screen, making it an invaluable tool for exploring vulva owners' pleasure, whether solo or with a partner.",
        "testimonial": "\"This completely changed how my partner and I communicate about touch. The specific vocabulary it gave us was life-changing.\""
    },
    {
        "id": "app-clue",
        "name": "Clue",
        "categoryId": "period-tracking",
        "categoryName": "Period Tracking & Fertility",
        "priceId": "free",
        "priceName": "Free / Premium ($39.99/yr)",
        "platformId": "all",
        "platforms": ["iOS", "Android"],
        "privacy": "European-based (GDPR compliant). Explicitly states they do not and will not sell health data to advertisers or data brokers.",
        "pros": ["Science-based, non-pink/gender-neutral design", "Comprehensive symptom tracking", "Excellent privacy policy"],
        "cons": ["Advanced fertility features require paid tier", "Can feel clinical for some users"],
        "review": "In a post-Roe landscape, privacy is the number one feature of any cycle tracking app. Clue leads the pack with strict European data protections and a commitment to never selling user data. Beyond privacy, it offers a highly customizable tracking experience that correlates mood, energy, and sexual desire with your cycle, without the patronizing floral designs common in the space.",
        "testimonial": "\"I appreciate the gender-neutral design and knowing my data isn't being sold. It's accurate and straightforward.\""
    },
    {
        "id": "app-paired",
        "name": "Paired",
        "categoryId": "relationship",
        "categoryName": "Relationship Building",
        "priceId": "free",
        "priceName": "Free / Premium ($69.99/yr)",
        "platformId": "all",
        "platforms": ["iOS", "Android"],
        "privacy": "Standard app privacy. Partners link accounts but data is stored securely. Premium required for full privacy controls.",
        "pros": ["Daily prompts spark meaningful conversation", "Expert-led relationship advice", "Fun quizzes to test partner knowledge"],
        "cons": ["Expensive annual subscription", "Requires partner participation to be effective"],
        "review": "Paired gamifies relationship maintenance by sending daily questions to both partners. You can only see your partner's answer once you've answered yourself. It's excellent for couples looking to break out of routine communication ('How was work?') and dive into deeper topics around intimacy, future goals, and emotional needs.",
        "testimonial": "\"We've been married for 8 years and this app helped us discover things we never knew about each other.\""
    },
    {
        "id": "app-dipsea",
        "name": "Dipsea",
        "categoryId": "meditation",
        "categoryName": "Meditation & Intimacy",
        "priceId": "paid",
        "priceName": "Subscription ($59.99/yr)",
        "platformId": "all",
        "platforms": ["iOS", "Android", "Web"],
        "privacy": "Good. Listening history is kept private. Standard account data collection.",
        "pros": ["High-quality audio erotica", "Guided intimacy sessions for couples", "Diverse representation in stories"],
        "cons": ["No free tier (only trial)", "Audio-only format isn't for everyone"],
        "review": "Dipsea bridges the gap between mindfulness and arousal. It's essentially 'Headspace for intimacy.' The app features feminist, diverse audio stories designed to help users get out of their heads and into their bodies. Their guided sessions for couples are particularly effective for transitioning from stressed-out roommates to romantic partners.",
        "testimonial": "\"It's the perfect way to wind down and get in the mood without the visual intensity of traditional adult content.\""
    },
    {
        "id": "app-coral",
        "name": "Coral",
        "categoryId": "sex-education",
        "categoryName": "Sex Education & Wellness",
        "priceId": "paid",
        "priceName": "Subscription ($59.99/yr)",
        "platformId": "all",
        "platforms": ["iOS", "Android"],
        "privacy": "Strong privacy focus. Anonymous community features. Data is encrypted.",
        "pros": ["Science-backed intimacy exercises", "Expert Q&A forums", "Focus on desire discrepancy"],
        "cons": ["Community features can be hit or miss", "Steep learning curve for some exercises"],
        "review": "Coral acts as a sexual wellness coach in your pocket. It's particularly strong for couples dealing with mismatched libidos or individuals looking to understand their own desire frameworks. The app provides structured exercises, guided meditations, and a safe, anonymous community to ask questions you might be too embarrassed to ask elsewhere.",
        "testimonial": "\"The guided exercises helped me completely reframe my anxiety around initiation.\""
    },
    {
        "id": "app-mojo",
        "name": "Mojo",
        "categoryId": "sex-education",
        "categoryName": "Sex Education & Wellness",
        "priceId": "paid",
        "priceName": "Subscription ($79.99/yr)",
        "platformId": "all",
        "platforms": ["iOS", "Android"],
        "privacy": "Specializes in sensitive data protection. Anonymous profiles supported.",
        "pros": ["Specifically targets performance anxiety", "Cognitive Behavioral Therapy (CBT) approach", "Created by clinical psychologists"],
        "cons": ["Primarily focused on erectile issues", "Premium pricing"],
        "review": "Mojo is a standout tool designed specifically to address psychological erectile dysfunction and performance anxiety. Using CBT techniques, it helps users break the cycle of anxiety and physical response. It's a fantastic, private alternative or supplement to traditional therapy, providing actionable exercises to rebuild sexual confidence.",
        "testimonial": "\"Better than any pill. It actually helped me address the mental block that was causing the physical issue.\""
    },
    {
        "id": "app-lex",
        "name": "Lex",
        "categoryId": "health-screening", # It's LGBTQ+, let's map appropriately based on categories, perhaps relationship or we can add LGBTQ+ tag visually
        "categoryName": "LGBTQ+ Community & Connection",
        "priceId": "free",
        "priceName": "Free",
        "platformId": "all",
        "platforms": ["iOS", "Android"],
        "privacy": "Text-based profiles. Users control identity disclosure. Standard social app data collection.",
        "pros": ["Text-first approach reduces superficiality", "Inclusive space for queer, trans, and non-binary folks", "Great for finding platonic or romantic connections"],
        "cons": ["UI can be clunky", "Smaller user base outside major cities"],
        "review": "While technically a social/dating app, Lex is an essential digital tool for queer sexual wellness. Inspired by old-school newspaper personal ads, it’s text-first, focusing on who people are rather than just what they look like. It's an invaluable resource for finding community, education, and safe relationships for LGBTQ+ individuals.",
        "testimonial": "\"It feels so much safer and more intentional than traditional swipe-based dating apps.\""
    },
    {
        "id": "app-kink-academy",
        "name": "Kink Academy",
        "categoryId": "kink",
        "categoryName": "Kink Education",
        "priceId": "paid",
        "priceName": "Subscription ($15/mo)",
        "platformId": "web",
        "platforms": ["Web App"],
        "privacy": "Excellent. Independent platform, no app store tracking. Secure billing.",
        "pros": ["Extensive library of safety-first tutorials", "Real educators and practitioners", "Covers everything from impact to rope bondage"],
        "cons": ["No native mobile app", "Outdated website UI"],
        "review": "Kink Academy is the most comprehensive, safety-focused resource for BDSM and kink education. If you want to explore power dynamics, bondage, or impact play safely, this is where you start. The videos feature real practitioners prioritizing consent, negotiation, and physical safety over performative adult content.",
        "testimonial": "\"The emphasis on negotiation and aftercare makes this the only resource I trust for learning new kink skills.\""
    }
]

js_logic = f"""
  <script>
    const appData = {json.dumps(app_data)};

    document.addEventListener('DOMContentLoaded', () => {{
      const appList = document.getElementById('app-list');
      const categoryFilter = document.getElementById('category-filter');
      const priceFilter = document.getElementById('price-filter');
      const platformFilter = document.getElementById('platform-filter');

      function sanitizeHTML(str) {{
        const temp = document.createElement('div');
        temp.textContent = str;
        return temp.innerHTML;
      }}

      function renderApps(apps) {{
        appList.innerHTML = '';

        if (apps.length === 0) {{
          appList.innerHTML = '<div class="no-results"><h3>No apps found</h3><p>Try adjusting your filters to see more results.</p></div>';
          return;
        }}

        apps.forEach(app => {{
          const prosList = app.pros.map(pro => `<li>${{sanitizeHTML(pro)}}</li>`).join('');
          const consList = app.cons.map(con => `<li>${{sanitizeHTML(con)}}</li>`).join('');
          const platformBadges = app.platforms.map(p => `<span class="badge badge-platform">${{sanitizeHTML(p)}}</span>`).join('');

          const card = document.createElement('article');
          card.className = 'app-card';
          card.innerHTML = `
            <div class="app-header">
              <div class="app-title-group">
                <span class="card-tag">${{sanitizeHTML(app.categoryName)}}</span>
                <h2 class="app-title">${{sanitizeHTML(app.name)}}</h2>
                <div class="app-meta">
                  <span class="badge badge-price">${{sanitizeHTML(app.priceName)}}</span>
                  ${{platformBadges}}
                </div>
              </div>
            </div>

            <div class="app-content">
              <div class="app-main-info">
                <div class="app-review">
                  <h3>Our Review</h3>
                  <p>${{sanitizeHTML(app.review)}}</p>
                </div>
                <div class="app-privacy">
                  <strong>Privacy Assessment:</strong> ${{sanitizeHTML(app.privacy)}}
                </div>
                ${{app.testimonial ? `<blockquote class="app-testimonial">${{sanitizeHTML(app.testimonial)}}</blockquote>` : ''}}
              </div>

              <div class="app-sidebar">
                <div class="app-matrix">
                  <h4>The Good</h4>
                  <ul class="matrix-list pros">
                    ${{prosList}}
                  </ul>
                  <h4 style="margin-top: 1.5rem;">The Drawbacks</h4>
                  <ul class="matrix-list cons">
                    ${{consList}}
                  </ul>
                </div>
              </div>
            </div>
          `;
          appList.appendChild(card);
        }});
      }}

      function filterApps() {{
        const cat = categoryFilter.value;
        const price = priceFilter.value;
        const plat = platformFilter.value;

        const filtered = appData.filter(app => {{
          const matchCat = cat === 'all' || app.categoryId === cat || (cat === 'health-screening' && app.categoryId === 'health-screening');
          const matchPrice = price === 'all' || app.priceId === price;
          const matchPlat = plat === 'all' || app.platformId === plat || app.platformId === 'all';
          return matchCat && matchPrice && matchPlat;
        }});

        renderApps(filtered);
      }}

      categoryFilter.addEventListener('change', filterApps);
      priceFilter.addEventListener('change', filterApps);
      platformFilter.addEventListener('change', filterApps);

      // Initial render
      renderApps(appData);
    }});
  </script>
"""

with open('best-sex-education-apps-2026.html', 'r') as f:
    content = f.read()

# Insert script right before </body>
content = content.replace('</body>', js_logic + '\n</body>')

with open('best-sex-education-apps-2026.html', 'w') as f:
    f.write(content)

print("Injected content and JavaScript logic.")

# Build JSON-LD
schema = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Best Sex Education Apps & Digital Tools 2026",
    "description": "A curated list of the top sexual wellness and education apps, reviewed for privacy, pricing, and features.",
    "itemListElement": []
}

for i, app in enumerate(app_data):
    schema["itemListElement"].append({
        "@type": "ListItem",
        "position": i + 1,
        "item": {
            "@type": "SoftwareApplication",
            "name": app["name"],
            "applicationCategory": app["categoryName"],
            "operatingSystem": ", ".join(app["platforms"]),
            "offers": {
                "@type": "Offer",
                "price": "0" if app["priceId"] == "free" else "Paid",
                "priceCurrency": "USD"
            }
        }
    })

schema_json = json.dumps(schema, indent=2)
schema_script = f'\n  <script type="application/ld+json">\n{schema_json}\n  </script>\n'

with open('best-sex-education-apps-2026.html', 'r') as f:
    content = f.read()

content = content.replace('</head>', schema_script + '</head>')

with open('best-sex-education-apps-2026.html', 'w') as f:
    f.write(content)

print("Injected JSON-LD schema.")
