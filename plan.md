1. **Create the Guide File:** Create `sensual-touch-exploration-guide.html` in the root directory.
   - Include the standard head block, Montserrat font, and link to `shared.css`.
   - Add `<style>` block for internal styling (including the `body { background-color: #FAF8EB; }` rule, plus the specific `.site-nav` rules from `site_nav_css.txt` and the guide's specific layout CSS).
   - Implement the `nav` and `footer` matching the rest of the site (without `header` wrappers for the nav).
   - Write the content covering all requested topics: Progressive touch exercises, mindfulness techniques, communication, different types of touch, building anticipation, creating sensual environments, addressing trauma, and partner synchronization.
   - Include a comprehensive FAQ section with JSON-LD schema for SEO.
   - Include tracking and UI scripts (`consent.js`, Google Analytics, `mobile-nav.js`, `newsletter-bar.js`, `email-capture.js`, `back-to-top.js`).
2. **Update Navigation/Directories:** Add a link to the new guide in `guides.html` using a `.category-card` element.
3. **Update Sitemap:** Add the new URL to `sitemap.xml` safely.
4. **Test the new page:** Write a Playwright script `test_page.py` to verify the page loads, has no console errors (filtering external scripts), and generates a screenshot. Use `frontend_verification_complete`.
5. **Run tests:** Run any project tests (e.g. `pytest`) to ensure no regressions.
6. **Clean up:** Remove the temporary script `test_page.py`, `site_nav_css.txt`, and `site_nav_styles.txt`.
7. **Pre-commit:** Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
