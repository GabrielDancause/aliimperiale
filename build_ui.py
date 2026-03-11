import re

with open('best-sex-education-apps-2026.html', 'r') as f:
    content = f.read()

# The UI we want to add
ui_html = """
  <main class="main-content">
    <div class="content-container">
      <header class="page-header" style="text-align: center; margin-bottom: 2rem;">
        <span class="card-tag">Curated List & Review</span>
        <h1>Best Sex Education Apps & Digital Tools 2026</h1>
        <p class="intro-text">A comprehensive, continuously updated review of the best sexual wellness and education apps available today. We evaluate privacy, pricing, features, and overall value across multiple categories, including sex education, period tracking, fertility monitoring, and relationship building.</p>
      </header>

      <section class="filter-section">
        <div class="filter-controls">
          <div class="filter-group">
            <label for="category-filter">Category</label>
            <select id="category-filter" class="filter-select">
              <option value="all">All Categories</option>
              <option value="sex-education">Sex Education & Wellness</option>
              <option value="period-tracking">Period Tracking & Fertility</option>
              <option value="relationship">Relationship Building</option>
              <option value="meditation">Meditation & Intimacy</option>
              <option value="kink">Kink Education</option>
              <option value="health-screening">Sexual Health Screening</option>
            </select>
          </div>
          <div class="filter-group">
            <label for="price-filter">Pricing</label>
            <select id="price-filter" class="filter-select">
              <option value="all">Any Price</option>
              <option value="free">Free / Freemium</option>
              <option value="paid">Premium / Subscription</option>
            </select>
          </div>
          <div class="filter-group">
            <label for="platform-filter">Platform</label>
            <select id="platform-filter" class="filter-select">
              <option value="all">All Platforms</option>
              <option value="ios">iOS / Apple</option>
              <option value="android">Android</option>
              <option value="web">Web</option>
            </select>
          </div>
        </div>
      </section>

      <div id="app-list" class="app-list-grid">
        <!-- App cards will be dynamically injected here via JavaScript -->
      </div>
    </div>
  </main>
"""

# The CSS we want to inject into the existing <style> block
css_to_add = """
    /* Page Specific UI Styles */
    h1, h2, h3, h4, h5, h6 {
      font-family: 'Montserrat', sans-serif;
    }

    .main-content {
      padding: 4rem 2rem;
      background: var(--color-bg);
      color: var(--color-text);
      min-height: 80vh;
    }

    .content-container {
      max-width: 1000px;
      margin: 0 auto;
    }

    .page-header h1 {
      font-size: 2.5rem;
      color: var(--color-accent);
      margin: 1rem 0;
    }

    .intro-text {
      font-size: 1.1rem;
      line-height: 1.6;
      max-width: 800px;
      margin: 0 auto;
    }

    .card-tag {
      display: inline-block;
      padding: 0.25rem 0.75rem;
      background: var(--color-accent);
      color: var(--color-bg);
      border-radius: 99px;
      font-size: 0.85rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Filters */
    .filter-section {
      background: #fff;
      padding: 1.5rem;
      border-radius: 12px;
      margin-bottom: 2rem;
      border: 1px solid rgba(46, 62, 36, 0.1);
      box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }

    .filter-controls {
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      justify-content: center;
    }

    .filter-group {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      min-width: 200px;
      flex: 1;
    }

    .filter-group label {
      font-weight: 600;
      font-size: 0.9rem;
      color: var(--color-accent);
    }

    .filter-select {
      padding: 0.75rem 1rem;
      border: 1px solid rgba(46, 62, 36, 0.2);
      border-radius: 8px;
      background: var(--color-bg);
      font-family: 'Montserrat', sans-serif;
      font-size: 1rem;
      color: var(--color-text);
      cursor: pointer;
      appearance: none;
      background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%232E3E24%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E");
      background-repeat: no-repeat;
      background-position: right 1rem top 50%;
      background-size: 0.65rem auto;
      transition: border-color 0.2s;
    }

    .filter-select:focus {
      outline: none;
      border-color: var(--color-accent);
      box-shadow: 0 0 0 2px rgba(173, 152, 70, 0.3);
    }

    /* App Cards */
    .app-list-grid {
      display: grid;
      gap: 2rem;
    }

    .app-card {
      background: #fff;
      border-radius: 12px;
      padding: 2rem;
      border: 1px solid rgba(46, 62, 36, 0.1);
      box-shadow: 0 4px 6px rgba(0,0,0,0.02);
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .app-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 1rem;
      border-bottom: 1px solid rgba(46, 62, 36, 0.1);
      padding-bottom: 1rem;
    }

    .app-title {
      font-size: 1.8rem;
      color: var(--color-accent);
      margin: 0 0 0.5rem 0;
    }

    .app-meta {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .badge {
      font-size: 0.8rem;
      padding: 0.2rem 0.6rem;
      background: rgba(46, 62, 36, 0.05);
      border-radius: 4px;
      color: var(--color-text);
      font-weight: 600;
    }

    .badge-platform {
      background: #e9ecef;
      color: #495057;
    }

    .badge-price {
      background: rgba(173, 152, 70, 0.2);
      color: var(--color-accent);
    }

    .app-content {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 2rem;
    }

    @media (max-width: 768px) {
      .app-content {
        grid-template-columns: 1fr;
      }
    }

    .app-review {
      line-height: 1.6;
    }

    .app-matrix {
      background: var(--color-bg);
      padding: 1.5rem;
      border-radius: 8px;
    }

    .app-matrix h4 {
      margin-top: 0;
      color: var(--color-accent);
      border-bottom: 1px solid rgba(46, 62, 36, 0.1);
      padding-bottom: 0.5rem;
    }

    .matrix-list {
      list-style: none;
      padding: 0;
      margin: 0;
    }

    .matrix-list li {
      margin-bottom: 0.5rem;
      padding-left: 1.5rem;
      position: relative;
      font-size: 0.9rem;
    }

    .matrix-list.pros li::before {
      content: '✓';
      color: green;
      position: absolute;
      left: 0;
      font-weight: bold;
    }

    .matrix-list.cons li::before {
      content: '✗';
      color: red;
      position: absolute;
      left: 0;
      font-weight: bold;
    }

    .app-privacy {
      margin-top: 1rem;
      padding: 1rem;
      background: #f8f9fa;
      border-left: 4px solid var(--color-accent);
      border-radius: 4px;
      font-size: 0.9rem;
    }

    .app-testimonial {
      margin-top: 1.5rem;
      font-style: italic;
      color: #666;
      border-left: 3px solid rgba(173, 152, 70, 0.5);
      padding-left: 1rem;
    }

    .no-results {
      text-align: center;
      padding: 3rem;
      background: #fff;
      border-radius: 12px;
      color: #666;
    }
"""

content = content.replace('<!-- CONTENT_PLACEHOLDER -->', ui_html)
content = content.replace('</style>', css_to_add + '\n  </style>')

with open('best-sex-education-apps-2026.html', 'w') as f:
    f.write(content)

print("Injected UI and Style.")
