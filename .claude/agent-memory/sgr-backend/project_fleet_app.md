---
name: project_fleet_app
description: App fleet — Vehicle model, VehicleForm, CBVs de CRUD, URLs em /frota/ (Sprint 5)
type: project
---

App `fleet` implementado na Sprint 5 (tarefas 5.1 e 5.2).

**Why:** Módulo de gestão da frota de veículos da empresa de reboque.

**How to apply:** Ao trabalhar no app fleet ou em integrações que referenciam veículos (incidents, receipts).

## Model: Vehicle (`fleet/models.py`)

Campos: `brand`, `model`, `plate` (unique), `renavam` (unique, max_length=11), `year` (PositiveIntegerField), `color` (blank=True), `type` (choices), `created_at`, `updated_at`.

`TYPE_CHOICES`: `guincho`, `caminhao`, `utilitario`, `outro`.

`__str__`: `f'{self.brand} {self.model} — {self.plate}'`

`Meta.ordering = ['brand', 'model']`

Migration: `fleet/migrations/0001_initial.py`

## Form: VehicleForm (`fleet/forms.py`)

`ModelForm` com todos os campos exceto `created_at`/`updated_at`. Usa `INPUT_CLASSES` e `SELECT_CLASSES` do Design System. Campo `year` usa `NumberInput` com `attrs={'min': 1990, 'max': 2030}`.

## Views (`fleet/views.py`)

- `VehicleListView`: busca por Q object com `plate__icontains | brand__icontains | model__icontains`, `paginate_by=20`, contexto `query`.
- `VehicleCreateView`: `success_message='Veículo cadastrado com sucesso.'`
- `VehicleUpdateView`: `success_message='Veículo atualizado com sucesso.'`
- `VehicleDetailView`: tenta `self.object.incident_set.all()` dentro de `try/except Exception` — padrão defensivo para quando o app `incidents` ainda não existe.

## URLs (`fleet/urls.py`)

`app_name = 'fleet'`

- `'' -> fleet:list`
- `'create/' -> fleet:create`
- `'<int:pk>/edit/' -> fleet:edit`
- `'<int:pk>/' -> fleet:detail`

Incluído em `sgr/urls.py` com prefixo `frota/`.

## Templates (`templates/fleet/`)

- `vehicle_list.html` — tabela com badge de placa em `font-mono bg-[#1a2c42]`, badges coloridos por tipo, busca, paginação.
- `vehicle_form.html` — seção única "Identificação", grid responsivo, sem JS extra (sem CEP/CNPJ).
- `vehicle_detail.html` — cabeçalho com ícone SVG, seção de dados e seção de sinistros (renderiza lista se incidents existir, estado vazio caso contrário).
