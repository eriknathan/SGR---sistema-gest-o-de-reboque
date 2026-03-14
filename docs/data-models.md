# Modelos de Dados

Toda model deve ter os campos `created_at` e `updated_at`.

## Diagrama de Relacionamentos

```
USER ──────────────────────────────────────────────┐
                                                   │ registra
CUSTOMER ──┐                                       │
           │ possui                                ▼
DRIVER ────┼──────────────────────────────► INCIDENT ──► INCIDENT_PHOTO
           │ realiza                               │
VEHICLE ───┘ é utilizado                           └──► RECEIPT

DRIVER ──► DRIVER_PAYMENT
```

## Entidades

### USER (`accounts`)

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | int PK | |
| `email` | string | Campo de autenticação (substitui username) |
| `password` | string | |
| `first_name` | string | |
| `last_name` | string | |
| `is_active` | bool | |
| `created_at` | datetime | |
| `updated_at` | datetime | |

`USERNAME_FIELD = 'email'` — autenticação feita via `EmailBackend`.

---

### CUSTOMER (`customers`)

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | int PK | |
| `type` | string | `PF` ou `PJ` |
| `name` | string | Nome / Razão Social |
| `document` | string | CPF ou CNPJ |
| `phone` | string | |
| `email` | string | |
| `street` | string | Opcional |
| `number` | string | Opcional |
| `complement` | string | Opcional |
| `neighborhood` | string | Opcional |
| `city` | string | Opcional |
| `state` | string | Opcional |
| `zip_code` | string | Opcional — dispara busca ViaCEP |
| `created_at` | datetime | |
| `updated_at` | datetime | |

---

### DRIVER (`drivers`)

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | int PK | |
| `name` | string | |
| `document` | string | CPF |
| `phone` | string | |
| `email` | string | |
| `cnh_number` | string | Número da CNH |
| `cnh_category` | string | Categoria da CNH |
| `cnh_expiration` | date | Validade da CNH |
| `admission_date` | date | Data de admissão |
| `base_salary` | decimal | Salário base |
| `street` | string | |
| `number` | string | |
| `neighborhood` | string | |
| `city` | string | |
| `state` | string | |
| `zip_code` | string | |
| `created_at` | datetime | |
| `updated_at` | datetime | |

---

### DRIVER_PAYMENT (`drivers`)

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | int PK | |
| `driver` | FK → DRIVER | |
| `amount` | decimal | |
| `payment_date` | date | |
| `description` | string | |
| `created_at` | datetime | |
| `updated_at` | datetime | |

---

### VEHICLE (`fleet`)

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | int PK | |
| `model` | string | |
| `brand` | string | |
| `plate` | string | |
| `renavam` | string | |
| `year` | int | |
| `color` | string | |
| `type` | string | |
| `created_at` | datetime | |
| `updated_at` | datetime | |

---

### INCIDENT (`incidents`)

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | int PK | |
| `customer` | FK → CUSTOMER | |
| `driver` | FK → DRIVER | |
| `vehicle` | FK → VEHICLE | Veículo da frota (rebocador) |
| `towed_plate` | string | Placa do veículo rebocado |
| `towed_color` | string | |
| `towed_type` | string | |
| `towed_model` | string | |
| `origin_address` | string | |
| `destination_address` | string | |
| `payment_method` | string | `PIX`, `BOLETO` ou `DINHEIRO` |
| `service_value` | decimal | |
| `service_value_written` | string | Valor por extenso (gerado via `num2words`) |
| `service_datetime` | datetime | Data/hora do serviço |
| `notes` | string | Observações livres |
| `uuid` | UUID | Identificador público para link sem login |
| `created_at` | datetime | |
| `updated_at` | datetime | |

---

### INCIDENT_PHOTO (`incidents`)

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | int PK | |
| `incident` | FK → INCIDENT | |
| `photo_url` | string | Caminho no storage (MinIO) |
| `stage` | string | `BEFORE`, `EMBARKED` ou `DELIVERED` |
| `created_at` | datetime | |
| `updated_at` | datetime | |

Upload obrigatório nas 3 etapas. Armazenamento via MinIO (local) → S3 (futuro).

---

### RECEIPT (`receipts`)

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | int PK | |
| `incident` | FK → INCIDENT (OneToOne) | |
| `file_name` | string | `Recibo-[Empresa]-[Placa]-[Data].pdf` |
| `file_path` | string | Caminho em `MEDIA_ROOT/receipts/` |
| `generated_at` | datetime | |
| `created_at` | datetime | |
| `updated_at` | datetime | |
