from django import forms

from .models import Vehicle

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


class VehicleForm(forms.ModelForm):
    """Form for creating and updating a Vehicle instance."""

    class Meta:
        """Meta options for VehicleForm."""

        model = Vehicle
        fields = ['brand', 'model', 'plate', 'renavam', 'year', 'color', 'type']
        widgets = {
            'brand': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ex: Ford',
            }),
            'model': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ex: F-4000',
            }),
            'plate': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ex: ABC-1234',
            }),
            'renavam': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '11 dígitos',
            }),
            'year': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'min': 1990,
                'max': 2030,
                'placeholder': 'Ex: 2022',
            }),
            'color': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ex: Branco',
            }),
            'type': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
        }
