from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel
from base.models.target_area_ennum import TargetAreaEnum
from base.models.level_ennum import LevelEnum
from django.utils.text import slugify
import secrets


# Create your models here.
class RoutineModel(NamedDateTimeModel):
    level = models.CharField(max_length=15, choices=LevelEnum.choices, default=LevelEnum.BEGINER,
                             verbose_name="Niveau ")
    target_area = models.CharField(max_length=10, choices=TargetAreaEnum.choices, default=TargetAreaEnum.ARM,
                                   verbose_name="Zone ciblée ")

    exercices = models.ManyToManyField("exercise.ExerciseModel", verbose_name="Exercices ")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name} - {self.level} jours, {self.target_area}"

    class Meta:
        verbose_name = "Routine"
        verbose_name_plural = "Routines"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(secrets.token_urlsafe(8))

        super(RoutineModel, self).save(*args, **kwargs)