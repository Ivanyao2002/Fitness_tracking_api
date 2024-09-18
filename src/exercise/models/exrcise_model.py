from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel
from base.models.target_area_ennum import TargetAreaEnum
from base.models.level_ennum import LevelEnum
from django.utils.text import slugify
import secrets


# Create your models here.
class ExerciseModel(NamedDateTimeModel):
    level = models.CharField(max_length=10, choices=LevelEnum.choices, default=LevelEnum.BEGINER,
                             verbose_name="Niveau ")
    target_area = models.CharField(max_length=10, choices=TargetAreaEnum.choices, default=TargetAreaEnum.ARM,
                                   verbose_name="Zone ciblée ")
    duration = models.PositiveIntegerField(verbose_name="Durée ", blank=True)
    repetition = models.PositiveIntegerField(verbose_name="Répétition ", blank=True)
    description = models.TextField(verbose_name="Description ")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name} - {self.level}"

    class Meta:
        verbose_name = "Exercice"
        verbose_name_plural = "Exercices"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(secrets.token_urlsafe(8))

        super(ExerciseModel, self).save(*args, **kwargs)
