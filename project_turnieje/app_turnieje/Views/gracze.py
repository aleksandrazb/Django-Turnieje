import datetime
import pytz as pytz
from django.shortcuts import render, redirect
from ..forms import GraczeForm
from ..models import Gracze
from ..models import Turnieje
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def gracze_view(request):
    print(request.user)
    gracze = Gracze.objects.all()

    data = {
        'gracze': gracze,
        'name': request.user,
        'title': 'Lista graczy'
    }
    return render(request, 'lista_graczy.html', data)


@login_required(login_url="login")
def dodaj_gracza_view(request):
    print(request.user)
    form = GraczeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(gracze_view)
    data = {
        'form': form,
        'name': request.user,
        'title': 'Dodaj gracza'
    }
    return render(request, 'dodaj_gracza.html', data)


@login_required(login_url="login")
def usun_gracza_view(request, gracz_id):
    print(request.user)
    print("USUN GRACZA")
    gracz = Gracze.objects.get(id=gracz_id)
    print("gracz")
    print(gracz)
    gracz.delete()

    return redirect(gracze_view)
