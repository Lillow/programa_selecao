# Generated by Django 5.1.2 on 2024-10-21 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0001_initial'),
        ('movements', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movements',
            new_name='Movement',
        ),
    ]