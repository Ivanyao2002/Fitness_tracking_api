from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('sets', models.PositiveIntegerField(verbose_name='Séries par semaine')),
                ('starting', models.TimeField(verbose_name='Heure de début ')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Programme',
                'verbose_name_plural': 'Programmes',
            },
        ),
        migrations.CreateModel(
            name='RoutineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=180)),
                ('level', models.CharField(choices=[('Beginer', 'Débutant'), ('Intermediaire', 'Intermediaire'), ('Avance', 'Avancé')], default='Beginer', max_length=15, verbose_name='Niveau ')),
                ('target_area', models.CharField(choices=[('Bras', 'Bras'), ('Poitrine', 'Poitrine'), ('Jambe', 'Jambe'), ('Abdos', 'Abdos'), ('Epaule', 'Epaule')], default='Bras', max_length=10, verbose_name='Zone ciblée ')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Routine',
                'verbose_name_plural': 'Routines',
            },
        ),
    ]
