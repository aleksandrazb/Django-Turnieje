from django.shortcuts import render, redirect
from ..forms import TurniejeForm
from ..models import Turnieje, Uzytkownicy
from django.contrib.auth.decorators import login_required
import datetime
import pytz as pytz


@login_required(login_url="login")
def turnieje_view(request):
    print(request.user)
    turnieje = Turnieje.objects.filter(autor=request.user)
    data = {
        'turnieje': turnieje,
        'name': request.user,
        'title': 'Lista turniejów'
    }
    return render(request, 'lista_turniejow.html', data)


@login_required(login_url="login")
def turniej_create_view(request):
    print(request.user)
    init = {
        'autor': Uzytkownicy.objects.filter(login=request.user).first()
    }
    form = TurniejeForm(request.POST or None, initial=init)
    if form.is_valid():
        form.save()
        return redirect(turnieje_view)
    data = {
        'form': form,
        'name': request.user.login,
        'title': 'Stwórz turniej'
    }
    return render(request, 'stworz_turniej.html', data)


@login_required(login_url="login")
def usun_turniej_view(request, turniej_id):
    print(request.user)
    turniej = Turnieje.objects.get(id=turniej_id)
    teraz = datetime.datetime.now()
    teraz = pytz.utc.localize(teraz)
    if turniej.data_rozpoczecia > teraz:
        turniej.delete()
    return redirect(turnieje_view)
