# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-11-13 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planilla', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salario',
            name='bonoAntig',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Bono de Antiguedad'),
        ),
        migrations.AlterField(
            model_name='salario',
            name='bonoProduccion',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Bono por Produccion'),
        ),
        migrations.AlterField(
            model_name='salario',
            name='haberBase',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Haber Base'),
        ),
        migrations.AlterField(
            model_name='salario',
            name='horasExtra',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nº Horas Extra'),
        ),
        migrations.AlterField(
            model_name='salario',
            name='montoHorasExtra',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Monto por Horas Extra'),
        ),
        migrations.AlterField(
            model_name='salario',
            name='otrosBonos',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Otros Bonos'),
        ),
        migrations.AlterField(
            model_name='salario',
            name='otrosDescuentos',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Otros Descuentos'),
        ),
        migrations.AlterField(
            model_name='salario',
            name='porcAFP',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Porcentaje descuento AFP'),
        ),
        migrations.AlterField(
            model_name='salario',
            name='porcISSS',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Porcentaje descuento ISSS'),
        ),
        migrations.AlterField(
            model_name='salario',
            name='sueldoBruto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Sueldo Bruto'),
        ),
        migrations.AlterField(
            model_name='salario',
            name='sueldoNeto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Sueldo Neto'),
        ),
    ]
