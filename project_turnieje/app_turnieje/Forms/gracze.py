from django import forms
from ..models import Gracze


class GraczeForm(forms.ModelForm):
    class Meta:
        model = Gracze
        fields = [
            'imie_nazwisko'
        ]