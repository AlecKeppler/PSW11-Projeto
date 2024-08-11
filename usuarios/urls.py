from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('cadastro/', views.Cadastro, name="cadastro"),
    path('logar/', views.Logar, name="logar")
]
