# Generated by Django 4.2.4 on 2024-05-17 06:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("geeksapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicios",
            name="slug",
            field=models.SlugField(
                editable=False, max_length=350, null=True, unique=True
            ),
        ),
    ]
