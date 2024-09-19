from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from django.utils.text import slugify
import secrets


# Create your models here.
class ProgressModel(DateTimeModel):

    user = models.ForeignKey("user.CustomUserModel", on_delete=models.CASCADE,
                             verbose_name="Nom d'utilisateur ")
    program = models.ForeignKey("program.ProgramModel", on_delete=models.CASCADE, verbose_name="Programme", null=True, blank=True)
    exercise = models.ForeignKey("exercise.ExerciseModel", on_delete=models.CASCADE, verbose_name="Exercice")
    date = models.DateField(auto_now_add=True, verbose_name="Date de la session")
    performance_notes = models.FloatField()
    slug = models.SlugField(unique=True)


    def __str__(self):
        return f"Progrès de {self.user} sur {self.exercise} le {self.date}"

    class Meta:
        verbose_name = "Progrès"
        verbose_name_plural = "Progrès"
        ordering = ['-date']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(secrets.token_urlsafe(8))

        super(ProgressModel, self).save(*args, **kwargs)


