from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    """
    Backend de autenticacao por e-mail para CustomUser.

    Permite que o usuario faca login usando seu e-mail e senha,
    substituindo o comportamento padrao que utiliza username.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Autentica o usuario pelo campo email.

        Aceita o parametro 'username' para compatibilidade com o formulario
        padrao do Django, mas trata o valor como e-mail.
        """
        UserModel = get_user_model()
        email = kwargs.get('email', username)

        if email is None or password is None:
            return None

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None

    def get_user(self, user_id):
        """Retorna o usuario pelo ID ou None se nao existir."""
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
