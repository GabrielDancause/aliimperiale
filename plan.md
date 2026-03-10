1.  **Create the interactive tool HTML file**: Create a new file called `desire-compatibility-calculator.html` in the root directory.
    -   It should follow the standard interactive tool layout, including the nav from `index.html` and `shared.css`.
    -   It should include the `consent.js` script and Google Analytics tag (`G-G86C7NJG3F`).
    -   Include SEO meta tags, Open Graph, canonical URL `https://aliimperiale.com/desire-compatibility-calculator.html`, and an FAQPage JSON-LD schema.
    -   The tool should have 25-30 questions about sexual compatibility, communication, libidos, etc.
    -   It should provide detailed results with percentage scores, personalized recommendations, and resources.
    -   It should use `localStorage` for client-side persistence.
    -   It should have a mobile-first responsive design using the specified color palette and fonts.
    -   It should be styled using inline CSS and use vanilla JavaScript for the logic.
    -   It should have an FAQ section with 5 questions corresponding to the JSON-LD schema.
    -   It should use the voice of Ali Imperiale.
2.  **Verify the new file**: Read the contents of `desire-compatibility-calculator.html` using the `read_file` tool to verify the contents and structure.
3.  **Update `sitemap.xml`**: Append the new URL `https://aliimperiale.com/desire-compatibility-calculator.html` to `sitemap.xml`.
4.  **Verify `sitemap.xml` update**: Read the last few lines of `sitemap.xml` using `run_in_bash_session` to verify the new URL is included correctly.
5.  **Update `tools.html`**: Add a new link to the calculator in `tools.html` within the `.category-grid`.
6.  **Verify `tools.html` update**: Read the contents of `tools.html` to verify the link was added correctly.
7.  **Test the tool with Playwright**: Create a local Python HTTP server and write a Playwright script to visually verify the functionality and take a screenshot.
8.  **Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.**
9.  **Submit the code**: Submit the changes with an appropriate commit message.
