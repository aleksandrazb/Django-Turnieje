# Generated by Django 3.1.3 on 2021-07-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_turnieje', '0017_auto_20210701_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzytkownicy',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
