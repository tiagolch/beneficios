# Generated by Django 3.1.7 on 2021-03-21 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficio', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('nome', 'codigo')},
        ),
    ]
