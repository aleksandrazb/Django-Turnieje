from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from ..managers import CustomUserManager


class Uzytkownicy(AbstractBaseUser):
    id = models.AutoField(db_index=True, primary_key=True)
    login = models.CharField(max_length=50, unique=True, default='anonymus')
    #password = models.CharField(max_length=1024)
    email = models.EmailField(max_length=254, null=True, blank=True)
    data_urodzenia = models.DateField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    has_module_perms = models.BooleanField(default=False)
    has_perms = models.BooleanField(default=False)
    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['data_urodzenia']
    objects = CustomUserManager()

    def get_absolute_url(self):
        return reverse('uzytkownik_detail', kwargs={'pk': self.login})

    def __str__(self):
        return str(self.login)
