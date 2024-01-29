# Generated by Django 5.0.1 on 2024-01-28 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adquisicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presupuesto', models.CharField(max_length=255)),
                ('unidad', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('cantidad', models.IntegerField()),
                ('valor_unitario', models.FloatField()),
                ('valor_total', models.FloatField()),
                ('fecha_adquisicion', models.DateField()),
                ('proveedor', models.CharField(max_length=255)),
                ('documentacion', models.CharField(max_length=255)),
            ],
        ),
    ]
