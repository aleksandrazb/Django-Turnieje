from django.db import models
from django.urls import reverse


class Uzytkownicy(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    nazwa = models.CharField(max_length=20)
    haslo = models.CharField(max_length=1024, blank=False, null=False)
    mail = models.CharField(max_length=100)
    data_urodzenia = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('uzytkownik_detail', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.nazwa)
