from django.db import models
from django.urls import reverse


class Gracze(models.Model):
    objects = ['id', 'imie_nazwisko']
    id = models.AutoField(db_index=True, primary_key=True)
    imie_nazwisko = models.CharField(max_length=50, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('gracz_detail', kwargs={'pk': self.imie_nazwisko})

    def __str__(self):
        return str(self.imie_nazwisko)
