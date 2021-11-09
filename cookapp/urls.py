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

    
]
