# Padrões de Código

## Regras Gerais

- **Linguagem do código:** inglês — variáveis, funções, classes, nomes de arquivos e campos de models.
- **Interface:** português brasileiro (pt-BR) — labels, mensagens de erro, textos exibidos ao usuário e documentos gerados.
- **Aspas:** aspas simples em todo o código Python.
- **Estilo:** PEP8. Usar `flake8` para verificação.
- **Docstrings:** obrigatórias em todas as classes e métodos.
- **Sem over-engineering:** código simples, sem abstrações desnecessárias.

## Views

Usar **Class Based Views (CBV)** sempre que possível.

Toda view protegida deve usar `LoginRequiredMixin`.

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
```

## Models

Toda model deve ter os campos `created_at` e `updated_at`:

```python
class Customer(models.Model):
    # campos...
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## Signals

Signals devem ficar em arquivo `signals.py` dentro do respectivo app — nunca dentro de `models.py` ou `views.py`.

```
customers/
├── models.py
├── signals.py   ← signals aqui
├── views.py
└── ...
```

## Forms

Usar `ModelForm`. Aplicar as classes do Design System (Tailwind) via `attrs` nos widgets.

## Variáveis de Ambiente

Todas as configurações críticas via arquivo `.env`, lidas com `python-decouple`.

Nunca commitar o arquivo `.env`. O `.gitignore` deve incluir:
```
.env
venv/
*.sqlite3
__pycache__/
```

## Nomenclatura de Arquivos de Recibo

```
Recibo-[NomeDaEmpresa]-[PlacaDoVeiculo]-[Data].pdf
```
