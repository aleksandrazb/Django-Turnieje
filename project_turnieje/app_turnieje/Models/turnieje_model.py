from django.db import models
from django.urls import reverse


class Turnieje(models.Model):
    objects = ['id', 'nazwa', 'ilosc_graczy']
    id = models.AutoField(db_index=True, primary_key=True)
    nazwa = models.CharField(max_length=20)
    ilosc_graczy = models.IntegerField(choices=[(2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'),
                                                (14, '14'), (16, '16'), (18, '18'), (20, '20'), (22, '22'),
                                                (24, '24')])
    data_rozpoczecia = models.DateTimeField()
    autor = models.CharField(max_length=50, default="Anonymus")

    def get_absolute_url(self):
        return reverse('turniej_detail', kwargs={'pk': self.nazwa})

    def __str__(self):
        return str(self.nazwa)
