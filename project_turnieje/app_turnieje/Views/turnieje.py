from django.shortcuts import render, redirect
from ..forms import TurniejeForm
from ..models import Turnieje


def turnieje_view(request):
    print(request.user)
    turnieje = Turnieje.objects.all()

    data = {
        'turnieje': turnieje,
        'name': request.user,
        'title': 'Lista turniejów'
    }
    return render(request, 'lista_turniejow.html', data)


def turniej_create_view(request):
    print(request.user)
    form = TurniejeForm(request.POST or None)
    if form.is_valid():
        form.save()
    data = {
        'form': form,
        'name': request.user,
        'title': 'Stwórz turniej'
    }
    return render(request, 'stworz_turniej.html', data)


def usun_turniej_view(request, turniej_id):
    print(request.user)
    turnieje = Turnieje.objects.all()
    turniej = Turnieje.objects.get(id=turniej_id)
    turniej.delete()

    data = {
        'turnieje': turnieje,
        'name': request.user,
        'title': 'Usunięto'
    }
    return redirect(turnieje_view)