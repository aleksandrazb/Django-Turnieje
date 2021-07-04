from django import forms
from ..models import GraczeWTurnieju


class GraczeWTurniejuForm(forms.ModelForm):
    #turniej = forms.ChoiceField(disabled=True)

    class Meta:
        model = GraczeWTurnieju
        fields = [
            'turniej',
            'gracz'
        ]