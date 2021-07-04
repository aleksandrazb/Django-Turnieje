from django.shortcuts import render, redirect
from ..forms import MeczeForm
from ..models import Mecze, Turnieje, GraczeWTurnieju
from django.contrib.auth.decorators import login_required
import datetime
import pytz as pytz


@login_required(login_url="login")
def mecze_view(request, turniej_id):
    print(request.user)
    mecze = Mecze.objects.filter(id_turnieju=turniej_id)
    turnieje = Turnieje.objects.filter(id=turniej_id)
    turniej = Turnieje.objects.get(id=turniej_id)
    print(turnieje)

    gracze_w_turnieju = GraczeWTurnieju.objects.filter(turniej=turniej)
    print(gracze_w_turnieju)

    teraz = datetime.datetime.now()
    teraz = pytz.utc.localize(teraz)
    if turniej.data_rozpoczecia > teraz:
        data = {
            'mecze': mecze,
            'gracze_w_turnieju': gracze_w_turnieju,
            'turnieje': turnieje,
            'turniej_id': turniej_id,
            'name': request.user,
            'title': 'Szczegóły turnieju',
            'rozpoczety': False
        }
    else:
        data = {
            'mecze': mecze,
            'gracze_w_turnieju': gracze_w_turnieju,
            'turnieje': turnieje,
            'turniej_id': turniej_id,
            'name': request.user,
            'title': 'Szczegóły turnieju',
            'rozpoczety': True
        }
    return render(request, 'szczegoly_turnieju.html', data)


@login_required(login_url="login")
def edytuj_mecz_view(request, id_meczu, turniej_id):  # TODO: zapisywanie zmienionych danych
    print(request.user)
    mecz = Mecze.objects.get(id=id_meczu)
    init = {
        'id_turnieju': mecz.id_turnieju,
        'faza': mecz.faza,
        'id_gracza1': mecz.id_gracza1,
        'id_gracza2': mecz.id_gracza2,
        'wynik_gracza1': mecz.wynik_gracza1,
        'wynik_gracza2': mecz.wynik_gracza2,
        'wygrana': mecz.wygrana
    }
    print("FORM")
    form = MeczeForm(request.GET, instance=mecz, initial=init)
    print(form.is_valid())

    if request.POST:
        #form = MeczeForm(request.POST or None, instance=mecz)
        print("----------------------request.POST")
        print(form.is_valid())
        if form.is_valid():
            form = MeczeForm(request.POST or None, instance=mecz)
            if form.is_valid():
                form.save()
                return redirect('/lista_turniejow/' + str(turniej_id))
            else:
                print("-------------------------IS NOT VALID")
                print(form)

    data = {
        'form': form,
        'name': request.user,
        'title': 'Edytuj mecz',
        'edit': mecz
    }
    return render(request, 'edytuj_mecz.html', data)


@login_required(login_url="login")
def dodaj_mecz_view(request, turniej_id):
    print(request.user)
    turniej = Turnieje.objects.get(id=turniej_id)
    init = {
        'id_turnieju': turniej.id,
            'faza': None,
           'id_gracza1': None,
           'id_gracza2': None,
           'wynik_gracza1': None,
           'wynik_gracza2': None,
           'wygrana': None
    }

    #form = MeczeForm(initial=init)
    form = MeczeForm(request.GET, initial=init)

    if request.POST:
        form = MeczeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/lista_turniejow/' + str(turniej_id))

    data = {
        'form': form,
        'turniej_id': turniej_id,
        'name': request.user.login,
        'title': 'Stwórz mecz'
    }
    return render(request, 'edytuj_mecz.html', data)


@login_required(login_url="login")
def usun_mecz_view(request, id_meczu, turniej_id):
    print(request.user)
    mecz = Mecze.objects.get(id=id_meczu)
    mecz.delete()
    return redirect('/lista_turniejow/' + str(turniej_id))

