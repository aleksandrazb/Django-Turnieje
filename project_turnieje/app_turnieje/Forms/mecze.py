from django import forms
from django.forms import TextInput
from django.utils.datastructures import MultiValueDict

from ..models import Mecze


class MeczeForm(forms.ModelForm):
    #id_turnieju = forms.CharField(disabled=True)

    def __init__(self, data, **kwargs):
        initial = kwargs.get('initial', {})
        data = MultiValueDict({**{k: [v] for k, v in initial.items()}, **data})
        super().__init__(data, **kwargs)

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
