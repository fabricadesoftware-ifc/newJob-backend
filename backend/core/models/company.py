from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from .contractType import ContractType
from .local import Local
from backend.files.models import Image



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
    cnpj = models.CharField(
        max_length=14,
        unique=True,
        validators=[validate_cnpj],
        help_text="Digite um CNPJ válido com 14 dígitos."
    )
    email = models.EmailField(unique=True, help_text="Digite um email válido.")
    ramo = models.CharField(
        max_length=3,
        choices=BusinessArea.choices,
        help_text="Escolha o ramo de atuação da empresa.",
        blank=True,
        null=True
    )
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
    local = models.ForeignKey(Local, on_delete=models.CASCADE, blank=True, null=True)
    pessoa_de_contato = models.CharField(
        max_length=255,
        help_text="Digite o nome completo da pessoa de contato na empresa.",
        blank=True,
        null=True
    )    
    logo = models.ForeignKey(Image,  related_name="+",       
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,)
    

    def __str__(self):
        return self.name
