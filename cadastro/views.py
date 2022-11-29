
from math import prod
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import ListaDespesas, ListaProdutos
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from relatorios.models import *



""" Configurações do CRUD de Produtos """


def estoque(request):
    #caixa = Caixa()
    #caixa.log_forma_pagamento = ""
    #caixa.caixa = 0
    #caixa.save()
    produto_list = ListaProdutos.objects.all()
    tags = []
    for prod in produto_list:
        if prod.tipo_produto in tags:
            pass
        else:
            tags.append(prod.tipo_produto)
    return render (request , 'paginas/estoque.html',{'tags':tags,'produtos':produto_list})

# ADD Produto

def add_produto(request):
    if request.method == 'POST':
        if request.POST.get('nome_produto')\
            and request.POST.get('quantidade_produto')\
            or request.POST.get('nota_produto'):
            produto = ListaProdutos()
            produto.nome_produto = request.POST.get('nome_produto')
            produto.quantidade_produto = request.POST.get('quantidade_produto')
            produto.nota_produto = request.POST.get('nota_produto')
            produto.custo = request.POST.get('custo')
            produto.tipo_produto = request.POST.get('tipo_produto')
            produto.vendido = 0
            produto.save()
            messages.success(request, 'Produto adicionado com sucesso!')
            return HttpResponseRedirect("/estoque")
    else:
        return render(request, 'cadastro\\add.html')


# VIEW Produto

def produto(request, produto_id):
    produto = ListaProdutos.objects.get(id = produto_id)
    if produto != None:
        return render(request , 'cadastro/edit.html', {'produto':produto})


# EDIT Produto

def edit_produto(request):
    if request.method == 'POST':
        produto = ListaProdutos.objects.get(id = request.POST.get('id'))
        if produto != None:
            produto.nome_produto = request.POST.get('nome_produto')
            produto.quantidade_produto = request.POST.get('quantidade_produto')
            produto.nota_produto = request.POST.get('nota_produto')
            produto.custo = request.POST.get('custo')
            produto.tipo_produto = request.POST.get('tipo_produto')
            produto.save()
            messages.success(request, 'Produto editado com sucesso!')
            return HttpResponseRedirect("/estoque")

# EDIT LIST Produto

def edit_by_type(request):
    if request.method == 'POST':
        produtos = ListaProdutos.objects.all()
        for produto in produtos:
            if produto.tipo_produto == request.POST.get('tipo_produto'):
                produto.custo = request.POST.get('custo')
                if request.POST.get('quantidade_produto'):
                    produto.quantidade_produto = request.POST.get('quantidade_produto')
                produto.save()
        return HttpResponseRedirect("/estoque")

# DELETE Produto

def delete_produto(request, produto_id):
    produto = ListaProdutos.objects.get(id = produto_id)
    produto.delete()
    messages.success(request, "Produto deletado com sucesso!")
    return HttpResponseRedirect("/estoque")







""" Configurações do CRUD de Despesas """


def gastos(request):
    despesa_list = ListaDespesas.objects.all()

    gastos = {'mensal': 0,
    'semanal': 0,
    'esporadico': 0}

    for despesa in despesa_list:
        if despesa.tipo_gasto.lower() == 'mensal':
            gastos['mensal'] += despesa.custo
        if despesa.tipo_gasto.lower() == 'semanal':
            gastos['semanal'] += despesa.custo
        if despesa.tipo_gasto == 'Esporádico':
            gastos['esporadico'] += despesa.custo

    return render (request , 'paginas/gastos.html',{'despesas':despesa_list, 'gastos': gastos})


# ADD Despesa

def add_despesa(request):
    if request.method == 'POST':
        if request.POST.get('nome_despesa')\
            and request.POST.get('custo')\
            and request.POST.get('quantidade_despesa')\
            and request.POST.get('tipo_gasto')\
            or request.POST.get('nota_despesa'):
            despesa = ListaDespesas()
            despesa.nome_despesa = request.POST.get('nome_despesa')
            despesa.custo = request.POST.get('custo')
            despesa.quantidade_despesa = request.POST.get('quantidade_despesa')
            despesa.tipo_gasto = request.POST.get('tipo_gasto')
            despesa.nota_despesa = request.POST.get('nota_despesa')
            despesa.save()
            messages.success(request, 'Despesa adicionada com sucesso!')
            return HttpResponseRedirect('/gastos')
    else:
        return render(request , 'cadastro/add-despesa.html')
        

# VIEW Despesa

def despesa(request, despesa_id):
    despesa = ListaDespesas.objects.get(id = despesa_id)
    if despesa != None:
        return render(request , 'cadastro/edit-despesa.html', {'despesa':despesa})


# EDIT Despesa

def edit_despesa(request):
    if request.method == 'POST':
        despesa = ListaDespesas.objects.get(id = request.POST.get('id'))
        if despesa != None:
            despesa.nome_despesa = request.POST.get('nome_despesa')
            despesa.custo = request.POST.get('custo')
            despesa.tipo_gasto = request.POST.get('tipo_gasto')
            despesa.nota_despesa = request.POST.get('nota_despesa')
            despesa.save()
            messages.success(request, 'Despesa editada com sucesso!')
            return HttpResponseRedirect('/gastos')


# DELETE Despesa

def delete_despesa(request, despesa_id):
    despesa = ListaDespesas.objects.get(id = despesa_id)
    despesa.delete()
    messages.success(request, "Despesa deletada com sucesso!")
    return HttpResponseRedirect('/gastos') 


""" Configuração dO JSON para Produtos """


def produto_json(request):
    produtos = ListaProdutos.objects.all()
    data = [produto.get_data() for produto in produtos]
    response = {'data': data}
    return JsonResponse(response)


""" Listagem de Produtos a serem vendidos """

def finalizar_vendas(request):
    if request.method == 'POST':
        cart = json.loads(request.POST.get('cart'))
        caixa = Caixa.objects.first()
        caixa.caixa += float(request.POST.get('valor-total'))
        if caixa.log_forma_pagamento == '':
            caixa.log_forma_pagamento = caixa.log_forma_pagamento + request.POST.get('forma_pagamento')
        else:
            caixa.log_forma_pagamento = caixa.log_forma_pagamento + ", " + request.POST.get('forma_pagamento')
        caixa.save()
        produtos = ListaProdutos.objects.all()
        print(cart)
        for i in range(0, len(produtos)):
            produto = ListaProdutos.objects.get(id = cart[i]['id']) 
            produto.quantidade_produto -= int(cart[i]['quantidade_produto'])
            produto.vendido += int(cart[i]['quantidade_produto'])
            produto.save()
        return HttpResponseRedirect('/estoque')
