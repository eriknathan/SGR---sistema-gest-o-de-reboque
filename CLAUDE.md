# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**SGR — Sistema de Gestão de Reboque.** Django 5.x full-stack web app for tow truck service management. See `docs/` for full documentation and `PRD.md` for product requirements.

## Commands

```bash
# Setup
python -m venv venv && source venv/bin/activate
pip install django python-decouple pillow requests num2words

# Development
python manage.py migrate
python manage.py runserver           # http://localhost:8000
python manage.py createsuperuser

# Quality
flake8 .                             # PEP8 check
python manage.py test                # Django test runner
```

## Architecture

Django project at `sgr/` (settings, urls, wsgi). Eight apps:

| App | Role |
|---|---|
| `accounts` | `CustomUser` with email login, `EmailBackend` in `backends.py` |
| `core` | Dashboard, shared mixins |
| `customers` | PF/PJ clients — ViaCEP + CNPJ API integration |
| `drivers` | Drivers + `DriverPayment` history |
| `fleet` | Company vehicles |
| `incidents` | Central module — tow services, 3-stage photo upload, public UUID |
| `receipts` | PDF generation (WeasyPrint/ReportLab), public access via UUID |
| `notifications` | SMTP email with PDF attachment |

All templates live in `templates/` at the **project root**, organized by app. `settings.py` `DIRS` points there.

## Critical Settings

```python
AUTH_USER_MODEL = 'accounts.CustomUser'   # email-based auth, no username
AUTHENTICATION_BACKENDS = ['accounts.backends.EmailBackend']
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

All secrets and config via `.env` read with `python-decouple`. Never hardcode.

## Mandatory Conventions

- **Single quotes** throughout all Python code.
- **CBV always** — use `LoginRequiredMixin` on every protected view.
- **Every model** must have `created_at = DateTimeField(auto_now_add=True)` and `updated_at = DateTimeField(auto_now=True)`.
- **Signals** go in `<app>/signals.py` only — never in `models.py`.
- **Code in English, UI in pt-BR** (labels, messages, error text, generated documents).
- **Docstrings** on all classes and methods.

## Frontend

TailwindCSS loaded via CDN — no build step. Theme config is inline in `base.html`. Font: Poppins (Google Fonts). Design System tokens and component snippets are in `docs/design-system.md`.

Key JS integrations written inline in templates:
- CEP → address autofill via ViaCEP API
- CNPJ → company data autofill via BrasilAPI (PJ clients only)
- File input → image preview before upload

## Agents

Specialized agents are defined in `agents/`:
- `agents/backend.md` — Django backend (models, views, PDF, email, APIs)
- `agents/frontend.md` — DTL templates + TailwindCSS + inline JS
- `agents/qa.md` — browser testing via Playwright against `localhost:8000`
