---
name: project_customers_app
description: Customer model, forms, views e URLs implementados na Sprint 3
type: project
---

App `customers` implementado na Sprint 3 (2026-03-14).

**Model `Customer`** em `customers/models.py`:
- Campos: `type` (PF/PJ), `name`, `document` (unique, max 18), `phone`, `email`
- Endereço: `zip_code`, `street`, `number`, `complement`, `neighborhood`, `city`, `state` — todos `blank=True`
- Auditoria: `created_at` (auto_now_add), `updated_at` (auto_now)
- `Meta.ordering = ['name']`, verbose_name em pt-BR

**Form `CustomerForm`** em `customers/forms.py`:
- `ModelForm` com todos os campos do model (exceto auditoria)
- Widgets com classes do Design System via `INPUT_CLASSES` / `SELECT_CLASSES`
- Campos de endereço marcados como `required=False` em `__init__`
- IDs explícitos em campos de endereço para integração ViaCEP via JS

**Views** em `customers/views.py`:
- `CustomerListView` — busca via `Q(name__icontains=q) | Q(document__icontains=q)`, paginação 20
- `CustomerCreateView` — `SuccessMessageMixin`, `success_url = reverse_lazy('customers:list')`
- `CustomerUpdateView` — idem, mesma URL de sucesso
- `CustomerDetailView` — tenta `incident_set.all()` dentro de try/except (guard para sprint futura)
- Todas com `LoginRequiredMixin`

**URLs** em `customers/urls.py` com `app_name = 'customers'`:
- `''` → `customers:list`
- `'create/'` → `customers:create`
- `'<int:pk>/edit/'` → `customers:edit`
- `'<int:pk>/'` → `customers:detail`
- Incluído em `sgr/urls.py` como `path('clientes/', include('customers.urls', namespace='customers'))`

**Migration**: `customers/migrations/0001_initial.py` aplicada.

**Why:** módulo central de CRUD de clientes PF/PJ, base para vinculação com sinistros (incidents).
**How to apply:** ao criar incidents, o FK deve apontar para `customers.Customer`; `CustomerDetailView` já tem guard para `incident_set`.
