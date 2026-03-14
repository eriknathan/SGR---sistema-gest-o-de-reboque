from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Configuracao do app de autenticacao e gerenciamento de usuarios."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        """Registra os signals do app accounts ao inicializar."""
        pass  # signals serao importados aqui quando criados
