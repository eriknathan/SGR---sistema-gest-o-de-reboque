---
name: URL structure — root and app namespaces
description: URL routing structure established in Sprint 1
type: project
---

`sgr/urls.py` configurado com:
- `admin/` → Django admin
- `accounts/` → `accounts.urls` com namespace `accounts`
- `''` (raiz) → `core.urls` com namespace `core`
- `clientes/` → `customers.urls` com namespace `customers`

Namespaces de URL por app:
- `accounts` → `accounts:login`, `accounts:logout`
- `core` → `core:dashboard` (rota raiz `/`)
- `customers` → `customers:list`, `customers:create`, `customers:edit`, `customers:detail`

**Why:** Sprint 1 estrutura base; Sprint 2 core na raiz; Sprint 3 adicionou customers em /clientes/.
**How to apply:** Ao adicionar novos apps, incluir com `include('app.urls', namespace='app')` e definir `app_name` no `urls.py` do app.
