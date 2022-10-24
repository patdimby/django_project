# Generated by Django 4.1.2 on 2022-10-24 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0012_alter_post_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="banner",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="posts.localuser",
            ),
        ),
    ]