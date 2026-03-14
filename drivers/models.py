"""Models for the drivers app."""

from django.db import models


class Driver(models.Model):
    """Model representing a tow truck driver."""

    CNH_CATEGORIES = [
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    name = models.CharField(max_length=255, verbose_name='Nome')
    document = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Telefone')
    email = models.EmailField(blank=True, verbose_name='E-mail')
    cnh_number = models.CharField(max_length=20, unique=True, verbose_name='Número CNH')
    cnh_category = models.CharField(
        max_length=2,
        choices=CNH_CATEGORIES,
        verbose_name='Categoria CNH',
    )
    cnh_expiration = models.DateField(verbose_name='Validade CNH')
    admission_date = models.DateField(verbose_name='Data de Admissão')
    base_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Salário Base',
    )
    # Address
    zip_code = models.CharField(max_length=9, blank=True, verbose_name='CEP')
    street = models.CharField(max_length=255, blank=True, verbose_name='Rua')
    number = models.CharField(max_length=10, blank=True, verbose_name='Número')
    complement = models.CharField(max_length=100, blank=True, verbose_name='Complemento')
    neighborhood = models.CharField(max_length=100, blank=True, verbose_name='Bairro')
    city = models.CharField(max_length=100, blank=True, verbose_name='Cidade')
    state = models.CharField(max_length=2, blank=True, verbose_name='Estado')
    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options for Driver."""

        ordering = ['name']
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'

    def __str__(self):
        """Return string representation."""
        return self.name


class DriverPayment(models.Model):
    """Model representing a payment made to a driver."""

    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Motorista',
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Valor',
    )
    payment_date = models.DateField(verbose_name='Data do Pagamento')
    description = models.TextField(blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options for DriverPayment."""

        ordering = ['-payment_date']
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        """Return string representation."""
        return f'Pagamento {self.driver.name} - {self.payment_date}'
