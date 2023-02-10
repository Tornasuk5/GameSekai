from django.urls import path
from . import views

urlpatterns = [
    path('<str:game_name>', views.game)
]
