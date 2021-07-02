from django import forms
from ..models import Uzytkownicy


class RejestracjaForm(forms.ModelForm):

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RejestracjaForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = Uzytkownicy
        fields = [
            'login',
            'password',
            'email',
            'data_urodzenia'
        ]