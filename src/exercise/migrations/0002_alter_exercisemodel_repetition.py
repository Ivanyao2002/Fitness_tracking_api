# Generated by Django 5.1.1 on 2024-09-19 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisemodel',
            name='repetition',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Répétition '),
        ),
    ]
