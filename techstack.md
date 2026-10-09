# Tech Stack

Internal. How the system is built, who owns each part, and the design rules that keep the "no vendor lock-in" promise true. Licences and IP are in [2_legal.md](2_legal.md#3-code-ownership-ip). What is built today is in [4_product_scope.md](4_product_scope.md).

## 1. Layers

```
┌───────────────────────────────────────────────────────────────┐
│  Company_Custom      one client's customization               │  Client proprietary
├───────────────────────────────┬───────────────────────────────┤
│  Nava AI                      │                               │  Closed source
│  AI Business Assistant        │                               │  PT Upaya Teknologi Sejahtera
├───────────────────────────────┘                               │
│  Platform Core       UI/UX, Bahasa Indonesia, localization    │  Closed source
│                                                               │  PT Upaya Teknologi Sejahtera
├───────────────────────────────────────────────────────────────┤
│  ERPNext             Accounting, Buying, Selling, Stock,      │  Open source (GPL v3)
│                      Asset Management                         │
├───────────────────────────────────────────────────────────────┤
│  Frappe              web framework, users, permissions, DB    │  Open source (MIT)
└───────────────────────────────────────────────────────────────┘
```

| Layer | What it does | Owner |
| :-- | :-- | :-- |
| **Frappe** (v16) | Web framework: database, users, roles and permissions, REST API, document engine | Open source |
| **ERPNext** (v16) | The ERP modules Navario sells ([C5](0_business_constraint.md#2-offer)) | Open source |
| **Platform Core** | Simplified screens and menus, Bahasa Indonesia translation, Indonesian localization (chart of accounts, PPN/PPh setup, print formats), company branding | Navario |
| **Nava AI** | The AI Business Assistant: chat app (Vue frontend, served inside Frappe, same login), agentic workflow, business tools, request log, usage tracking | Navario |
| **Company_Custom** | Fields, workflows, print formats and integrations built for one client | The client |

## 2. Nava AI

```
User (chat app, same login as the ERP)
   │
   ▼
1. Intent classifier ─────────── Gemini Flash-Lite
   │
   ▼
2. Reasoning: plan the steps ─── Gemini Flash
   │
   ▼
3. Execution loop ────────────── Gemini Flash
   │   AI asks for a tool ──► System checks the user's permissions,
   │                          runs the tool, logs the request
   │   ◄── result ────────────┘
   ▼
Answer: summary, table, or link to a document, report or pre-filled form
```

- **The model never touches the database.** It can only ask for a tool. The system checks the user's permissions (the same Frappe roles and permissions as the ERP), runs the tool, and returns the result.
- **No write without the user.** New documents open as pre-filled forms the user saves. Actions and setup changes show a preview and need Apply.
- **Request log:** who asked what and whether it was allowed. Field values are never logged.
- **AI provider:** Google Gemini only ([C7](0_business_constraint.md#2-offer)), the fastest route for now. A move to a cheaper provider of the same quality is planned, so all model calls go through one internal interface ([X16](1_challenges.md#6-product-and-technology)). Model stack and cost: [ai_cost_simulation.md](ai_cost_simulation.md).
- **AI key:** retail uses Navario's key with a question pool per company. Enterprise and AI projects use the client's own key (BYOK).

## 3. Hosting

| | **Retail (SaaS)** | **Enterprise** |
| :-- | :-- | :-- |
| **Server** | Shared cloud | Dedicated server per client |
| **Backups** | Daily, kept 14 days | Daily, kept 30 days |
| **AI key** | Navario's | The client's (BYOK) |
| **Provider and region** | DigitalOcean, Singapore | DigitalOcean, Singapore |
| **Who hosts** | Navario | Navario. No on-premise ([L6](2_legal.md#1-rules)). |

DigitalOcean is the fastest route for now. A move to a cheaper host of the same quality is planned ([X16](1_challenges.md#6-product-and-technology)).

Client data is stored outside Indonesia, and AI questions are processed by Google. Both must be disclosed in the service agreement and Privacy Policy ([L7](2_legal.md#1-rules)), not in marketing.

## 4. Design rules

These keep the client free to leave, and keep Platform Core and Nava AI closed. Today's code follows rules 1–3 (confirmed by the founder, 9 Oct 2026). Re-check them before every major ERPNext upgrade.

1. **ERPNext is never modified.** Platform Core, Nava AI and Company_Custom are separate apps on top of it. So ERPNext upgrades follow the open-source releases, and a client's system can run on plain ERPNext.
2. **Company_Custom depends only on Frappe and ERPNext,** never on Platform Core or Nava AI. Otherwise the client's own code breaks when they leave.
3. **Configuration is stored as data.** Chart of accounts, tax templates, print formats and roles that Platform Core sets up are saved as records in the client's database, not only in Platform Core code. So they stay with the client.
4. **Client data lives only in the client's database.** Nava AI keeps the request log and usage counts, not business data.
5. **No source code leaves Navario** for Platform Core or Nava AI: not to partners, not to clients ([8_partnership_model.md](8_partnership_model.md#rules), rule 3).

## 5. If a client leaves

| Stays with the client | Stays with Navario |
| :-- | :-- |
| All business data (full export) | Simplified screens and menus (Platform Core) |
| Configuration stored as data: chart of accounts, tax setup, print formats, users and roles (rule 3) | Bahasa Indonesia translation (Platform Core) |
| ERPNext and Frappe (open source) | AI Business Assistant (Nava AI) |
| Their own customization (Company_Custom) | |

The client can run its business on plain ERPNext with any other provider. That is what "no vendor lock-in" means in sales material.

## Assumptions

- One shared server holds many retail clients (one Frappe site per client).
- Moving to another host or AI provider later is possible without client-facing changes.

## Open decisions

- [ ] **Server cost per retail client.** Unknown, but needed for the financial model ([5 §6](5_saas_pricing_model.md#6-financial-model), [6 §6](6_enterprise_pricing_model.md#6-financial-model)). Recommendation: measure it on the demo server.
- [ ] **Backup restore drill.** Backups are promised; a restore has never been tested. Recommendation: run one before the first go-live.
- [ ] **What a "full data export" contains** ([4_product_scope.md](4_product_scope.md#2-first-paid-client), 2.9). Recommendation: a database backup plus files, tested once by restoring it on plain ERPNext.
- [ ] **When to move host and AI provider.** Recommendation: after the first paying clients, when real usage data shows the saving. Re-run the cost simulation for the new provider first.
