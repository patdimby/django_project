# Generated by Django 4.1.2 on 2022-10-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0006_banner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Info",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("phone", models.CharField(max_length=50)),
                ("adresse", models.CharField(max_length=50)),
                ("mail", models.EmailField(max_length=254)),
                ("website", models.URLField()),
            ],
        ),
    ]
