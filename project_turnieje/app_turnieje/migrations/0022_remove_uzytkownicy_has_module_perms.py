# Generated by Django 3.1.3 on 2021-07-01 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_turnieje', '0021_uzytkownicy_has_module_perms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uzytkownicy',
            name='has_module_perms',
        ),
    ]
