# Generated by Django 3.2 on 2022-08-25 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Address',
            new_name='Addresses',
        ),
    ]
