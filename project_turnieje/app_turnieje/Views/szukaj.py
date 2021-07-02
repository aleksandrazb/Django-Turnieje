from django.shortcuts import render
from ..models import Turnieje
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def szukaj_list_view(request):
    print(request.user)
    print("GET")
    print(request.GET)
    print("POST")
    print(request.POST)

    szukaj_od = request.GET.get('szukaj_od')
    szukaj_do = request.GET.get('szukaj_do')

    if szukaj_od is None or '':
        szukaj_od = '1000-01-01'
    if szukaj_do is None or '':
        szukaj_do = '3000-01-01'

    lista_turniejow = Turnieje.objects.filter(data_rozpoczecia__range=[szukaj_od, szukaj_do])

    data = {
        'name': request.user,
        'turnieje': lista_turniejow,
        'szukaj_od': szukaj_od,
        'szukaj_do': szukaj_do,
        'title': 'Szukaj turniejów'
    }
    return render(request, 'szukaj.html', data)
