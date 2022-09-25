import imp
from django.urls import path
from .views import VendasView, GastosView, EstoqueView, RelatoriosView 


urlpatterns = [
    path('vendas', VendasView.as_view(), name='vendas'),
    path('estoque', EstoqueView.as_view(), name='estoque'),
    path('gastos', GastosView.as_view(), name='gastos'), 
    path('relatorios', RelatoriosView.as_view(), name='relatorios'),

   

]