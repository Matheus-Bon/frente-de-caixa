import imp
from django.urls import path
from .views import relatoriosPage, vendasPage
from cadastro.views import estoque , gastos


urlpatterns = [

    path('vendas', vendasPage, name='vendas'),
    path('estoque', estoque, name='estoque'),
    path('gastos', gastos, name='gastos'),
    path('relatorios', relatoriosPage, name='relatorios'),




]
