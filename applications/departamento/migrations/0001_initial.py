# Generated by Django 4.2.4 on 2023-09-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=20, unique=True, verbose_name='Nombre Corto')),
                ('annulate', models.BooleanField(default=False, verbose_name='Anulado')),
            ],
        ),
    ]
