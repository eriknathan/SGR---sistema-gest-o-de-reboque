"""App configuration for the customers app."""

from django.apps import AppConfig


class CustomersConfig(AppConfig):
    """Configuration class for the customers app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers'
    verbose_name = 'Clientes'
