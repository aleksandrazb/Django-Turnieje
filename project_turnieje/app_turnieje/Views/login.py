from django.shortcuts import render
from ..forms import RejestracjaForm


def register_user(request): # TODO: logowanie i wylogowywanie i przydział czynności
    print(request.user)
    form = RejestracjaForm(request.POST or None)

    if form.is_valid():
        form.save()

    data = {
        'form': form,
        'name': request.user,
        'title': 'Rejestracja'
    }
    return render(request, 'rejestracja.html', data)
