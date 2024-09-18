from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from base.models.target_area_ennum import TargetAreaEnum
from django.utils.text import slugify
import secrets


# Create your models here.
class ProgramModel(DateTimeModel):

    target_area = models.CharField(max_length=10, choices=TargetAreaEnum.choices, default=TargetAreaEnum.ARM,
                                   verbose_name="Zone ciblée ")
    user = models.ForeignKey("user.CustomUserModel", on_delete=models.CASCADE,
                             verbose_name="Nom d'utilisateur ")
    exercices = models.ManyToManyField("exercise.ExerciseModel", verbose_name="Exercices ")
    starting = models.DateField(verbose_name="Date de début ")
    ending = models.DateField(verbose_name="Date de fin ")
    slug = models.SlugField(unique=True)

    def program_duration(self):
        duration = self.ending - self.starting
        return duration.days

    def __str__(self):
        return f"{self.user} - {self.program_duration()} jours, {self.target_area}"

    class Meta:
        verbose_name = "Programme"
        verbose_name_plural = "Programmes"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(secrets.token_urlsafe(8))

        super(ProgramModel, self).save(*args, **kwargs)