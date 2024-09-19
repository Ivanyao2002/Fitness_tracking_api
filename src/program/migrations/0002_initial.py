

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercise', '0001_initial'),
        ('program', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='programmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="Nom d'utilisateur "),
        ),
        migrations.AddField(
            model_name='routinemodel',
            name='exercices',
            field=models.ManyToManyField(to='exercise.exercisemodel', verbose_name='Exercices '),
        ),
        migrations.AddField(
            model_name='programmodel',
            name='routine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.routinemodel', verbose_name='Nom de la routine '),
        ),
    ]
