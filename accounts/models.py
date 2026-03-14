from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    """Manager para CustomUser com autenticacao por e-mail."""

    def create_user(self, email, password=None, **extra_fields):
        """Cria e retorna um usuario com e-mail e senha."""
        if not email:
            raise ValueError('O campo e-mail e obrigatorio.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Cria e retorna um superusuario com e-mail e senha."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuario deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuario deve ter is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de usuario personalizado com autenticacao por e-mail.

    Substitui o campo username pelo campo email como identificador
    principal de autenticacao.
    """

    email = models.EmailField(unique=True, verbose_name='E-mail')
    first_name = models.CharField(max_length=150, blank=True, verbose_name='Nome')
    last_name = models.CharField(max_length=150, blank=True, verbose_name='Sobrenome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_staff = models.BooleanField(default=False, verbose_name='Equipe')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        """Retorna a representacao em string do usuario."""
        return self.email

    def get_full_name(self):
        """Retorna o nome completo do usuario."""
        return f'{self.first_name} {self.last_name}'.strip()

    def get_short_name(self):
        """Retorna o primeiro nome do usuario."""
        return self.first_name
