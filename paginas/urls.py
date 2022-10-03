import imp
from django.urls import path
from .views import  vendasPage, estoquePage, gastosPage, relatoriosPage


urlpatterns = [

    path('vendas', vendasPage, name='vendas'),
    path('estoque/', estoquePage, name='estoque'),
    path('gastos/', gastosPage, name='gastos'),
    path('relatorios', relatoriosPage, name='relatorios'),



    #path('vendas', VendasView.as_view(), name='vendas'),
    #path('estoque', EstoqueView.as_view(), name='estoque'),
    #path('gastos', GastosView.as_view(), name='gastos'), 
    #path('relatorios', RelatoriosView.as_view(), name='relatorios'),

   

]