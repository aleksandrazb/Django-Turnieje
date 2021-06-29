from django.db import models
from django.urls import reverse


class Gracze(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50, blank=False, null=False)
    id_turnieju = models.ForeignKey('Turnieje', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('gracz_detail', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.id)
