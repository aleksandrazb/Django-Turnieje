from .Views.home import home
from .Views.login import login

from .Views.turnieje import turniej_create_view, usun_turniej_view, turnieje_view, szczegoly_turnieju_view
from .Views.szukaj import szukaj_list_view
from .Views.gracze import dodaj_gracza_view, gracze_view, usun_gracza_view


__all__ = [
   'home',
   'login',

   'turniej_create_view',
   'szukaj_list_view',
   'usun_turniej_view',
   'turnieje_view',
   'dodaj_gracza_view',
   'gracze_view',
   'usun_gracza_view',
   'szczegoly_turnieju_view'
]