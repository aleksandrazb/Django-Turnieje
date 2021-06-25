from django.contrib import admin
from .models import Turnieje, Uzytkownicy, Gracze

# Register your models here.
admin.site.register(Turnieje)
admin.site.register(Uzytkownicy)
admin.site.register(Gracze)
