# Generated by Django 4.2.1 on 2023-06-04 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Inquiry',
        ),
    ]