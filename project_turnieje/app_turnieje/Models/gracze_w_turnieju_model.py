from django.db import models
from django.urls import reverse


class GraczeWTurnieju(models.Model):
    objects = ['id', 'turniej', 'gracz']
    id = models.AutoField(db_index=True, primary_key=True)
    turniej = models.ForeignKey('Turnieje', on_delete=models.CASCADE)
    gracz = models.ForeignKey('Gracze', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('gracz_detail', kwargs={'pk': [self.gracz, self.turniej]})

    def __str__(self):
        return str(self.gracz)
