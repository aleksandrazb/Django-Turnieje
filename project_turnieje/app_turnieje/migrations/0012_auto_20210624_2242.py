# Generated by Django 3.1.3 on 2021-06-24 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_turnieje', '0011_auto_20210624_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gracze',
            old_name='id_gracza',
            new_name='id',
        ),
    ]
