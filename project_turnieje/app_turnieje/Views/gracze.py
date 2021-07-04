import random
from django.shortcuts import render, redirect
from ..forms import GraczeForm, GraczeWTurniejuForm
from ..models import Gracze, GraczeWTurnieju, Turnieje, Mecze
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
    form = GraczeForm(request.GET or None)
    if request.POST:
        form = GraczeForm(request.POST)
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
    gracz = Gracze.objects.get(id=gracz_id)
    gracz.delete()
    return redirect(gracze_view)


@login_required(login_url="login")
def dodaj_gracza_do_turnieju_view(request, turniej_id):
    print(request.user)
    form = GraczeWTurniejuForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/lista_turniejow/' + str(turniej_id))
    data = {
        'form': form,
        'name': request.user,
        'title': 'Dodaj gracza do turnieju'
    }
    return render(request, 'dodaj_gracza.html', data)


@login_required(login_url="login")
def usun_gracza_z_turnieju_view(request, id, turniej_id):
    print(request.user)
    gracz_w_turnieju = GraczeWTurnieju.objects.get(id=id)
    gracz_w_turnieju.delete()
    return redirect('/lista_turniejow/' + str(turniej_id))


@login_required(login_url="login")
def paruj_graczy_turnieju_view(request, turniej_id):
    print(request.user)
    turniej = Turnieje.objects.get(id=turniej_id)
    gracze_w_turnieju = GraczeWTurnieju.objects.filter(turniej=turniej_id)
    lista_graczy = []
    for gracz in gracze_w_turnieju:
        lista_graczy.append(gracz)
    if turniej.ilosc_graczy > len(lista_graczy):
        liczba_meczy = len(lista_graczy)//2
    else:
        liczba_meczy = turniej.ilosc_graczy//2
    for mecz in range(liczba_meczy):
        para = random.sample(set(lista_graczy), 2)
        Mecze.objects.create(id_turnieju=turniej, faza=1, id_gracza1=para[0].gracz, id_gracza2=para[1].gracz)
        lista_graczy.remove(para[0])
        lista_graczy.remove(para[1])
    return redirect('/lista_turniejow/' + str(turniej_id))
