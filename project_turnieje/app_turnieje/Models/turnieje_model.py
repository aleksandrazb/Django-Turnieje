from django.db import models
from django.urls import reverse


class Turnieje(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    nazwa = models.CharField(max_length=20)
    ilosc_graczy = models.IntegerField()
    data_rozpoczecia = models.DateTimeField()
    autor = models.CharField(max_length=20, default='Anonymus')

    def get_absolute_url(self):
        return reverse('turniej_detail', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.id)
