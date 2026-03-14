"""Forms for the drivers app."""

from django import forms

from .models import Driver, DriverPayment

INPUT_CLASSES = (
    'w-full px-3 py-2.5 text-sm bg-white border border-gray-200 rounded-lg '
    'text-[#1a2c42] placeholder-[#6b7280] focus:outline-none focus:ring-2 '
    'focus:ring-[#e85d36]/30 focus:border-[#e85d36] transition-colors'
)
SELECT_CLASSES = (
    'w-full px-3 py-2.5 text-sm bg-white border border-gray-200 rounded-lg '
    'text-[#1a2c42] focus:outline-none focus:ring-2 '
    'focus:ring-[#e85d36]/30 focus:border-[#e85d36] transition-colors'
)
DATE_CLASSES = INPUT_CLASSES


class DriverForm(forms.ModelForm):
    """Form for creating and updating a Driver."""

    class Meta:
        """Meta options for DriverForm."""

        model = Driver
        fields = [
            'name',
            'document',
            'phone',
            'email',
            'cnh_number',
            'cnh_category',
            'cnh_expiration',
            'admission_date',
            'base_salary',
            'zip_code',
            'street',
            'number',
            'complement',
            'neighborhood',
            'city',
            'state',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Nome completo',
            }),
            'document': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '000.000.000-00',
            }),
            'phone': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '(00) 00000-0000',
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'email@exemplo.com',
            }),
            'cnh_number': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Número da CNH',
            }),
            'cnh_category': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'cnh_expiration': forms.DateInput(attrs={
                'class': DATE_CLASSES,
                'type': 'date',
            }),
            'admission_date': forms.DateInput(attrs={
                'class': DATE_CLASSES,
                'type': 'date',
            }),
            'base_salary': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '0,00',
                'step': '0.01',
            }),
            'zip_code': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '00000-000',
                'id': 'id_zip_code',
            }),
            'street': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Rua, Avenida...',
            }),
            'number': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Nº',
            }),
            'complement': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Apto, Sala...',
            }),
            'neighborhood': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Bairro',
            }),
            'city': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Cidade',
            }),
            'state': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'UF',
                'maxlength': '2',
            }),
        }

    def __init__(self, *args, **kwargs):
        """Initialize form and mark address fields as not required."""
        super().__init__(*args, **kwargs)
        address_fields = ['zip_code', 'street', 'number', 'complement', 'neighborhood', 'city', 'state']
        for field in address_fields:
            self.fields[field].required = False


class DriverPaymentForm(forms.ModelForm):
    """Form for registering a payment to a driver."""

    class Meta:
        """Meta options for DriverPaymentForm."""

        model = DriverPayment
        fields = ['amount', 'payment_date', 'description']
        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '0,00',
                'step': '0.01',
            }),
            'payment_date': forms.DateInput(attrs={
                'class': DATE_CLASSES,
                'type': 'date',
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Descrição do pagamento...',
                'rows': 3,
            }),
        }
