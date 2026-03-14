---
name: project_drivers_app
description: Driver and DriverPayment models, forms, CBVs, and URL structure implemented in Sprint 4
type: project
---

App `drivers` implementado na Sprint 4 (2026-03-14).

## Models

**Driver** (`drivers/models.py`):
- Campos principais: `name`, `document` (CPF, unique), `phone`, `email`, `cnh_number` (unique), `cnh_category` (choices A/B/AB/C/D/E), `cnh_expiration` (DateField), `admission_date` (DateField), `base_salary` (Decimal 10,2)
- Endereço: `zip_code`, `street`, `number`, `complement`, `neighborhood`, `city`, `state`
- Auditoria: `created_at`, `updated_at`
- Meta: `ordering = ['name']`

**DriverPayment** (`drivers/models.py`):
- FK para `Driver` via `related_name='payments'`
- Campos: `amount` (Decimal 10,2), `payment_date` (DateField), `description` (TextField, blank)
- Meta: `ordering = ['-payment_date']`

## Forms (`drivers/forms.py`)

- `DriverForm`: todos os campos do Driver exceto audit; campos de endereço com `required=False` no `__init__`; `DateInput` com `type=date` para `cnh_expiration` e `admission_date`
- `DriverPaymentForm`: campos `amount`, `payment_date`, `description`; `DateInput` com `type=date` para `payment_date`
- Classes CSS do Design System: `INPUT_CLASSES` e `SELECT_CLASSES` definidas como constantes no topo do arquivo

## Views (`drivers/views.py`)

- `DriverListView`: busca por `q` em `name__icontains | document__icontains`, paginação 20
- `DriverCreateView`: `success_url = reverse_lazy('drivers:list')`, mensagem em pt-BR
- `DriverUpdateView`: idem
- `DriverDetailView`: `get_context_data` inclui `payments = driver.payments.all()` e tenta `driver.incident_set.all()` dentro de try/except (incidents app ainda não existe)
- `DriverPaymentCreateView`: recebe `driver_pk` da URL, atribui `form.instance.driver` no `form_valid`, redireciona para `drivers:detail` do motorista

## URLs (`drivers/urls.py`)

```
app_name = 'drivers'
''                         → drivers:list
'create/'                  → drivers:create
'<int:pk>/edit/'           → drivers:edit
'<int:pk>/'                → drivers:detail
'<int:driver_pk>/payment/add/' → drivers:payment_add
```

Incluído em `sgr/urls.py` com prefixo `motoristas/`.

**Why:** Módulo central para gestão de motoristas e histórico de pagamentos, prerequisito para o app `incidents`.

**How to apply:** Ao criar o app `incidents`, lembrar de adicionar FK para `Driver`. O `DriverDetailView` já tem try/except preparado para incluir `incident_set` quando o app existir.
