from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import UserManager
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.



class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given username and password.
        """
        if not username:
            raise ValueError(_('The username must be set'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('user name'), unique=True, max_length=20, )
    email = models.EmailField(
        _('email address'), unique=True, null=True, blank=True)
    is_company = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(null=True, blank=True, max_length=255)
    last_name = models.CharField(null=True, blank=True, max_length=255)
    # photo = models.ImageField(null=True, blank=True,
    #                           upload_to="ProfilePhotos")
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def get_full_name(self):
        return str(self.first_name) + " " + str(self.last_name)

class Ingrediants(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ingrediants = models.CharField(max_length=255, blank=True, null=True)
    direction = models.CharField(max_length=255, blank=True, null=True)
    upload_time = models.DateTimeField()
    cook_duration = models.IntegerField(default=0)
    photo = models.ImageField(null=True, blank=True,
                              upload_to="RecipePhotos")
    total_score = models.IntegerField(default=0)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return self.name
    link = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return str(self.pk)