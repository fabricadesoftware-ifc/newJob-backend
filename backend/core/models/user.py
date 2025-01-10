from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import uuid
from backend.files.models import Image, Document
from .local import Local


# Validação de CNPJ
def validate_cnpj(value):
    if not value.isdigit() or len(value) != 14:
        raise ValidationError("O CNPJ deve ter exatamente 14 dígitos e conter apenas números.")


# Gerenciador customizado para o User
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """Cria, salva e retorna um novo usuário."""
        if not email:
            raise ValueError("Os usuários devem ter um endereço de email.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Cria, salva e retorna um superusuário."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser precisa ter is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser precisa ter is_superuser=True.")

        return self.create_user(email=email, password=password, username=username, **extra_fields)


# Modelo Base para usuários e empresas
class User(AbstractUser):
    class UserType(models.TextChoices):
        STANDARD = "STANDARD", _("Usuário Padrão")
        COMPANY = "COMPANY", _("Empresa")

    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        help_text=_("Sequência aleatória usada como identificador público."),
    )
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    comorbidade = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(
        max_length=31,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="O telefone deve ter entre 9 e 15 dígitos, podendo incluir o código do país."
            )
        ]
    )
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True, blank=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    avatar = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        related_name="+",
        blank=True,
        null=True,
        default=None,
    )
    curriculo = models.ForeignKey(
        Document,
        on_delete=models.SET_NULL,
        related_name="+",
        blank=True,
        null=True,
        default=None,
    )
    description = models.TextField(blank=True, null=True)
    user_type = models.CharField(
        max_length=8,
        choices=UserType.choices,
        default=UserType.STANDARD,
        help_text="Define se o usuário é padrão ou uma empresa."
    )

    cnpj = models.CharField(
        max_length=14,
        unique=True,
        validators=[validate_cnpj],
        blank=True,
        null=True,
        help_text="Digite um CNPJ válido com 14 dígitos."
    )
    fantasy_name = models.CharField(max_length=255, blank=True, null=True)
    ramo = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ramo de atuação da empresa."
    )
    pessoa_de_contato = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Nome completo da pessoa de contato na empresa."
    )
    logo = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        related_name="company_logos",
        null=True,
        blank=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    EMAIL_FIELD = "email"

    def save(self, *args, **kwargs):
        if self.cnpj:
            self.user_type = self.UserType.COMPANY
        else:
            self.user_type = self.UserType.STANDARD
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name or self.username
