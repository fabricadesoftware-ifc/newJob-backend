import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from backend.files.models import Image


class User(AbstractUser):
    first_name = None
    last_name = None

    public_id = models.CharField(
        max_length=255,
        default=uuid.uuid4(),
        unique=True,
        help_text="Random sequence to be used as a public identifier.",
    )
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
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
    # objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    EMAIL_FIELD = "email"

    # def save(self, *args, **kwargs):
    #     self.username = self.email
    #     super(User, self).save(*args, **kwargs)
