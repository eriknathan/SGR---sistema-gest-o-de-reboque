from django.contrib.auth.views import LoginView

from .forms import EmailAuthenticationForm


class CustomLoginView(LoginView):
    """
    View de login personalizada que utiliza autenticacao por e-mail.

    Herda de LoginView do Django e substitui o formulario padrao
    pelo EmailAuthenticationForm.
    """

    form_class = EmailAuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
