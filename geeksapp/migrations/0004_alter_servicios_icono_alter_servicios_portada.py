# Generated by Django 4.2.4 on 2024-05-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("geeksapp", "0003_alter_servicios_options_servicios_portada"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicios",
            name="icono",
            field=models.ImageField(upload_to="iconos/", verbose_name="Icono"),
        ),
        migrations.AlterField(
            model_name="servicios",
            name="portada",
            field=models.ImageField(
                null=True, upload_to="portadas/", verbose_name="Portada"
            ),
        ),
    ]