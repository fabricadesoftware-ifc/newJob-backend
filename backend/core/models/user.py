import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _  # Para tradução
from backend.files.models import Image


class UserManager(BaseUserManager):
    """Manager para usuários."""

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """Cria, salva e retorna um novo usuário."""
        if not email:
            raise ValueError("Os usuários devem ter um endereço de email.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Cria, salva e retorna um superusuário."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractUser):
    first_name = None
    last_name = None

    public_id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True,
        help_text=_("Sequência aleatória usada como identificador público."),
    )
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(null=True, max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=31, blank=True)
    linkedin = models.URLField(null=True)
    profile_title = models.CharField(max_length=255, null=True)
    profile_description = models.TextField(null=True)
    reset_code = models.CharField(max_length=6, null=True, blank=True)
    avatar = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name="+",
        blank=True,
        null=True,
        default=None,
    )
    passage_id = models.UUIDField(
        default=uuid.uuid4(), 
        unique=True,
        verbose_name=_("ID de passagem"),
        help_text=_("Identificador de passagem")
    )
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    EMAIL_FIELD = "email"

    # def save(self, *args, **kwargs):
    #     self.username = self.email
    #     super(User, self).save(*args, **kwargs)
