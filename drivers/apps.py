"""App configuration for the drivers app."""

from django.apps import AppConfig


class DriversConfig(AppConfig):
    """Configuration class for the drivers app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drivers'
    verbose_name = 'Motoristas'
