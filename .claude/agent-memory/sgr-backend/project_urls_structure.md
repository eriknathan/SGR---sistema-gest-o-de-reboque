---
name: URL structure — root and app namespaces
description: URL routing structure established in Sprint 1
type: project
---

`sgr/urls.py` configurado com:
- `admin/` → Django admin
- `accounts/` → `accounts.urls` com namespace `accounts`

Namespaces de URL por app:
- `accounts` → `accounts:login`, `accounts:logout`

**Why:** Sprint 1 estabeleceu a estrutura base de URLs.
**How to apply:** Ao adicionar novos apps, incluir com `include('app.urls', namespace='app')` e definir `app_name` no `urls.py` do app.
