import datetime

import pytz as pytz
from django.shortcuts import render
from ..models import Turnieje


def home(request):
    print(request.user)
    teraz = datetime.datetime.now()
    teraz = pytz.utc.localize(teraz)

    lista_turniejow = Turnieje.objects.filter(data_rozpoczecia__lt=teraz)

    data = {
        'name': request.user,
        'turnieje': lista_turniejow,
        'title': 'Lista rozpoczętych turniejów'
    }
    return render(request, 'home.html', data)

