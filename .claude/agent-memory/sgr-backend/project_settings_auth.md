---
name: settings.py — auth configuration
description: Auth-related settings already configured in sgr/settings.py
type: project
---

Configurações de autenticação já presentes em `sgr/settings.py`:

```python
AUTH_USER_MODEL = 'accounts.CustomUser'
AUTHENTICATION_BACKENDS = ['accounts.backends.EmailBackend']
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
```

Outras configurações relevantes já presentes:
- `LANGUAGE_CODE = 'pt-br'`
- `TIME_ZONE = 'America/Sao_Paulo'`
- `TEMPLATES DIRS = [BASE_DIR / 'templates']` — templates na raiz do projeto
- `python-decouple` já importado e em uso para `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`

**Why:** Configurações definidas na Sprint 1.
**How to apply:** Ao alterar settings, editar apenas as seções afetadas. Sempre usar `python-decouple` para novos valores sensíveis.
