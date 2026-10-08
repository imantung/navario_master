# Boffon.com — Website Requirements

| | |
| :-- | :-- |
| **Product** | Boffon.com marketing website |
| **Owner** | PT Inovasi Teknologi Terintegrasi ("Boffon") |
| **Production URL** | https://boffon.com |
| **Status** | Reverse-engineered from the implemented site, October 2026 |

This document describes what the current site does: its scope, pages, behaviour, content model and quality rules. It was written by reading the code, so it records how the site works today, not a future plan. Section 12 lists gaps and inconsistencies found while reading the code.

Requirement IDs use these prefixes: **G** (global), **P** (page), **C** (content), **I** (i18n), **S** (SEO/GEO), **N** (non-functional), **D** (deployment).

---

## 1. Purpose & Goals

Boffon sells tailored ERP implementation, customization, integration and consulting services to Indonesian organizations of all sizes. The website exists to:

1. **Explain ERP and its value** to business owners who still run on spreadsheets and disconnected tools.
2. **Present the product** as seven ERP modules, each with its workflow, operations, reports and screenshots.
3. **Speak to target industries** (trading, manufacturing, financial services, professional services) with challenges and solutions specific to each.
4. **Build credibility** with company background, 14+ years of experience, client logos and a physical address.
5. **Generate leads** by moving visitors into a WhatsApp conversation with a pre-filled inquiry.
6. **Win organic and AI-engine discovery** through bilingual SEO, structured data, and blog content that AI crawlers can read and cite.

### Key value propositions shown on the site
- Tailored, highly customizable ERP that fits each company's processes.
- No vendor lock-in and no per-user license fees.
- Cloud-hosted or self-hosted deployment.
- 100% data ownership.
- API integration with external software.

## 2. Audience

| Audience | Needs |
| :-- | :-- |
| Owners and directors of Indonesian SMEs and enterprises | Understand ERP, see relevance to their industry, contact sales |
| Operations, finance and procurement managers | Check module capabilities, workflows and reports |
| Indonesian-speaking visitors (primary) | Full Bahasa Indonesia experience; this is the default locale |
| English-speaking visitors | Full English experience |
| Search engines and AI crawlers (Googlebot, GPTBot, ClaudeBot, PerplexityBot, Google-Extended) | Server-rendered, structured, indexable content |

## 3. Scope

**In scope:** static marketing pages, product (module) pages, industry pages, a blog, legal pages, a contact-to-WhatsApp lead form, language and theme switching, analytics, and SEO/GEO metadata.

**Out of scope:** user accounts, a server-side backend, a CMS UI, e-commerce or pricing pages, and server-side form storage (leads go straight to WhatsApp).

---

## 4. Information Architecture

### 4.1 Sitemap

Indonesian (`id`) is the default locale. URL slugs are localized and do **not** map 1:1 between locales.

| Page | English URL | Indonesian URL |
| :-- | :-- | :-- |
| Root (language redirect) | `/` | `/` |
| Home | `/en/` | `/id/` |
| About | `/en/about` | `/id/tentang-kami` |
| Blog index | `/en/blogs` | `/id/blog` |
| Blog post | `/en/blogs/{slug}` | `/id/blog/{slug}` |
| Terms of Service | `/en/terms-of-service` | `/id/ketentuan-layanan` |
| Privacy Policy | `/en/privacy-policy` | `/id/kebijakan-privasi` |
| **Products** | | |
| Accounting | `/en/product/accounting` | `/id/produk/akuntansi` |
| Finance | `/en/product/finance` | `/id/produk/keuangan` |
| Buying | `/en/product/buying` | `/id/produk/pembelian` |
| Selling | `/en/product/selling` | `/id/produk/penjualan` |
| Stock | `/en/product/stock` | `/id/produk/persediaan` |
| Project | `/en/product/project` | `/id/produk/proyek` |
| Manufacturing | `/en/product/manufacturing` | `/id/produk/manufaktur` |
| **Industries** | | |
| Wholesale, Trading & Retail | `/en/industries/wholesale-trading-retail` | `/id/industri/grosir-perdagangan-ritel` |
| Manufacturing | `/en/industries/manufacturing` | `/id/industri/manufaktur` |
| Financial Services | `/en/industries/financial-services` | `/id/industri/jasa-keuangan` |
| Professional & Business Services | `/en/industries/professional-business-services` | `/id/industri/layanan-profesional-bisnis` |
| Not found | any unmatched path → `404.html` | same |
| Sitemap | `/sitemap-index.xml` | same |

