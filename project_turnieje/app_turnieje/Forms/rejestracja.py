from django import forms
from ..models import Uzytkownicy
from django.contrib.auth.models import BaseUserManager


class RejestracjaForm(forms.ModelForm):

    class Meta:
        model = Uzytkownicy
        fields = [
            'login',
            'password',
            'email',
            'data_urodzenia'
        ]