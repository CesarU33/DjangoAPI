# Generated by Django 5.1.2 on 2024-10-18 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_generos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Generos',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
