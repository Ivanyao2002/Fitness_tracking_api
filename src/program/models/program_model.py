from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from base.models.level_ennum import LevelEnum
from django.utils.text import slugify
import secrets


# Create your models here.
class ProgramModel(DateTimeModel):

    user = models.ForeignKey("user.CustomUserModel", on_delete=models.CASCADE,
                             verbose_name="Nom d'utilisateur ")
    level = models.CharField(max_length=15, choices=LevelEnum.choices, default=LevelEnum.BEGINER,
                             verbose_name="Niveau ")
    routine = models.ManyToManyField("program.RoutineModel", verbose_name="Nom de la routine ")
    sets = models.PositiveIntegerField(verbose_name="Séries par semaine")
    starting = models.TimeField(verbose_name="Heure de début ")
    slug = models.SlugField(unique=True)

    @property
    def program_duration(self):
        if self.ending < self.starting:
            duration = self.ending - self.starting
            return duration.days
        return 0

    def __str__(self):
        return f"{self.user} - {self.routine}"

    class Meta:
        verbose_name = "Programme"
        verbose_name_plural = "Programmes"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(secrets.token_urlsafe(8))

        super(ProgramModel, self).save(*args, **kwargs)