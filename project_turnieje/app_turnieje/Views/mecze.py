from django.shortcuts import render, redirect
from ..forms import MeczeForm
from ..models import Mecze, Turnieje


def mecze_view(request, turniej_id):
    print(request.user)
    mecze = Mecze.objects.filter(id_turnieju=turniej_id)
    turniej = Turnieje.objects.filter(id=turniej_id)

    data = {
        'mecze': mecze,
        'turniej': turniej,
        'turniej_id': turniej_id,
        'name': request.user,
        'title': 'Szczegóły turnieju'
    }
    return render(request, 'szczegoly_turnieju.html', data)


def edytuj_mecz_view(request, id_meczu):  # TODO: zapisywanie zmienionych danych
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
    form = MeczeForm(initial=init)

    if request.POST:
        form = MeczeForm(request.POST, instance=mecz)
        if form.is_valid():
            form.save()

        data = {
            'form': form,
            'name': request.user,
            'title': 'Edytuj mecz',
            'edit': mecz
        }
        return render(request, 'edytuj_mecz.html', data)
    else:
        data = {
            'form': form,
            'name': request.user,
            'title': 'Edytuj mecz',
            'edit': mecz
        }
        return render(request, 'edytuj_mecz.html', data)