### 4.2 Primary navigation

Home · Products ▾ (7 modules) · Industries ▾ (4 industries) · Blogs · About Us · [Language] [Theme] [Contact]

---

## 5. Global Requirements (every page)

### 5.1 Header
- **G-1** The header is sticky at the top, with a translucent, blurred surface background.
- **G-2** The left side shows the brand icon linking to the current locale's home page. Light and dark variants of the icon swap with the theme.
- **G-3** At the desktop breakpoint (≥ 950 px), the navigation is inline. *Products* and *Industries* open dropdowns on hover or keyboard focus. Each item has an icon and a localized label.
- **G-4** Below 950 px, a hamburger button (which animates into an ✕) opens a vertical menu. *Products* and *Industries* expand as collapsible sub-lists inside it. The menu itself opens and closes without JavaScript (checkbox/CSS). Small scripts close the menu when the viewport grows to desktop width, and collapse the sub-lists when the menu closes.
- **G-5** The header utilities are: Language picker, Theme picker, and a round WhatsApp-icon button that **opens the contact form modal** (it does not link to WhatsApp directly).
- **G-6** Only one of the Language and Theme pickers can be open at a time. Clicking outside closes them.

### 5.2 Language picker
- **G-7** Shows the current locale code (`EN` / `ID`). The dropdown lists "English" and "Bahasa Indonesia" and marks the active one with a check.
- **G-8** Each option links to the **equivalent page** in the other locale, using the page's alternate-language mapping.
- **G-9** Choosing a language sets the cookie `boffon-lang=<en|id>` (path `/`, 1 year, `SameSite=Lax`).

### 5.3 Theme picker
- **G-10** Options: Light, Dark, System (default). The trigger icon shows the current choice.
- **G-11** The choice is saved in `localStorage` under the key `boffon-theme`. *System* follows `prefers-color-scheme` and updates live when the OS setting changes.
- **G-12** A blocking inline script in `<head>` applies the `.dark` class before first paint, so the page never flashes the wrong theme.

### 5.4 CTA banner (every page except root and 404)
- **G-13** A full-width primary-color band appears above the footer. It holds the headline "Ready to optimize your business operations?" and a "Get in touch" button that opens the contact modal.

### 5.5 Footer
- **G-14** Brand logo (light/dark variants), the tagline "Business Offline (to) Online", and links to About and Blog.
- **G-15** Column of all 7 product modules and a column of all 4 industries.
- **G-16** Bottom line: © {current year} Boffon.com. All rights reserved. — Sitemap — Terms of Service — Privacy Policy.

### 5.6 Contact form modal (lead capture)
- **G-17** A native `<dialog>` modal, opened by any element marked `data-open-contact-form` (header button, CTA banner).
- **G-18** Fields:

  | Field | Type | Required |
  | :-- | :-- | :-- |
  | Name | text | Yes |
  | Company Name | text | Yes |
  | Company Email | email | Yes |
  | Phone | tel | No |
  | Interested in | multi-select checkboxes, one per module (7) | No |

- **G-19** On submit, the browser validates the form. If valid, the site builds a message from the localized template, e.g. *"Hello Boffon team, I'm {name} from {company}. Company email: {email} Phone: {phone} I'm interested in: {modules}"*. Empty optional values become `-`. The site then opens `https://wa.me/6281289895088?text=<encoded message>` in a new tab, closes the modal and resets the form.
- **G-20** The modal closes with the ✕ button, Esc, or a click on the backdrop.
- **G-21** No form data is sent to or stored on any Boffon server.

### 5.7 Analytics
- **G-22** Google Analytics 4 (`G-STL3VMW19E`) loads **only in production builds**.
- **G-23** Tracked custom events (category `engagement`):
  - `whatsapp_click`: header contact button clicked.
  - `contact_us_click`: CTA banner button clicked.
  - `whatsapp_message_sent`: contact form submitted.

---

## 6. Page Requirements

