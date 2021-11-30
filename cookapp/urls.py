from knox import views as knox_views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # home
    path('', views.home, name="home"),
    # signup
    path('register/', views.registerPage, name="register"),
	# login
    path('login/', views.loginPage, name="login"),  
	# logout
    path('logout/', views.logoutUser, name="logout"),
    # forgot password
    path('reset_password/',
        views.ResetPasswordView, name="reset_password"),

    path('rate_recipe/', views.rate_recipe, name='rate_recipe'),
    
    path('recipe_create/',views.recipe_create,name='recipe_create'),
    path('recipes_detail/<int:recipe_id>/',views.recipes_detail,name='recipes_detail'),
    
    path('search_ingredients/',views.search_ingredients,name='search_ingredients'),
    
]
