# Generated by Django 3.1.3 on 2021-06-24 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_turnieje', '0009_auto_20210624_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gracze',
            old_name='id',
            new_name='id_gracza',
        ),
        migrations.AlterField(
            model_name='gracze',
            name='id_turnieju',
            field=models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.CASCADE, to='app_turnieje.turnieje'),
        ),
    ]