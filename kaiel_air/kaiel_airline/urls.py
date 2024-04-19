from django.urls import path
from . import views

appname = "kaiel_airline"

urlpatterns = [
    path('', views.index, name="index")
]
