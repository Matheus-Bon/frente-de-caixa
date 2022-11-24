import imp
from django.urls import path
from cadastro.views import estoque , gastos
from .views import *
from . import views

urlpatterns = [

    path('finalizar-caixa', finalizar_caixa, name='finalizar-caixa'),
    path('finalizar-gastos', finalizar_gastos, name='finalizar-gastos'),
    path('relatorios', relatorios, name="relatorios"),
    path('relatorios/produtos', relatorio_produtos, name="relatorios-produtos"),
    path('relatorios/despesas', relatorio_despesas, name="relatorios-despesas"),
    path('edit-caixa', edit_caixa, name="edit-caixa")
]
