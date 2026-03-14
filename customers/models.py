"""Models for the customers app."""

from django.db import models


class Customer(models.Model):
    """
    Represents a client, either an individual (PF) or a legal entity (PJ).

    Stores personal/company data, contact info, and full address.
    """

    TYPE_PF = 'PF'
    TYPE_PJ = 'PJ'
    TYPE_CHOICES = [
        (TYPE_PF, 'Pessoa Física'),
        (TYPE_PJ, 'Pessoa Jurídica'),
    ]

    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=TYPE_PF,
        verbose_name='Tipo',
    )
    name = models.CharField(max_length=255, verbose_name='Nome')
    document = models.CharField(
        max_length=18,
        unique=True,
        verbose_name='CPF / CNPJ',
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Telefone',
    )
    email = models.EmailField(blank=True, verbose_name='E-mail')

    # Address
    zip_code = models.CharField(
        max_length=9,
        blank=True,
        verbose_name='CEP',
    )
    street = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Logradouro',
    )
    number = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='Número',
    )
    complement = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Complemento',
    )
    neighborhood = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Bairro',
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Cidade',
    )
    state = models.CharField(
        max_length=2,
        blank=True,
        verbose_name='UF',
    )

    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options for Customer."""

        ordering = ['name']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        """Return the customer name as string representation."""
        return self.name
