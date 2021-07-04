from django.db import models
from django.urls import reverse
from django.conf import settings


class Turnieje(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    nazwa = models.CharField(max_length=20)
    #ilosc_graczy = models.IntegerField(choices=[(1, '2'), (2, '4'), (3, '6'), (4, '8'), (5, '10'), (6, '12'), (7, '14'),
    #                                            (8, '16'), (9, '18'), (10, '20'), (11, '22'), (12, '24')])
    ilosc_graczy = models.IntegerField(choices=[(2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'),
                                                (14, '14'), (16, '16'), (18, '18'), (20, '20'), (22, '22'),
                                                (24, '24')])
    data_rozpoczecia = models.DateTimeField()
    #autor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    autor = models.CharField(max_length=50, default="Anonymus")

    def get_absolute_url(self):
        return reverse('turniej_detail', kwargs={'pk': self.nazwa})

    def __str__(self):
        return str(self.nazwa)
