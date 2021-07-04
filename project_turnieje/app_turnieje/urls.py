"""app_turnieje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('', include("django.contrib.auth.urls")),
    path('rejestracja/', views.register_user, name='register_user'),
    path('stworz_turniej/', views.turniej_create_view, name='turniej_create_view'),
    path('szukaj/', views.szukaj_list_view, name='szukaj_list_view'),
    path('lista_turniejow/', views.turnieje_view, name='turnieje_view'),
    path('usun_turniej/<turniej_id>/', views.usun_turniej_view, name='usun_turniej_view'),
    path('dodaj_gracza/', views.dodaj_gracza_view, name='dodaj_gracza_view'),
    path('lista_graczy/', views.gracze_view, name='gracze_view'),
    path('usun_gracza/<gracz_id>/', views.usun_gracza_view, name='usun_gracza_view'),
    path('lista_turniejow/<turniej_id>/', views.mecze_view, name='mecze_view'),
    path('edytuj_mecz/<id_meczu>/<turniej_id>', views.edytuj_mecz_view, name='edytuj_mecz_view'),
    path('dodaj_mecz/<turniej_id>/', views.dodaj_mecz_view, name='dodaj_mecz_view'),
    path('usun_mecz/<id_meczu>/<turniej_id>', views.usun_mecz_view, name='usun_mecz_view'),

    path('dodaj_gracza/<turniej_id>/', views.dodaj_gracza_do_turnieju_view, name='dodaj_gracza_do_turnieju_view'),
    path('usun_gracza/<id>/<turniej_id>/', views.usun_gracza_z_turnieju_view, name='usun_gracza_z_turnieju_view'),
]
