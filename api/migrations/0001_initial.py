# Generated by Django 5.1.2 on 2024-10-28 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('genero_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_genero', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usuario_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=255)),
                ('fk_genero', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.genero')),
            ],
            options={
                'db_table': 'Usuarios',
            },
        ),
    ]
