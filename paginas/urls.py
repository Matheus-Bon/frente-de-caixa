import imp
from django.urls import path
from cadastro.views import estoque , gastos
from .views import vendas
from . import views
from relatorios.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('vendas', vendas, name='vendas'),
    path('estoque', estoque, name='estoque'),
    path('gastos', gastos, name='gastos'),


    #path('' , views.Login , name='login'),
    #path('login_user' , views.LoginUser , name='login_user'),
    #path('logout' , views.LogoutUser , name='logout'),

    path('', auth_views.LoginView.as_view( template_name='paginas/login.html' ), name='login'),

    path('logout',auth_views.LogoutView.as_view( ) , name = 'logout' )



]