### P-1 Root `/`
- Static page, marked `noindex`, with its canonical URL set to `/id/`.
- A client-side script reads the `boffon-lang` cookie and redirects to `/en/` or `/id/`. With no cookie it uses `/id/`.
- Without JavaScript, a `<noscript>` meta refresh sends the visitor to `/id/`, and a visible fallback link is shown.
- **Constraint:** Astro's built-in `redirectToDefaultLocale` must stay **off**. Hosting is fully static, so the cookie can only be read client-side.

### P-2 Home (`/en/`, `/id/`)
Sections, in order:
1. **Hero:** H1 "Tailored ERP Systems Built for Your Business." plus a subheadline about connecting every department into one platform.
2. **ERP journey diagram:** an animated 4-slide explainer:
   1. "From fragmented silos, chaotic communication": 7 scattered users connected by a messy mesh of arrows.
   2. "To centralize into one truth": all users point to a central Boffon ERP hub.
   3. "Complete end-to-end coverage": the hub expands into 7 module nodes.
   4. "Fully accountable financial control": modules arranged around Accounting at the core, with connecting arrows.
   - Auto-advances every 4 s. Has Previous/Next buttons, Play/Pause, and dot navigation. Any manual navigation pauses autoplay.
   - Respects `prefers-reduced-motion`: no autoplay, no animation.
   - Includes a screen-reader-only text description of the full sequence.
   - Module nodes in the diagram are labeled without the "Module" suffix.
3. **Challenge:** "90% of organizations globally still rely on spreadsheets…" with 5 pain points (Siloed Spreadsheets, No Single Source of Truth, Manual Processes & Errors, Zero Real-Time Visibility, Disconnected Teams).
4. **Comparison:** *Without ERP* vs *With ERP*, 5 items each, in two side-by-side cards (✕ vs ✓).
5. **Architecture:** a subtitle with inline links to the 4 industry pages, a card of 4 foundations (Adaptable Workflow Architecture, Flexible Integration, Flexible Deployment, 100% Data Ownership), and a card of links to all 7 modules.

The home page is the only page allowed to use full-width bands. All other pages follow the single-container layout rule (N-10).

### P-3 Product / module pages (×7)
All seven are built from one shared template. Each page has:
- **Breadcrumb:** Home › Products › {Module}.
- **Hero:** module icon, H1 module title, one-line subtitle.
- **Screenshot stack** (only when screenshots exist): an animated, cross-fading stack of product screenshots with two static "backing cards" behind it and a faint brand watermark.
  - Images are loaded from `src/assets/products/{folder}/`, sorted by filename. A file `N_name_dark.png` pairs with `N_name.png` and is shown in dark mode.
  - The first image loads eagerly with high priority. The rest load lazily. Responsive widths are 400/600/800/1200.
  - Every image has a localized caption as its alt text.
  - With reduced motion, only the first image is shown, statically.
- **Standard workflow:** a vertical diagram of step boxes joined by arrows, rendered on the server with zero client JavaScript.
- **Key Operations & Activities** list and **Core Reports & Insights** list. Each list shows the first 5 items, and a "Load more" toggle reveals the rest.

| Module | Subtitle | Workflow steps | Screenshots |
| :-- | :-- | :-- | :-- |
| Accounting | Financial clarity for every transaction. | Journal Entry → Payment Entry → Bank Reconciliation → Period Closing Voucher → Financial Statements → Audit Trail & Ledger Report | 5 |
| Finance | Turn financial data into decisions. | Budget Creation → Cost Center Allocation → Expense Claim & Revenue Posting → Budget Variance Report → Cash Flow Mapping → Financial Statements | 4 |
| Buying (Procurement) | Full visibility for every purchase order. | Material Request → RFQ → Supplier Quotation → Purchase Order → Purchase Receipt → Purchase Invoice → Payment Entry | 5 |
| Selling (Sales) | One pipeline, from lead to cash. | Lead → Opportunity → Quotation → Sales Order → Delivery Note → Sales Invoice → Payment Entry | 5 |
| Stock (Inventory) | No more stockouts or overstocking. | Purchase Receipt / Stock Entry → Warehouse Putaway → Batch & Serial Tracking → Stock Transfer / Material Request → Delivery Note → Stock Reconciliation | 5 |
| Project Management | Deliver projects on time, on budget. | Project Creation → Task & Milestone Setup → Timesheet Logging → Task Progress Tracking → Sales Invoice from Timesheet → Project Profitability Review | — |
| Manufacturing | Plan, produce, deliver with precision. | Sales Order / Demand Forecast → Production Plan → Material Request → Work Order → Job Card → Quality Inspection → Stock Entry – Manufacture | — |

