---
name: accounts app — Sprint 1 implementation
description: CustomUser model, EmailBackend, login/logout views and URLs implemented in Sprint 1
type: project
---

App `accounts` implementado na Sprint 1 com os seguintes componentes:

- `accounts/models.py`: `CustomUser` herda de `AbstractBaseUser` + `PermissionsMixin`. Campos: `email` (USERNAME_FIELD), `first_name`, `last_name`, `is_active`, `is_staff`, `created_at`, `updated_at`. Manager customizado `CustomUserManager` com `create_user` e `create_superuser`.
- `accounts/backends.py`: `EmailBackend` herda de `ModelBackend`. Autentica pelo campo `email`, aceita `username` como alias para compatibilidade com formulários Django.
- `accounts/forms.py`: `EmailAuthenticationForm` herda de `AuthenticationForm`. Redefine campo `username` como `EmailField` com label 'E-mail' em pt-BR.
- `accounts/views.py`: `CustomLoginView` herda de `LoginView`. Usa `EmailAuthenticationForm`, template `accounts/login.html`, `redirect_authenticated_user=True`.
- `accounts/urls.py`: namespace `accounts`, rotas `login/` e `logout/`.
- Migration: `accounts/migrations/0001_initial.py` — banco recriado do zero (db.sqlite3 anterior descartado por conflito de histórico).

**Why:** Sprint 1 exigiu autenticação por e-mail em vez do username padrão do Django.

**How to apply:** Sempre referenciar `AUTH_USER_MODEL = 'accounts.CustomUser'`. Nunca usar `User` diretamente — usar `get_user_model()`. Login via `/accounts/login/`.
