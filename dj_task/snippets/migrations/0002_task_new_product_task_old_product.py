# Generated by Django 4.2.1 on 2023-11-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("snippets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="new_product",
            field=models.FilePathField(default=""),
        ),
        migrations.AddField(
            model_name="task",
            name="old_product",
            field=models.FilePathField(default=""),
        ),
    ]