from django.db import models
from django.urls import reverse


class Mecze(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    id_turnieju = models.ForeignKey('Turnieje', on_delete=models.CASCADE)
    faza = models.IntegerField()
    id_gracza1 = models.ForeignKey('Gracze', on_delete=models.CASCADE)
    id_gracza2 = models.ForeignKey('Gracze', on_delete=models.CASCADE)
    wynik_gracza1 = models.IntegerField()
    wynik_gracza2 = models.IntegerField()
    wygrana = models.ForeignKey('Gracze', on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('mecz_detail', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.id)
