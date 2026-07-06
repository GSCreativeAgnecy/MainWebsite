
# GS Creative Agency — Main Website

The official company website for [GS Creative Agency](https://gscreativeagency.com), a Calgary-based digital creative agency.

Built with **FastAPI** + **Jinja2** + **Tailwind CSS** — zero client-side build step, deploy anywhere.

---

## Pages

| Route | Page |
|-------|------|
| `/` | Home — hero, stats, services preview, CTA |
| `/services` | Services — 4 service cards + process flow |
| `/about` | About — story, values, company info |
| `/portfolio` | Portfolio — project showcase (RW, Brownies, FSH) |
| `/contact` | Contact — multi-currency budget form, contact info |
| `/health` | Health check — returns `{"status": "ok"}` |
| `*` | 404 — custom not-found page |

---

## Tech Stack

- **Backend:** Python 3.11+, FastAPI, Uvicorn
- **Templates:** Jinja2 (server-rendered)
- **Styling:** Tailwind CSS (CDN — no build step)
- **Deployment:** Docker + Docker Compose, Coolify-ready

---

## Quick Start

### Local Development

```bash
# Clone
git clone https://github.com/GSCreativeAgnecy/MainWebsite.git
cd MainWebsite

# Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run
uvicorn main:app --reload --port 8000
```

Open **http://localhost:8000** in your browser.

### Docker

```bash
docker compose up -d
```

### Coolify

1. Connect your Coolify instance to `github.com/GSCreativeAgnecy/MainWebsite.git`
2. Select **Docker Compose** as the build pack
3. Coolify auto-detects `docker-compose.yaml`
4. Set your domain in Coolify's proxy settings
5. Deploy — the `/health` endpoint confirms the container is healthy

---

## Project Structure

```
MainWebsite/
├── main.py                 # FastAPI app (routes + contact form handler)
├── Dockerfile              # Docker image (Python 3.11-slim + curl)
├── docker-compose.yaml     # Coolify-ready compose file
├── requirements.txt        # Python dependencies
├── LICENSE                 # All Rights Reserved
├── README.md               # This file
├── static/
│   └── css/
│       └── style.css       # Custom styles (animations, glass, gradients)
└── templates/
    ├── base.html           # Base layout (nav, footer, scroll animations)
    ├── index.html          # Home page
    ├── services.html       # Services page
    ├── about.html          # About page
    ├── portfolio.html      # Portfolio page
    ├── contact.html        # Contact form with multi-currency budget
    └── 404.html            # Custom 404 page
```

---

## Contact Form

The `/contact` page includes a working form that sends a **JSON POST** to `/contact`.

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Required |
| `email` | string | Required |
| `company` | string | Optional |
| `budget_currency` | string | USD, CAD, EUR, GBP, INR |
| `budget` | string | `<5k`, `5k-15k`, `15k-50k`, `50k+` |
| `message` | string | Required |

### Backend

The POST endpoint logs submissions via Python `logging`. In production, wire it to SendGrid / Resend / SMTP to forward submissions to `hello@gscreativeagency.com`.

---

## Brand

- **Primary:** Gold/Amber (`#f59e0b`)
- **Background:** Dark gray/navy (`#111827`, `#0f172a`)
- **Text:** White + gray-400
- **Font:** Inter (via Google Fonts)

---

## License

Copyright © 2026 GS Creative Agency. All rights reserved.

This repository is publicly viewable for portfolio/reference purposes. You may **not** copy, modify, distribute, or use the code or design without prior written permission. See [LICENSE](./LICENSE) for full terms.

---

## Contact

- **Email:** hello@gscreativeagency.com
- **Location:** Calgary, Alberta, Canada