The full operations and reports lists for each module live in `siteContent.json`.

### P-4 Industry pages (×4)
All four are built from one shared template. Each page has:
- **Breadcrumb:** Home › Industries › {Industry}.
- **Hero:** industry icon and H1 title.
- **Context paragraph** describing a typical day-to-day operational problem in that industry.
- **Hero image** (cropped, max height ~24 rem).
- **Two columns:** *Key Business Challenges* (4 items) and *How ERP Helps* (4 items, each naming a **module** in bold followed by its benefit).

| Industry | Nav label (EN / ID) | Icon | Modules referenced |
| :-- | :-- | :-- | :-- |
| Wholesale, Trading & Retail | Trading / Perdagangan | Truck | Stock, Accounting (e-Faktur), Selling, Buying |
| Manufacturing | Manufacturing / Manufaktur | CPU | Manufacturing, Stock, Accounting, Buying |
| Financial Services | Financial / Keuangan | Landmark | Accounting, Finance, Project |
| Professional & Business Services | Services / Layanan | Briefcase | Project, Accounting, Finance |

### P-5 About
- Breadcrumb, then H1 "About Us".
- Four rows, each with an icon or statistic on the left and copy on the right:
  1. 🚀 "Business Offline (to) Online": mission statement (digital evolution, integrated systems, automation, AI integration).
  2. **14+** "14+ Years of Industry Expertise".
  3. 🧩 "Software Built Around Your Business": customizability and best practices.
  4. **Trusted By:** a grid of 11 client logos (Elmoz Geo Solusi, FIFGROUP Astra, Hitachi, Indoparta Nusantara, Kehamilan Sehat, MedcoEnergi, MKAPR, PT Mulia Lestari, Putra Nusa Elshada, Sahabat Abadi Sejahtera, Supersoft Sistemindo). Logos sit on a light tile in both themes.
- **Headquarters & Location:** the legal name *PT Inovasi Teknologi Terintegrasi*, the address *Gedung Cahaya, Jl. Palmerah Utara III No. 9, RT 004/RW 006, Kec. Palmerah, Jakarta Barat, DKI Jakarta 11480*, and a lazy-loaded Google Maps embed.

### P-6 Blog index
- Breadcrumb. On large screens, a two-column layout: a left column with H1 "ERP, Business & AI Insights" and the subtitle, and a right column with post cards.
- Shows only posts in the current locale, newest first.
- Each card shows: date (formatted for the locale) · author · "N min read", then the title, description and tag pills. The whole card is a link.

### P-7 Blog post
- **Breadcrumb:** Home › Blog › {Post title}.
- **Header:** date · author · reading time, then H1 title, then tags.
- **Body:** Markdown rendered with typography styles. Every H2–H6 heading wraps itself in a self-link anchor that shows a link icon on hover.
- **Table of contents:** a collapsible box (open by default) listing the H2 headings. It is sticky in a right sidebar on large screens and sits above the content on small screens. It is hidden when the post has no H2.
- **Footer links:** "← Back to Blog", plus "Next Article →" pointing to the next **newer** post in the same locale (none on the newest post).
- **Reading time:** word count ÷ 200, rounded, minimum 1 minute.
- The language picker links to the translated version of the same post (see C-6).

### P-8 Terms of Service / Privacy Policy
- Breadcrumb, H1 title, and a "Last updated" line (currently August 24, 2026).
- An intro paragraph followed by numbered sections, rendered as H2 plus paragraphs in typography styles.
- **Terms**, 10 sections: Acceptance, Services, Use of Website, Intellectual Property, Fees & Payment, Confidentiality & Data Protection, Limitation of Liability, Changes, Governing Law (Republic of Indonesia), Contact.
- **Privacy**, 9 sections: Information Collected, Use, Cookies & Analytics (language cookie and Google Analytics), Third-Party Services (WhatsApp/Meta, hosting, and similar), Retention, Security, Your Rights, Changes, Contact.

