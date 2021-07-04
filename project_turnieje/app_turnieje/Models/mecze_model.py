from django.db import models
from django.urls import reverse


class Mecze(models.Model):
    objects = ['id', 'id_turnieju', 'faza', 'id_gracza1', 'id_gracza2', 'wynik_gracza1', 'wynik_gracza2', 'wygrana']
    id = models.AutoField(db_index=True, primary_key=True)
    id_turnieju = models.ForeignKey('Turnieje', on_delete=models.CASCADE)
    faza = models.IntegerField()
    id_gracza1 = models.ForeignKey('Gracze', related_name='gracz1', on_delete=models.CASCADE, blank=True, null=True)
    id_gracza2 = models.ForeignKey('Gracze', related_name='gracz2', on_delete=models.CASCADE, blank=True, null=True)
    wynik_gracza1 = models.IntegerField(blank=True, null=True)
    wynik_gracza2 = models.IntegerField(blank=True, null=True)
    wygrana = models.ForeignKey('Gracze', related_name='zwyciezca', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('mecz_detail', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.id)
