

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercise', '0001_initial'),
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date de la session')),
                ('performance_notes', models.FloatField()),
                ('slug', models.SlugField(unique=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.exercisemodel', verbose_name='Exercice')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='program.programmodel', verbose_name='Programme')),
            ],
            options={
                'verbose_name': 'Progrès',
                'verbose_name_plural': 'Progrès',
                'ordering': ['-date'],
            },
        ),
    ]
