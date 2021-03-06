# Generated by Django 3.1.7 on 2021-03-22 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beneficio', '0006_dia_de_pagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='limiteContratacaoPadrao',
            field=models.PositiveIntegerField(default=270),
        ),
        migrations.AddField(
            model_name='dia_de_pagamento',
            name='profissional',
            field=models.ForeignKey(db_column='nomeCompleto', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='nomeCompleto2', to='beneficio.profissional'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contrato',
            name='limiteContratacao',
            field=models.PositiveIntegerField(default=270),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='tempoInicial',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dia_de_pagamento',
            name='salario',
            field=models.ForeignKey(db_column='salario', on_delete=django.db.models.deletion.CASCADE, to='beneficio.profissional', verbose_name='Salario'),
        ),
    ]
