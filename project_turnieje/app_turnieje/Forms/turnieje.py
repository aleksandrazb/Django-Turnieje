from django import forms
from ..models import Turnieje


class TurniejeForm(forms.ModelForm):
    data_rozpoczecia = forms.DateTimeField(input_formats=["%d.%m.%Y %H:%M", "%d.%m.%Y %H.%M"])

    class Meta:
        model = Turnieje
        fields = [
            'nazwa',
            'ilosc_graczy',
            'data_rozpoczecia',
            'autor'
        ]