### P-9 404
- A single top-level `404.html`, because GitHub Pages serves only the root 404 file. It is `noindex`.
- A centered card with a large "404", a title, a short message, and two buttons: *Back to homepage* and *Visit our blog*.
- Both language versions are in the HTML. A script shows the English version when the requested path starts with `/en`. Otherwise, or without JavaScript, the Indonesian version is shown.
- The header and footer render in the default locale (Indonesian). The CTA banner is not shown.

---

## 7. Content Requirements

- **C-1 All copy lives in data.** Every user-facing string is a `LocalizedText` `{ en, id }` entry in `src/data/siteContent.json`, read through `src/lib/content.ts`. Components must not hardcode copy.
- **C-2 SEO copy.** Every content block has `seo: { title, description }`. Page titles use the suffix `| Boffon`.
- **C-3 Module registry.** Adding a module requires:
  - an entry in `routes.ts → modules`
  - an entry in `src/lib/modules.ts` (icon and content key)
  - a content block in `siteContent.json` (`nav`, `seo`, `hero`, `workflow`, `operations`, `reports`, and optionally `screenshots`)
  - a page file per locale

  Modules then appear automatically in the header, footer, home page, contact form interests and ERP diagram (the diagram needs manual positioning).
- **C-4 Industry registry.** This works the same way as C-3, through `src/lib/industries.ts` and `siteContent.json → industries`.
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
- **C-7 Blog writing style.** Blog posts should favor content that is easy to extract (direct definitions, bulleted lists, comparison tables) and link to related posts. Current posts:
  - *What is ERP?* / *Apa Itu ERP?* (2026-08-15)
  - *The Benefits of ERP Across Business Aspects* / *Manfaat Sistem ERP di Berbagai Aspek Bisnis* (2026-08-23)
  - *ERP for SMEs* / *ERP untuk UMKM* (2026-09-01)

  All are by author "Iman".

## 8. Internationalization

- **I-1** Two locales: `id` (default) and `en`. Every route has a locale prefix (`/id/…`, `/en/…`).
- **I-2** Every page pair is registered as `{ en, id }` in `src/lib/routes.ts`. Pages without an entry cannot emit correct canonical and hreflang links.
- **I-3** `<html lang>` matches the page locale. Dates are formatted with `id-ID` or `en-US`.
- **I-4** The visitor's language choice is remembered via the `boffon-lang` cookie and applied at `/` (see P-1).
- **I-5** Every page must be fully available in both languages. Blog posts are the exception: they may exist in one language only, and the language picker then lists only the languages that exist.

## 9. SEO & GEO (Generative Engine Optimization)

- **S-1** Each page has exactly one `<h1>`, and heading levels never skip.
- **S-2** `BaseLayout` emits, from content data, the following tags. Pages must never hardcode them.
  - `<title>`, meta description, `author`, `robots: index, follow`
  - canonical URL
  - `hreflang` alternates for `en` and `id`, plus `x-default` pointing to the Indonesian page
  - OpenGraph tags: type, site_name, title, description, url, 1200×630 `og-image.png`, locale `id_ID`/`en_US` plus the alternate locale
  - Twitter `summary_large_image` card
- **S-3** Structured data (JSON-LD):
  - Every page includes a `ProfessionalService` block (name, URL, logo, image, description, `areaServed: ID`, `knowsAbout`: ERP Implementation, Business Process Automation, System Integration, Enterprise Software Customization).
  - Every non-home page includes a `BreadcrumbList` that matches its visible breadcrumb.
  - Blog posts include a `BlogPosting` block (headline, description, datePublished, inLanguage, keywords, author as a Person, publisher as an Organization, mainEntityOfPage).
  - New page types with a natural schema.org type (FAQ, Product, and similar) should add their own JSON-LD.
- **S-4** Content that crawlers need must be server-rendered. AI crawlers usually don't run JavaScript, so diagrams, workflows and lists must exist in the static HTML.
- **S-5** `robots.txt` allows `*` and explicitly allows GPTBot, ClaudeBot, PerplexityBot and Google-Extended. It also points to `sitemap-index.xml`.
- **S-6** An XML sitemap is generated automatically for every page and linked from the footer.
- **S-7** The root redirect page and the 404 page are `noindex`.

