from django.db.models.aggregates import Count
from django.shortcuts import render, redirect , get_object_or_404
from .models import *
from .forms import CreateUserForm,RecipeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.utils import timezone
from django.db.models import Max
# search
from functools import reduce
import operator
from django.db.models import Q

# Create your views here.
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')		
	context = {'form':form}
	return render(request, 'register.html', context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')
	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def home(request):    
    if request.user.is_authenticated and request.user.is_company:
        recipe = Recipe.objects.order_by('-score')
        ingrediants=Ingrediants.objects.all().order_by('-count')
        # ing = Ingrediants.objects.all().aggregate(Max('count'))

        context = {
            'list_of_recipes':recipe,
            'list_of_ingrediants':ingrediants,
        }
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html', {})

def ResetPasswordView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            form = PasswordChangeForm(user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(
                    request, 'Your password was successfully updated!')
                return redirect('login')
            else:
                messages.error(request, 'Please provide correct information.')
                return render(request, 'password_reset.html', {'form': form })
        except:
            messages.error(request, 'User does not exists')
    
    form = PasswordChangeForm(request.user)
    return render(request, 'password_reset.html', {'form': form })


@login_required(login_url='login')
def rate_recipe(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        el_id=str(el_id)
        recipe = Recipe.objects.get(id=el_id)
        recipe.total_score=int(recipe.total_score)+1
        recipe.score = (int(recipe.score)+int(val))
        recipe.save()
        mscore=0
        if recipe.total_score>0:
            mscore =round(recipe.score/recipe.total_score,2)
        context ={
            'recipe':recipe,
            'mscore':mscore
        }
        return render(request, 'recipes_detail.html', context)
    return render(request, 'recipes_detail.html', {})

    
@login_required(login_url='login')
def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.upload_time = timezone.now()
            recipe.save()
            return redirect('recipes_detail', recipe.id)
        else:
            return redirect('recipe_create')
    return render(request, 'recipe_create.html', {})

@login_required(login_url='login')
def recipes_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)    
    mscore=0
    if recipe.total_score>0:
        mscore = round(recipe.score/recipe.total_score,2)
    return render(request, 'recipes_detail.html', {'recipe': recipe, 'mscore':mscore})

def search_ingredients(request):
    if request.method == "POST":
        filter_score = request.POST.get('score')
        if request.user.is_authenticated and request.user.is_company:
            if filter_score:
                recipe = Recipe.objects.filter(score__gte=filter_score).order_by('-score')
            else:
                recipe = Recipe.objects.all().order_by('-score')
            context = {
                'list_of_recipes': recipe,
                'searched_filter_score':filter_score
            }
        else:
            ingrediants = request.POST.getlist('name')    
            ingrediants = list(filter(None, ingrediants)) # remove none value    
            recipe = None
            if len(ingrediants)>0:
                ingrediants = list(dict.fromkeys(ingrediants)) # remove duplicate
                recipe= Recipe.objects.filter(reduce(operator.and_, (Q(ingrediants__contains=x) for x in ingrediants))).order_by('-upload_time')
                if filter_score:
                    recipe=recipe.filter(score__gte=filter_score)
                    # score ingrediants
                    # match_ing= Ingrediants.objects.filter(reduce(operator.or_, (Q(name__iexact=x) for x in ingrediants)))
                    for ing in ingrediants:
                        match = Ingrediants.objects.filter(name=ing)
                        if match:
                            match[0].count = match[0].count+1
                            match[0].save()
                        else:
                            new = Ingrediants(name=ing,count=1)
                            new.save()
            
            context = {
                'list_of_recipes': recipe,
                'searched_ingrediants':ingrediants,
                'searched_filter_score':filter_score
            }
        return render(request, 'home.html', context)
    return render(request, 'home.html', {})
    