# Generated by Django 5.0.6 on 2024-06-24 05:34

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0003_book_meta_alter_store_polygon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='meta',
            field=models.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
    ]
