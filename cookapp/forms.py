from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2','is_company']

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields =['name', 'ingrediants', 'direction','upload_by', 'cook_duration','photo','link']
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['photo'].required = False
        self.fields['link'].required = False