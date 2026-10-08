# Navario.id — Website Requirements

| | |
| :-- | :-- |
| **Product** | Navario.id marketing website (previously boffon.com) |
| **Owner** | Navario *(new legal entity, PT Perorangan, to be registered; see [README](../README.md#open-business-decisions))* |
| **Production URL** | https://navario.id |
| **Status** | Target spec for the rebrand, October 2026. Based on the boffon.com implementation; section 0 lists what has to change. |

This document describes what the site must do: its scope, pages, behavior, content model and quality rules. The technical foundations (sections 5, 8–11) are unchanged from the boffon.com site. Content and pages are rewritten for the new positioning: an **AI Business Assistant bundled with an ERP, for Indonesian trading companies**. The [proposal](../proposal/draft_oct_2026/draft_proposal.md) is the source for all product claims and copy.

Requirement IDs use these prefixes: **G** (global), **P** (page), **C** (content), **I** (i18n), **S** (SEO/GEO), **N** (non-functional), **D** (deployment).

---

## 0. Rebrand Checklist (boffon.com → navario.id)

**Brand and domain**
- [ ] `public/CNAME` → `navario.id`. Forward `boffon.com` to `navario.id` (301) at the registrar.
- [ ] New logo and icon (light and dark variants), favicon and `og-image.png`.
- [ ] Replace every "Boffon" string: page title suffix `| Navario`, footer copyright, WhatsApp message template, JSON-LD names.
- [ ] Rename the cookie `boffon-lang` → `navario-lang` and the storage key `boffon-theme` → `navario-theme`.
- [ ] Remove the tagline "Business Offline (to) Online" (it was a Boffon acronym). New tagline: "Ask, don't search." / "Tanya, jangan cari."
- [ ] `package.json` name → `navario.id`. Replace the Astro starter `README.md`.

**Pages**
- [ ] Rewrite Home around the AI assistant (P-2).
- [ ] Add pages: AI Assistant (P-3), Pricing (P-5), Partners (P-6).
- [ ] Keep 5 module pages: Accounting, Buying, Selling, Stock, **Asset Management (new)**.
- [ ] Remove module pages: Finance, Project, Manufacturing.
- [ ] Remove all 4 industry pages and the Industries menu. Home speaks to trading companies directly.
- [ ] Rewrite About (P-7): founder story, no "Trusted By" logos of non-Navario clients.
- [ ] Update the contact form (G-18) and the CTA banner copy (G-13).
- [ ] Update Terms and Privacy for Navario; make the Indonesian version authoritative.

---

## 1. Purpose & Goals

Navario sells an AI Business Assistant bundled with a complete ERP to Indonesian SMEs, starting with trading companies. The website exists to:

1. **Show the AI assistant working** through demo videos and examples, because the live demo is the main sales tool.
2. **Explain what's included:** the ERP modules (Accounting, Buying, Selling, Stock, Asset Management) and the Indonesian localization.
3. **Show fixed, public prices** for retail packages.
4. **Build trust** for a new company: founder background, safety and access rules, data ownership and, once available, client case studies.
5. **Generate leads** by moving visitors into a WhatsApp conversation, mainly to book a live demo.
6. **Recruit partners** (accountants, consultants, IT firms).
7. **Win organic and AI-engine discovery** through bilingual SEO, structured data, and blog content that AI crawlers can read and cite.

### Key value propositions shown on the site
From the proposal:
- Ask in plain Bahasa Indonesia or English, answered from the company's own live data.
- One system for accounting, buying, selling, stock and assets.
- Safe by design: same access rights as the ERP, never changes data on its own, every request logged, data not used to train AI.
- Built for Indonesian companies: Bahasa Indonesia, PPN and PPh, Indonesian chart of accounts, local documents.
- Fixed, public prices; enterprise plans with unlimited users; no vendor lock-in.

## 2. Audience

| Audience | Needs |
| :-- | :-- |
| Owners and directors of Indonesian trading SMEs | Understand what the assistant does, see prices, book a demo |
| Finance, purchasing and sales managers | Check that the modules cover their daily work and reports |
| Partners (accountants, tax consultants, IT/ERP consultants) | Understand the partner model and get in touch |
| Indonesian-speaking visitors (primary) | Full Bahasa Indonesia experience; this is the default locale |
| English-speaking visitors | Full English experience |
| Search engines and AI crawlers (Googlebot, GPTBot, ClaudeBot, PerplexityBot, Google-Extended) | Server-rendered, structured, indexable content |

## 3. Scope

**In scope:** static marketing pages, AI assistant page, product (module) pages, a pricing page, a partner page, a blog, legal pages, a contact-to-WhatsApp lead form, language and theme switching, analytics, and SEO/GEO metadata.

**Out of scope:** user accounts, a server-side backend, a CMS UI, online payment, a self-service sign-up or trial, and server-side form storage (leads go straight to WhatsApp).

---

## 4. Information Architecture

### 4.1 Sitemap

Indonesian (`id`) is the default locale. URL slugs are localized and do **not** map 1:1 between locales.

| Page | English URL | Indonesian URL |
| :-- | :-- | :-- |
| Root (language redirect) | `/` | `/` |
| Home | `/en/` | `/id/` |
| AI Assistant | `/en/ai-assistant` | `/id/asisten-ai` |
| Pricing | `/en/pricing` | `/id/harga` |
| Partners | `/en/partners` | `/id/mitra` |
| About | `/en/about` | `/id/tentang-kami` |
| Blog index | `/en/blogs` | `/id/blog` |
| Blog post | `/en/blogs/{slug}` | `/id/blog/{slug}` |
| Terms of Service | `/en/terms-of-service` | `/id/ketentuan-layanan` |
| Privacy Policy | `/en/privacy-policy` | `/id/kebijakan-privasi` |
| **Products** | | |
| Accounting | `/en/product/accounting` | `/id/produk/akuntansi` |
| Buying | `/en/product/buying` | `/id/produk/pembelian` |
| Selling | `/en/product/selling` | `/id/produk/penjualan` |
| Stock | `/en/product/stock` | `/id/produk/persediaan` |
| Asset Management | `/en/product/asset-management` | `/id/produk/manajemen-aset` |
| Not found | any unmatched path → `404.html` | same |
| Sitemap | `/sitemap-index.xml` | same |

### 4.2 Primary navigation

Home · AI Assistant · Products ▾ (5 modules) · Pricing · Partners · Blog · About Us · [Language] [Theme] [Book a demo]

---

## 5. Global Requirements (every page)

### 5.1 Header
- **G-1** The header is sticky at the top, with a translucent, blurred surface background.
- **G-2** The left side shows the Navario icon linking to the current locale's home page. Light and dark variants of the icon swap with the theme.
- **G-3** At the desktop breakpoint (≥ 950 px), the navigation is inline. *Products* opens a dropdown on hover or keyboard focus. Each item has an icon and a localized label.
- **G-4** Below 950 px, a hamburger button (which animates into an ✕) opens a vertical menu. *Products* expands as a collapsible sub-list inside it. The menu itself opens and closes without JavaScript (checkbox/CSS). Small scripts close the menu when the viewport grows to desktop width, and collapse the sub-list when the menu closes.
- **G-5** The header utilities are: Language picker, Theme picker, and a **"Book a demo"** button that opens the contact form modal. Its accessible name says "Book a demo", not "WhatsApp".
- **G-6** Only one of the Language and Theme pickers can be open at a time. Clicking outside closes them.

### 5.2 Language picker
- **G-7** Shows the current locale code (`EN` / `ID`). The dropdown lists "English" and "Bahasa Indonesia" and marks the active one with a check.
- **G-8** Each option links to the **equivalent page** in the other locale, using the page's alternate-language mapping.
- **G-9** Choosing a language sets the cookie `navario-lang=<en|id>` (path `/`, 1 year, `SameSite=Lax`).

### 5.3 Theme picker
- **G-10** Options: Light, Dark, System (default). The trigger icon shows the current choice. Labels are localized.
- **G-11** The choice is saved in `localStorage` under the key `navario-theme`. *System* follows `prefers-color-scheme` and updates live when the OS setting changes.
- **G-12** A blocking inline script in `<head>` applies the `.dark` class before first paint, so the page never flashes the wrong theme.

### 5.4 CTA banner (every page except root, 404 and Partners)
- **G-13** A full-width primary-color band appears above the footer. It holds the headline "See it answer your business questions." and a "Book a live demo" button that opens the contact modal.

### 5.5 Footer
- **G-14** Navario logo (light/dark variants), the tagline "Ask, don't search.", and links to AI Assistant, Pricing, Partners, About and Blog.
- **G-15** A column of the 5 product modules.
- **G-16** Bottom line: © {current year} Navario. All rights reserved. — Sitemap — Terms of Service — Privacy Policy.

### 5.6 Contact form modal (lead capture)
- **G-17** A native `<dialog>` modal, opened by any element marked `data-open-contact-form` (header button, CTA banner, pricing and partner buttons). An opener can preselect the topic, e.g. `data-open-contact-form="partner"`.
- **G-18** Fields:

  | Field | Type | Required |
  | :-- | :-- | :-- |
  | Name | text | Yes |
  | Company Name | text | Yes |
  | Phone (WhatsApp) | tel | Yes |
  | Company Email | email | No |
  | I want to | single select: Book a live demo (default) / Ask about pricing / Become a partner | Yes |
  | Number of staff | single select: 1–10 / 11–30 / 31–100 / 100+ | No |

- **G-19** On submit, the browser validates the form. If valid, the site builds a message from the localized template, e.g. *"Hello Navario team, I'm {name} from {company}. I want to: {topic}. Staff: {size}. Phone: {phone} Email: {email}"*. Empty optional values become `-`. The site then opens `https://wa.me/6281289895088?text=<encoded message>` in a new tab, closes the modal and resets the form.
- **G-20** The modal closes with the ✕ button, Esc, or a click on the backdrop.
- **G-21** No form data is sent to or stored on any Navario server.

### 5.7 Analytics
- **G-22** Google Analytics 4 loads **only in production builds**, on every page including 404. Use a new GA4 property for navario.id, or rename the existing `G-STL3VMW19E`.
- **G-23** Tracked custom events (category `engagement`):
  - `demo_click`: header "Book a demo" button clicked.
  - `contact_us_click`: CTA banner button clicked.
  - `pricing_cta_click`: a package button on the pricing page clicked.
  - `partner_cta_click`: the partner page button clicked.
  - `demo_video_play`: a demo video started.
  - `whatsapp_message_sent`: contact form submitted, with the topic as a parameter.

---

## 6. Page Requirements

### P-1 Root `/`
- Static page, marked `noindex`, with its canonical URL set to `/id/`.
- A client-side script reads the `navario-lang` cookie and redirects to `/en/` or `/id/`. With no cookie it uses `/id/`.
- Without JavaScript, a `<noscript>` meta refresh sends the visitor to `/id/`, and a visible fallback link is shown.
- **Constraint:** Astro's built-in `redirectToDefaultLocale` must stay **off**. Hosting is fully static, so the cookie can only be read client-side.

### P-2 Home (`/en/`, `/id/`)
Sections, in order (copy adapted from the proposal):
1. **Hero:** H1 "Ask, Don't Search: An AI Business Assistant, Business System Included." Subheadline: "Your team asks in plain Bahasa Indonesia or English and gets answers from your own business data." Buttons: *Book a live demo* and *Watch the 3-min demo*.
2. **Demo video:** the 3-minute demo in Bahasa Indonesia (English subtitles), loaded lazily on click (poster image first). A text transcript sits below it for crawlers and accessibility.
3. **"Your team asks / The assistant answers":** the 6-row example table from proposal section 2.
4. **The problem:** the two problem lists from proposal section 1 (spreadsheets / hard-to-use software), framed for trading companies.
5. **Safe by design:** the 5 safety points from the proposal.
6. **One system for the whole business:** cards linking to the 5 module pages, plus the Indonesian localization points.
7. **Pricing teaser:** starting monthly price and a link to Pricing.

The home page is the only page allowed to use full-width bands. All other pages follow the single-container layout rule (N-10).

### P-3 AI Assistant (`/en/ai-assistant`, `/id/asisten-ai`)
- Breadcrumb, H1 "AI Business Assistant".
- Content from proposal sections 3, 5 and 6: how it works (5 steps), the agentic workflow diagram (server-rendered SVG or HTML, not an image of text), the capability table, and the chat features.
- 3–5 short demo clips, one per capability, each with a caption and transcript.
- An FAQ block with `FAQPage` JSON-LD. Questions to cover: Is my data used to train AI? Can staff see data they shouldn't? Can it change data by itself? Which languages? What is an "AI question" and how many do we get?

### P-4 Product / module pages (×5)
All five are built from one shared template. Each page has:
- **Breadcrumb:** Home › Products › {Module}.
- **Hero:** module icon, H1 module title, one-line subtitle.
- **"Ask the assistant" box:** 2–3 example questions for this module with the kind of answer the user gets (from the proposal's capability table).
- **Screenshot stack** (only when screenshots exist): an animated, cross-fading stack of product screenshots with two static "backing cards" behind it and a faint brand watermark. Screenshots must show the **current Navario UI in Bahasa Indonesia**, not stock ERPNext screens.
  - Images are loaded from `src/assets/products/{folder}/`, sorted by filename. A file `N_name_dark.png` pairs with `N_name.png` and is shown in dark mode.
  - The first image loads eagerly with high priority. The rest load lazily. Responsive widths are 400/600/800/1200.
  - Every image has a localized caption as its alt text.
  - With reduced motion, only the first image is shown, statically.
- **Standard workflow:** a vertical diagram of step boxes joined by arrows, rendered on the server with zero client JavaScript.
- **Key Operations & Activities** list and **Core Reports & Insights** list. Each list shows the first 5 items, and a "Load more" toggle reveals the rest.

| Module | Subtitle | Workflow steps | Screenshots |
| :-- | :-- | :-- | :-- |
| Accounting | Financial clarity for every transaction. | Journal Entry → Payment Entry → Bank Reconciliation → Period Closing Voucher → Financial Statements → Audit Trail & Ledger Report | Retake in Navario UI |
| Buying (Procurement) | Full visibility for every purchase order. | Material Request → Supplier Quotation → Purchase Order → Purchase Receipt → Purchase Invoice → Payment Entry | Retake in Navario UI |
| Selling (Sales) | From quotation to cash, in one flow. | Quotation → Sales Order → Delivery Note → Sales Invoice → Payment Entry | Retake in Navario UI |
| Stock (Inventory) | No more stockouts or overstocking. | Purchase Receipt → Stock Transfer → Delivery Note → Stock Reconciliation → Stock Reports | Retake in Navario UI |
| Asset Management | Know what you own, where it is and what it's worth. | Asset Purchase → Asset Registration → Location & Custodian → Depreciation Schedule → Maintenance → Disposal | New |

Workflows should only show steps the trading template actually uses (Lead/Opportunity, RFQ and Batch/Serial tracking were removed for that reason; add them back if they are part of the demo). The full operations and reports lists for each module live in `siteContent.json`.

### P-5 Pricing (`/en/pricing`, `/id/harga`)
- Breadcrumb, H1 "Pricing", one-line intro: "Fixed prices. Hosting, AI and support included."
- A **Retail** card: price per user per month (minimum 3 users), annual discount, AI questions per user, and the two setup options (Fast-Track, Standard) with what each includes. The numbers come from [pricing_model.md](../pricing_model/pricing_model.md) and are stored in `siteContent.json`, not hardcoded.
- An **Enterprise** card: "Unlimited users, dedicated server, delivered with our implementation partners." Show "from IDR 12.5M / month" or no price (decide). Button: *Talk to us*.
- Add-ons summary (AI top-ups, data migration, training). Customization is shown as "quoted at a fixed price after review".
- A note that prices exclude PPN.
- FAQ with `FAQPage` JSON-LD: What is an AI question? What happens when we run out? Can we add users later? How do we compare with Odoo? Can we export our data?
- Each package button opens the contact modal with the topic "Ask about pricing" preselected.

### P-6 Partners (`/en/partners`, `/id/mitra`)
- Breadcrumb, H1 "Partner with Navario".
- Who it's for: accountants, tax consultants, business consultants, IT/ERP consulting firms.
- The two partner types and what each earns, in plain terms. Commission rates are shown; internal rules stay in [partnership_model.md](../partnership_model/partnership_model.md).
- What Navario provides to partners (demo instance, training, proposal).
- Button opens the contact modal with the topic "Become a partner" preselected. No CTA banner on this page.

### P-7 About
- Breadcrumb, then H1 "About Us".
- Rows, each with an icon or statistic on the left and copy on the right:
  1. **Mission:** "Your team should spend its time running the business, not searching for information."
  2. **15+** "15+ years building software", the founder's background and why Navario exists.
  3. **Built on open source:** a mature open-source ERP platform, improved for Indonesian companies; no vendor lock-in.
  4. **Clients:** hidden until there are Navario client case studies. Do not reuse the boffon.com "Trusted By" logos unless each company is a Navario client and has given permission.
- **Headquarters & Location:** the legal name and registered address of the new entity, and a lazy-loaded Google Maps embed. Until the entity is registered, show only the city and the WhatsApp contact.

### P-8 Blog index
- Breadcrumb. On large screens, a two-column layout: a left column with H1 "Business & AI Insights" and the subtitle, and a right column with post cards.
- Shows only posts in the current locale, newest first.
- Each card shows: date (formatted for the locale) · author · "N min read", then the title, description and tag pills. The whole card is a link.

### P-9 Blog post
- **Breadcrumb:** Home › Blog › {Post title}.
- **Header:** date · author · reading time, then H1 title, then tags.
- **Body:** Markdown rendered with typography styles. Every H2–H6 heading wraps itself in a self-link anchor that shows a link icon on hover.
- **Table of contents:** a collapsible box (open by default) listing the H2 headings. It is sticky in a right sidebar on large screens and sits above the content on small screens. It is hidden when the post has no H2.
- **Footer links:** "← Back to Blog", plus "Next Article →" pointing to the next **older** post in the same locale (none on the oldest post).
- **Reading time:** word count ÷ 200, rounded, minimum 1 minute.
- The language picker links to the translated version of the same post (see C-6).

### P-10 Terms of Service / Privacy Policy
- Breadcrumb, H1 title, and a "Last updated" line.
- An intro paragraph followed by numbered sections, rendered as H2 plus paragraphs in typography styles.
- **The Indonesian version is authoritative**; the English version states that it is a translation.
- **Terms**, 10 sections: Acceptance, Services, Use of Website, Intellectual Property, Fees & Payment, Confidentiality & Data Protection, Limitation of Liability, Changes, Governing Law (Republic of Indonesia), Contact.
- **Privacy**, 9 sections: Information Collected, Use, Cookies & Analytics (language cookie and Google Analytics), Third-Party Services (WhatsApp/Meta, hosting, and similar), Retention, Security, Your Rights (UU PDP No. 27/2022), Changes, Contact.
- These pages cover the website only. Client data inside the product (including AI processing) is covered by the service agreement.

### P-11 404
- A single top-level `404.html`, because GitHub Pages serves only the root 404 file. It is `noindex`.
- A centered card with a large "404", a title, a short message, and two buttons: *Back to homepage* and *Visit our blog*.
- Both language versions are in the HTML. A script shows the English version when the requested path starts with `/en`. Otherwise, or without JavaScript, the Indonesian version is shown. The language picker label matches the version shown.
- The header and footer render in the default locale (Indonesian). The CTA banner is not shown.

---

## 7. Content Requirements

- **C-1 All copy lives in data.** Every user-facing string is a `LocalizedText` `{ en, id }` entry in `src/data/siteContent.json`, read through `src/lib/content.ts`. Components must not hardcode copy. This includes accessible labels, control labels, theme option names and "Load more".
- **C-2 SEO copy.** Every content block has `seo: { title, description }`. Every page title, including blog posts, uses the suffix `| Navario`.
- **C-3 Module registry.** Adding a module requires:
  - an entry in `routes.ts → modules`
  - an entry in `src/lib/modules.ts` (icon and content key)
  - a content block in `siteContent.json` (`nav`, `seo`, `hero`, `askExamples`, `workflow`, `operations`, `reports`, and optionally `screenshots`)
  - a page file per locale

  Modules then appear automatically in the header, footer, home page and contact form.
- **C-4 Claims follow the proposal.** Product claims must match the [proposal](../proposal/draft_oct_2026/draft_proposal.md). Don't advertise features the demo can't show (for example e-Faktur export or e-Meterai) until they ship.
- **C-5 Blog post files.** Posts are Markdown files in `src/content/blog/`, named `YYYYMMDD-SS-slug-name.md`. Frontmatter is validated by schema:

  | Field | Type |
  | :-- | :-- |
  | `title` | string |
  | `publishDate` | date |
  | `description` | string |
  | `lang` | `en` \| `id` |
  | `tags` | string[] |
  | `author` | string |

  The URL slug is the part of the filename after the `YYYYMMDD-SS-` prefix.
- **C-6 Blog translations.** Translation pairs share the same `YYYYMMDD-SS` prefix and must have different `lang` values. A filename that breaks the pattern, or a duplicate language in a pair, **fails the build**.
- **C-7 Blog writing style.** Blog posts should favor content that is easy to extract (direct definitions, bulleted lists, comparison tables) and link to related posts. Topics should serve trading SMEs and the AI assistant. Existing posts (*What is ERP?*, *The Benefits of ERP Across Business Aspects*, *ERP for SMEs*) stay; add a closing link to the AI Assistant page. Suggested next posts:
  - *AI for trading companies: what it can and can't do*
  - *How to track overdue receivables without spreadsheets*
  - *Is business data safe with an AI assistant?*

## 8. Internationalization

- **I-1** Two locales: `id` (default) and `en`. Every route has a locale prefix (`/id/…`, `/en/…`).
- **I-2** Every page pair is registered as `{ en, id }` in `src/lib/routes.ts`. Pages without an entry cannot emit correct canonical and hreflang links.
- **I-3** `<html lang>` matches the page locale. Dates are formatted with `id-ID` or `en-US`. Prices are formatted as `IDR 1.600.000` (`id`) and `IDR 1,600,000` (`en`).
- **I-4** The visitor's language choice is remembered via the `navario-lang` cookie and applied at `/` (see P-1).
- **I-5** Every page must be fully available in both languages. Blog posts are the exception: they may exist in one language only, and the language picker then lists only the languages that exist.

## 9. SEO & GEO (Generative Engine Optimization)

- **S-1** Each page has exactly one `<h1>`, and heading levels never skip.
- **S-2** `BaseLayout` emits, from content data, the following tags. Pages must never hardcode them.
  - `<title>`, meta description, `author`, `robots: index, follow`
  - canonical URL
  - `hreflang` alternates for `en` and `id`, plus `x-default` pointing to the Indonesian page
  - OpenGraph tags: type, site_name (`Navario`), title, description, url, 1200×630 `og-image.png`, locale `id_ID`/`en_US` plus the alternate locale
  - Twitter `summary_large_image` card
- **S-3** Structured data (JSON-LD):
  - Every page includes an `Organization` block (name Navario, URL, logo, `areaServed: ID`).
  - Home, AI Assistant and Pricing include a `SoftwareApplication` block (`applicationCategory: BusinessApplication`, `operatingSystem: Web`, `offers` with the retail per-user price in IDR).
  - AI Assistant and Pricing include `FAQPage`.
  - Every non-home page includes a `BreadcrumbList` that matches its visible breadcrumb.
  - Blog posts include a `BlogPosting` block (headline, description, datePublished, inLanguage, keywords, author as a Person, publisher as an Organization, mainEntityOfPage).
- **S-4** Content that crawlers need must be server-rendered. AI crawlers usually don't run JavaScript, so diagrams, workflows, lists and video transcripts must exist in the static HTML.
- **S-5** `robots.txt` allows `*` and explicitly allows GPTBot, ClaudeBot, PerplexityBot and Google-Extended. It also points to `sitemap-index.xml`.
- **S-6** An XML sitemap is generated automatically for every page and linked from the footer.
- **S-7** The root redirect page and the 404 page are `noindex`.

## 10. Non-Functional Requirements

### Performance
- **N-1** The site is fully static, with no runtime server.
- **N-2** All CSS is inlined into `<head>` (`inlineStylesheets: 'always'`) to avoid render-blocking stylesheet requests.
- **N-3** Images are optimized through Astro's asset pipeline, with responsive `srcset`, lazy loading below the fold, and an eager, high-priority first screenshot. Maps, videos and other embeds load lazily; videos load only after a click on the poster.
- **N-4** Fonts are self-hosted via `@fontsource`: Alegreya 500–800 for headings and Outfit 400–700 for body text. No third-party font requests.
- **N-5** Client JavaScript is kept small and limited to progressive enhancement: theme, language cookie, menu helpers, slider, modal, video loader and analytics.

### Accessibility
- **N-6** Semantic landmarks are used: `header`, `nav` with `aria-label`, `main`, `footer`, `nav[aria-label=Breadcrumb]`, and `aria-current` on the active breadcrumb item and active language.
- **N-7** All animations respect `prefers-reduced-motion`. That covers the screenshot stack and any demo animations. Videos never autoplay.
- **N-8** Interactive controls are keyboard-reachable and show visible focus outlines. Icon-only buttons have localized `aria-label`s. Decorative icons are `aria-hidden`.
- **N-9** Text colors meet WCAG AA (4.5:1) contrast in both themes. Re-check if the brand colors change with the new logo.

### Design system
- **N-10** Page layout: every page except home wraps its breadcrumb and content in one container, `mx-auto max-w-6xl px-4 py-8 sm:px-6 lg:px-8`, matching the footer and CTA banner.
- **N-11** Colors come only from semantic tokens in `global.css`: primary, secondary, bg-app, bg-surface (with elevated, hover and invert variants), text-primary, text-secondary, text-on-primary, border-subtle/strong, and status colors.
  - Current light theme: blue `#2D68C4` on slate/white. Current dark theme: teal `#3b7e80` on slate-950/900. Update both tokens if the Navario brand uses different colors.
  - Dark mode works by switching the tokens under `.dark`, not by adding `dark:` utility pairs.
- **N-12** Typography roles: `text-h1-hero`, `h1`, `h2`, `h3` and `card-title`, which scale up at larger breakpoints.
- **N-13** Radius roles: full for pills and icon buttons, 2xl for panels, xl for popovers, lg for list items.
- **N-14** Shadow roles: sm at rest, md on hover, lg for overlays.
- **N-15** Responsive breakpoints: Tailwind defaults, plus a custom `nav` breakpoint at 950 px for the header.

### Privacy
- **N-16** The site uses one functional cookie (language), `localStorage` for the theme, and Google Analytics in production only. Contact data goes only to WhatsApp, as disclosed in the Privacy Policy.

### Code quality
- **N-17** TypeScript strict mode. `astro check` must pass.
- **N-18** Node ≥ 22.12.0.

## 11. Deployment & Operations

- **D-1** Hosting is GitHub Pages on the custom domain `navario.id` (configured in `public/CNAME`). `boffon.com` is forwarded to `navario.id` with a 301 at the domain registrar.
- **D-2** Every push to `main`, or a manual dispatch, runs `.github/workflows/deploy.yml` (`withastro/action@v4` then `actions/deploy-pages@v4`) and deploys to production. **There is no staging environment**, so preview the rebrand locally (`astro build && astro preview`) before pushing.
- **D-3** The build fails on blog naming or schema violations (C-5, C-6), so a broken post cannot reach production.

---

## 12. Known Issues Carried Over from boffon.com

These were found while reverse-engineering the old site. Fix them as part of the rebrand.

| # | Issue | Related rule |
| :-- | :-- | :-- |
| 1 | The "Load more / Muat lebih banyak" label in `ModuleList.astro` and the theme option labels (Light/Dark/System) are hardcoded. The theme labels are English-only. | C-1, G-10 |
| 2 | `TypewriterHeadline.astro` exists but no page uses it. The content keys `product.*`, `blog.readMore` and `blog.publishedOn` are also unused. Delete them, along with the ERP journey diagram and industry components the new site no longer uses. | — |
| 3 | Blog post `<title>` tags use the bare post title, without the site suffix. | C-2 |
| 4 | On the 404 page, the language picker label falls back to `EN` even though the page renders in Indonesian, and the page doesn't load analytics. | P-11, G-22 |
| 5 | The header contact button is labeled and styled as "WhatsApp" but opens the contact form. | G-5 |
| 6 | "Next Article" links to the next **newer** post; the new spec links to the next older post. | P-9 |
