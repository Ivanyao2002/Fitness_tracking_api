from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

class LevelEnum(models.TextChoices):
    
    BEGINER = "Beginer", _("Débutant")
    INTERMEDIATE = "Intermediaire", _("Intermediaire")
    ADVANCED = "Avance", _("Avancé")