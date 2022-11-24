from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib import messages
from relatorios.models import ControleGastos, ControleProduto, Caixa
from cadastro.models import *
from django.core import serializers
import time

# Create your views here.
def finalizar_caixa(request):
    caixa = Caixa.objects.first()
    vendas_do_dia = ControleProduto()
    vendas_do_dia.produtos = serializers.serialize('json', ListaProdutos.objects.all())

    cash = 0
    for produto in ListaProdutos.objects.all():
        cash = cash + (produto.vendido * produto.custo)
        produto.vendido = 0
        produto.save()
    vendas_do_dia.faturamento = cash
    vendas_do_dia.log_forma_pagamento = caixa.log_forma_pagamento
    vendas_do_dia.save()

    caixa.log_forma_pagamento = ''
    caixa.save()

    return HttpResponseRedirect('/estoque')

def finalizar_gastos(request):
    cash = Caixa.objects.first()

    registro_despesas = ControleGastos()
    registro_despesas.caixa = cash.caixa
    registro_despesas.despesas = serializers.serialize('json', ListaDespesas.objects.all())
    registro_despesas.save()

    for despesa in ListaDespesas.objects.all():
        cash.caixa -= despesa.custo
        cash.save()

    ListaDespesas.objects.all().delete()
    return HttpResponseRedirect('/estoque')

def relatorios(request):
    cash = Caixa.objects.first().caixa
    data_despesa, data_caixa = [], []
    for controle_periodo in ControleProduto.objects.all():
        info = {'periodo': controle_periodo.periodo, 'pk': controle_periodo.pk}
        data_caixa.append(info)
    for controle_periodo in ControleGastos.objects.all():
        info = {'periodo': controle_periodo.periodo, 'pk': controle_periodo.pk}
        data_despesa.append(info)
    return render(request, 'paginas/relatorios.html', {'data_despesa':data_despesa, 'data_caixa':data_caixa, 'cash':cash})


def relatorio_produtos(request):
    if request.method == 'POST':
        prod_json = ControleProduto.objects.get(pk = request.POST.get('periodo'))
        return render(request, 'selecao/historico-produtos.html', {'prod_json':prod_json})
    else:
        return HttpResponseRedirect('/relatorios')

def relatorio_despesas(request):
    if request.method == 'POST':
        desp_json = ControleGastos.objects.get(pk = request.POST.get('periodo'))
        return render(request, 'selecao/historico-gastos.html', {'desp_json':desp_json})
    else:
        return HttpResponseRedirect('/relatorios')

def edit_caixa(request):
    if request.method == 'POST':
        cash = Caixa.objects.first()
        cash.caixa = request.POST.get('new_caixa')
        cash.save()
        return HttpResponseRedirect('/relatorios')

