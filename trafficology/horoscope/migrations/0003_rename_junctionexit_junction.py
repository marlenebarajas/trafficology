# Generated by Django 5.0.1 on 2024-01-15 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0002_rename_junctions_junctionexit'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Junctionexit',
            new_name='Junction',
        ),
    ]
