from .views import *
from knox import views as knox_views
from django.urls import path

app_name = 'crm_app'

urlpatterns = [
    path('login/', LoginAPI.as_view(),
         name="login"),
    # # SEARCH APIS
    # path('search/<slug:type>/', SearchAPI.as_view(),
    #      name="search"),
]
