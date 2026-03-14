"""Forms for the customers app."""

from django import forms

from .models import Customer

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


class CustomerForm(forms.ModelForm):
    """
    ModelForm for creating and updating Customer instances.

    Applies Design System widget classes and ensures address fields
    are optional at the form level, consistent with model blank=True.
    """

    class Meta:
        """Meta options for CustomerForm."""

        model = Customer
        fields = [
            'type',
            'name',
            'document',
            'phone',
            'email',
            'zip_code',
            'street',
            'number',
            'complement',
            'neighborhood',
            'city',
            'state',
        ]
        widgets = {
            'type': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Nome completo ou razão social',
            }),
            'document': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'CPF ou CNPJ',
            }),
            'phone': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '(00) 00000-0000',
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'email@exemplo.com',
            }),
            'zip_code': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '00000-000',
                'id': 'id_zip_code',
            }),
            'street': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Rua, Avenida...',
                'id': 'id_street',
            }),
            'number': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Nº',
                'id': 'id_number',
            }),
            'complement': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Apto, Bloco...',
            }),
            'neighborhood': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Bairro',
                'id': 'id_neighborhood',
            }),
            'city': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Cidade',
                'id': 'id_city',
            }),
            'state': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'UF',
                'maxlength': '2',
                'id': 'id_state',
            }),
        }

    def __init__(self, *args, **kwargs):
        """Initialize form and mark address fields as not required."""
        super().__init__(*args, **kwargs)
        address_fields = [
            'zip_code', 'street', 'number', 'complement',
            'neighborhood', 'city', 'state',
        ]
        for field_name in address_fields:
            self.fields[field_name].required = False
