import imp
from django.urls import path
from cadastro.views import estoque , gastos
from .views import vendas, relatorios
from . import views


urlpatterns = [

    path('vendas', vendas, name='vendas'),
    path('estoque', estoque, name='estoque'),
    path('gastos', gastos, name='gastos'),
    path('relatorios', relatorios, name='relatorios'),


    path('login/' , views.Login , name='login'),
    path('login_user' , views.LoginUser , name='login_user'),
    path('logout' , views.LogoutUser , name='logout'),



]
