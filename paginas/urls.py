import imp
from django.urls import path
from cadastro.views import estoque , gastos
from .views import vendas
from . import views
from relatorios.views import *

urlpatterns = [

    path('vendas', vendas, name='vendas'),
    path('estoque', estoque, name='estoque'),
    path('gastos', gastos, name='gastos'),


    path('' , views.Login , name='login'),
    path('login_user' , views.LoginUser , name='login_user'),
    path('logout' , views.LogoutUser , name='logout'),



]
