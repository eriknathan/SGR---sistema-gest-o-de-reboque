from django.contrib.auth.forms import AuthenticationForm
from django import forms


class EmailAuthenticationForm(AuthenticationForm):
    """
    Formulario de autenticacao que substitui o campo username por email.

    Exibe labels em portugues (pt-BR) e valida o usuario pelo campo email.
    """

    username = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'autofocus': True,
            'placeholder': 'seu@email.com',
            'class': 'w-full',
        }),
    )

    password = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'placeholder': '••••••••',
            'class': 'w-full',
        }),
    )

    error_messages = {
        'invalid_login': (
            'E-mail ou senha incorretos. Verifique os dados e tente novamente.'
        ),
        'inactive': 'Esta conta esta inativa.',
    }
