# Generated by Django 3.1.3 on 2021-06-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_turnieje', '0004_turnieje_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnieje',
            name='autor',
            field=models.CharField(default='', max_length=20),
        ),
    ]
