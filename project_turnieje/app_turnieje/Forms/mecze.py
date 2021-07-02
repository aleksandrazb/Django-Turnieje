from django import forms
from django.forms import TextInput
from ..models import Mecze


class MeczeForm(forms.ModelForm):
    id_turnieju = forms.CharField(disabled=True)

    class Meta:
        model = Mecze
        fields = [
            'id_turnieju',
            'faza',
            'id_gracza1',
            'id_gracza2',
            'wynik_gracza1',
            'wynik_gracza2',
            'wygrana'
        ]
