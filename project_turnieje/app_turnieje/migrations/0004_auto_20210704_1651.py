# Generated by Django 3.1.3 on 2021-07-04 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_turnieje', '0003_graczewturnieju'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecze',
            name='id_gracza1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gracz1', to='app_turnieje.gracze'),
        ),
        migrations.AlterField(
            model_name='mecze',
            name='id_gracza2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gracz2', to='app_turnieje.gracze'),
        ),
    ]
