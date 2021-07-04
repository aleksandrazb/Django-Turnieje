from .Views.home import home
from .Views.login import register_user
from .Views.turnieje import turniej_create_view, usun_turniej_view, turnieje_view
from .Views.szukaj import szukaj_list_view
from .Views.gracze import dodaj_gracza_view, gracze_view, usun_gracza_view, dodaj_gracza_do_turnieju_view, \
   usun_gracza_z_turnieju_view, paruj_graczy_turnieju_view
from .Views.mecze import mecze_view, edytuj_mecz_view, dodaj_mecz_view, usun_mecz_view


__all__ = [
   'home',
   'register_user',
   'turniej_create_view',
   'usun_turniej_view',
   'turnieje_view',
   'szukaj_list_view',
   'dodaj_gracza_view',
   'gracze_view',
   'usun_gracza_view',
   'dodaj_gracza_do_turnieju_view',
   'usun_gracza_z_turnieju_view',
   'paruj_graczy_turnieju_view',
   'mecze_view',
   'edytuj_mecz_view',
   'dodaj_mecz_view',
   'usun_mecz_view'
]
