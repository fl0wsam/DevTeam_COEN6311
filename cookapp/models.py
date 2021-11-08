from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('user name'), unique=True, max_length=20, )
    email = models.EmailField(
        _('email address'), unique=True, null=True, blank=True)
    is_company = models.BooleanField(default=False)
    first_name = models.CharField(null=True, blank=True, max_length=255)
    last_name = models.CharField(null=True, blank=True, max_length=255)
    # photo = models.ImageField(null=True, blank=True,
    #                           upload_to="ProfilePhotos")
    objects = UserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def get_full_name(self):
        return str(self.first_name) + " " + str(self.last_name)

class Ingrediants(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ingrediants = models.CharField(max_length=255, blank=True, null=True)
    direction = models.CharField(max_length=255, blank=True, null=True)
    upload_time = models.DateTimeField()
    cook_duration = models.IntegerField()
    photo = models.ImageField(null=True, blank=True,
                              upload_to="RecipePhotos")
    def __str__(self):
        return self.name
    link = models.CharField(max_length=255, blank=True, null=True)
    
class Rate(models.Model):
    rate = models.IntegerField(null=True, blank=True)
