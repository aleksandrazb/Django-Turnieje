import datetime
import pytz as pytz
from django.shortcuts import render, redirect
from ..forms import GraczeForm
from ..models import Gracze
from ..models import Turnieje


def gracze_view(request):
    print(request.user)
    gracze = Gracze.objects.all()

    data = {
        'gracze': gracze,
        'name': request.user,
        'title': 'Lista graczy'
    }
    return render(request, 'lista_graczy.html', data)


def dodaj_gracza_view(request):
    print(request.user)
    form = GraczeForm(request.POST or None)

    if form.is_valid():
        form.save()
    data = {
        'form': form,
        'name': request.user,
        'title': 'Dodaj gracza'
    }
    return render(request, 'dodaj_gracza.html', data)


def usun_gracza_view(request, gracz_id, turniej_id):
    print(request.user)
    print("USUN GRACZA")

    gracze = Gracze.objects.all()
    gracz = Gracze.objects.get(id=gracz_id)

    teraz = datetime.datetime.now()
    teraz = pytz.utc.localize(teraz)
    turniej = Turnieje.objects.filter(id=turniej_id, data_rozpoczecia__gt=teraz)
    print("turniej")
    print(turniej)
    print("gracz")
    print(gracz)
    if turniej:
        gracz.delete()

    data = {
        'gracze': gracze,
        'name': request.user,
        'title': 'Dodaj gracza'
    }
    return redirect(gracze_view)
