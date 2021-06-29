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


def edytuj_mecz_view(request, id_meczu):  # TODO: autouzupełnianie pól
    print(request.user)
    if request.POST:
        mecz = Mecze.objects.get(id=id_meczu)
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
