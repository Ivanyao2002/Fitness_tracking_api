# Generated by Django 5.1.1 on 2024-09-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmodel',
            name='level',
            field=models.CharField(choices=[('Beginer', 'Débutant'), ('Intermediaire', 'Intermediaire'), ('Avance', 'Avancé')], default='Beginer', max_length=15, verbose_name='Niveau '),
        ),
    ]
