# Generated by Django 4.1.2 on 2022-10-17 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_social"),
    ]

    operations = [
        migrations.AlterModelOptions(name="social", options={"ordering": ["title"]},),
        migrations.AddField(
            model_name="social",
            name="link",
            field=models.URLField(blank=True, default=""),
        ),
    ]