## 10. Non-Functional Requirements

### Performance
- **N-1** The site is fully static, with no runtime server.
- **N-2** All CSS is inlined into `<head>` (`inlineStylesheets: 'always'`) to avoid render-blocking stylesheet requests.
- **N-3** Images are optimized through Astro's asset pipeline, with responsive `srcset`, lazy loading below the fold, and an eager, high-priority first screenshot. Maps and other embeds load lazily.
- **N-4** Fonts are self-hosted via `@fontsource`: Alegreya 500–800 for headings and Outfit 400–700 for body text. No third-party font requests.
- **N-5** Client JavaScript is kept small and limited to progressive enhancement: theme, language cookie, menu helpers, slider, modal, and analytics.

### Accessibility
- **N-6** Semantic landmarks are used: `header`, `nav` with `aria-label`, `main`, `footer`, `nav[aria-label=Breadcrumb]`, and `aria-current` on the active breadcrumb item and active language.
- **N-7** All animations respect `prefers-reduced-motion`. That covers the ERP slider, the screenshot stack and the typewriter.
- **N-8** Interactive controls are keyboard-reachable and show visible focus outlines. Icon-only buttons have `aria-label`s. Decorative icons are `aria-hidden`.
- **N-9** Text colors meet WCAG AA (4.5:1) contrast in both themes. For example, dark mode uses `--color-primary-text: #6cabad` specifically to pass on every dark surface.

### Design system
- **N-10** Page layout: every page except home wraps its breadcrumb and content in one container, `mx-auto max-w-6xl px-4 py-8 sm:px-6 lg:px-8`, matching the footer and CTA banner.
- **N-11** Colors come only from semantic tokens in `global.css`: primary, secondary, bg-app, bg-surface (with elevated, hover and invert variants), text-primary, text-secondary, text-on-primary, border-subtle/strong, and status colors.
  - Light theme: brand blue `#2D68C4` on slate/white.
  - Dark theme: brand teal `#3b7e80` on slate-950/900.
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

- **D-1** Hosting is GitHub Pages on the custom domain `boffon.com` (configured in `public/CNAME`).
- **D-2** Every push to `main`, or a manual dispatch, runs `.github/workflows/deploy.yml` (`withastro/action@v4` then `actions/deploy-pages@v4`) and deploys to production. **There is no staging environment.**
- **D-3** The build fails on blog naming or schema violations (C-5, C-6), so a broken post cannot reach production.

---

## 12. Observed Gaps & Open Items

These were found while reverse-engineering the site. Each needs a decision: fix it, or record it as intentional.

| # | Observation | Related rule |
| :-- | :-- | :-- |
| 1 | The ERP journey diagram's slide captions are defined in the component instead of `siteContent.json`. Its screen-reader description and control labels (Previous/Next/Pause/"Go to slide") are hardcoded **in English**, so Indonesian pages read them in English. | C-1, I-5 |
| 2 | The "Load more / Muat lebih banyak" label in `ModuleList.astro` and the theme option labels (Light/Dark/System) are hardcoded. The theme labels are English-only. | C-1, I-5 |
| 3 | The Project and Manufacturing module pages have no screenshots, unlike the other five modules. | P-3 |
| 4 | `TypewriterHeadline.astro` exists but no page uses it. The content keys `product.*`, `blog.readMore` and `blog.publishedOn` are also unused. | — |
| 5 | Blog post `<title>` tags use the bare post title, without the `\| Boffon` suffix used everywhere else. | C-2 |
| 6 | On the 404 page, the language picker label falls back to `EN` even though the page renders in Indonesian, and the page doesn't load analytics, so 404 hits aren't tracked. | P-9, G-22 |
| 7 | The header's contact button is labeled and styled as "WhatsApp" but opens the contact form first. The behavior works; the label may mislead screen-reader users. | G-5 |
| 8 | "Next Article" links to the next **newer** post. Readers may expect it to go to the next older post. | P-7 |
| 9 | `README.md` is still the Astro starter boilerplate. The package name is `www.boffon.com`, while the repository folder is `www.navario.id`. | — |
