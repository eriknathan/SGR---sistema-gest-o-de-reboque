from django.db import models


class Vehicle(models.Model):
    """Model representing a company vehicle in the fleet."""

    TYPE_CHOICES = [
        ('guincho', 'Guincho'),
        ('caminhao', 'Caminhão'),
        ('utilitario', 'Utilitário'),
        ('outro', 'Outro'),
    ]

    brand = models.CharField(max_length=100, verbose_name='Marca')
    model = models.CharField(max_length=100, verbose_name='Modelo')
    plate = models.CharField(max_length=10, unique=True, verbose_name='Placa')
    renavam = models.CharField(max_length=11, unique=True, verbose_name='RENAVAM')
    year = models.PositiveIntegerField(verbose_name='Ano')
    color = models.CharField(max_length=50, blank=True, verbose_name='Cor')
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='guincho',
        verbose_name='Tipo',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options for Vehicle model."""

        ordering = ['brand', 'model']
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        """Return string representation of the vehicle."""
        return f'{self.brand} {self.model} — {self.plate}'
