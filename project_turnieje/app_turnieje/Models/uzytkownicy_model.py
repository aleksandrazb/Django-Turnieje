from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from ..managers import CustomUserManager


class Uzytkownicy(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()
    id = models.AutoField(db_index=True, primary_key=True)
    login = models.CharField(max_length=50, unique=True, default='anonymus')
    email = models.EmailField(max_length=254, null=True, blank=True)
    data_urodzenia = models.DateField()
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    has_perms = models.BooleanField(default=False)
    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['data_urodzenia']

    def get_absolute_url(self):
        return reverse('uzytkownik_detail', kwargs={'pk': self.login})

    def __str__(self):
        return str(self.login)
