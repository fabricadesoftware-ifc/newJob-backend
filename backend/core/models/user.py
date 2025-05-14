from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import uuid
from backend.files.models import Image, Document
from .state import State
from .city import City


# Validação de CNPJ
def validate_cnpj(value):
    if not value.isdigit() or len(value) != 14:
        raise ValidationError("O CNPJ deve ter exatamente 14 dígitos e conter apenas números.")

class User(AbstractUser):
    class FormationType(models.IntegerChoices):
        FUND_INC = 1, "Fundamental Incompleto "
        FUND_COMP = 2, "Fundamental Completo",
        MEDIO_INC = 3, "Médio Incompleto",
        MEDIO_COMP = 4, "Médio Completo",
        SUP_INC = 5, "Superior Incompleto"
        SUP_COMP = 6, "Superior Completo"
        MESTRE = 7, "Mestrado"
        DOUTOR = 8, "Doutorado"


    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        help_text=_("Sequência aleatória usada como identificador público."),
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    comorbidade = models.CharField(max_length=100, blank=True, null=True)
    formation = models.IntegerField(choices=FormationType.choices, default=FormationType.MEDIO_COMP)
    formation_place = models.CharField(max_length=120, null=True, blank=True)
    state = models.ForeignKey(
        State,
        related_name="stateUser",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    city = models.ForeignKey(
        City,
        related_name="cityUser",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    address =  models.CharField(max_length=80, null=True, blank=True)
    phone = models.CharField(
        max_length=31,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,1 5}$',
                message="O telefone deve ter entre 9 e 15 dígitos, podendo incluir o código do país."
            )
        ]
    )
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

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    EMAIL_FIELD = "email"

    def __str__(self):
        return self.name or self.username
