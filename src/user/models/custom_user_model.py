from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
import secrets


# Create your models here.
class CustomUserModel(AbstractUser):
    weight = models.PositiveIntegerField(verbose_name="Poids ", validators=[MinValueValidator(30), MaxValueValidator(300)])
    size = models.PositiveIntegerField(verbose_name="Taille ", validators=[MinValueValidator(100), MaxValueValidator(250)])
    age = models.PositiveIntegerField(verbose_name="Age ", validators=[MinValueValidator(16), MaxValueValidator(90)])
    numbers = models.CharField(max_length=15, verbose_name="Numéros de téléphone ")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(secrets.token_urlsafe(8))  # Génère une chaîne aléatoire de 8 caractères

        super(CustomUserModel, self).save(*args, **kwargs)
