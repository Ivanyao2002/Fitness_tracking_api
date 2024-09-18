from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

class TargetAreaEnum(models.TextChoices):
    
    ARM  = "Bras", _("Bras")
    CHEST  = "Poitrine", _("Poitrine")
    LEG  = "Jambe", _("Jambe")
    ABS  = "Abdos", _("Abdos")
    SHOULDER  = "Epaule", _("Epaule")