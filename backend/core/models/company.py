from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import BaseBackend
from .local import Local
from django.contrib.auth.hashers import make_password
from backend.files.models import Image
from .state import State
from .city import City
from .user import User
# class CompanyBackend(BaseBackend):
#     def authenticate(self, request, email=None, password=None):
#         try:
#             company = Company.objects.get(email=email)
#             if company and check_password(password, company.password):
#                 return company
#         except Company.DoesNotExist:
#             return None

def validate_cnpj(value):
    if not value.isdigit() or len(value) != 14:
        raise ValidationError("O CNPJ deve ter exatamente 14 dígitos e conter apenas números.")


class Company(models.Model):
    class BusinessArea(models.TextChoices):
        TECNOLOGIA = "TEC", "Tecnologia"
        FINANCEIRO = "FIN", "Financeiro"
        SAUDE = "SAU", "Saúde"
        EDUCACAO = "EDU", "Educação"
        COMERCIO = "COM", "Comércio"
        OUTRO = "OUT", "Outro"
    name = models.CharField(max_length=255)
    fantasy_name = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(max_length=1500, default="Esta empresa não possuí descrição ainda.")
    owner_user = models.ForeignKey(
        User,
        related_name="user",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    cnpj = models.CharField(
        max_length=14,
        unique=True,
        validators=[validate_cnpj],
        help_text="Digite um CNPJ válido com 14 dígitos."
    )
    email = models.EmailField(unique=True, help_text="Digite um email válido.")
    # password = models.CharField(max_length=128, help_text="Senha da empresa (hash).")
    reset_code = models.CharField(max_length=6, null=True, blank=True)
    telefone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="O telefone deve ter entre 9 e 15 dígitos, podendo incluir o código do país."
            )
        ],
        help_text="Digite um número de telefone válido, incluindo o código do país, se necessário.",
        blank=True,
        null=True
    )
    state = models.ForeignKey(
        State,
        related_name="stateComp",
        on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        City,
        related_name="cityComp",
        on_delete=models.CASCADE
    )
    address =  models.CharField(max_length=80, null=True, blank=True)
    logo = models.ForeignKey(Image,  related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,)


    def __str__(self):
        return self.name
