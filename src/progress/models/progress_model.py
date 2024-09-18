from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from django.utils.text import slugify
import secrets


# Create your models here.
class ProgressModel(DateTimeModel):

    user = models.ForeignKey("user.CustomUserModel", on_delete=models.CASCADE,
                             verbose_name="Nom d'utilisateur ")
    program = models.ForeignKey("program.ProgramModel", on_delete=models.CASCADE,
                            verbose_name="Programme ")
    date = models.DateField()
    performance_notes = models.TextField(verbose_name="Performances ")
    slug = models.SlugField(unique=True)


    def __str__(self):
        return f"{self.user} - {self.program}"

    class Meta:
        verbose_name = "Progrès"
        verbose_name_plural = "Progrès"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(secrets.token_urlsafe(8))

        super(ProgressModel, self).save(*args, **kwargs)