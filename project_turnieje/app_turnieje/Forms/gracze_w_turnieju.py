from django import forms
from ..models import GraczeWTurnieju


class GraczeWTurniejuForm(forms.ModelForm):
    class Meta:
        model = GraczeWTurnieju
        fields = [
            'turniej',
            'gracz'
        ]
