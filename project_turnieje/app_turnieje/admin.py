from django.contrib import admin
from .models import Turnieje, Uzytkownicy, Gracze, Mecze, GraczeWTurnieju

# Register your models here.
admin.site.register(Turnieje)
admin.site.register(Uzytkownicy)
admin.site.register(Gracze)
admin.site.register(Mecze)
admin.site.register(GraczeWTurnieju)
