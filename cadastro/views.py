
from atexit import register
from cgitb import html
from dataclasses import fields
import json
from unittest import result
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import ListaDespesas, ListaProdutos
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib import messages


""" Configurações do CRUD da parte de Despesa FIXA e VARIÁVEL """


def despesa_List(request):
    despesa_list = ListaDespesas.objects.all()
    return render(request, "paginas/gastos.html", {'despesas': despesa_list })


#----------# Função ADD Despesa #----------#


def add_despesa(request):
    if request.method =="POST":
        if request.POST.get('nome_despesa') \
            and request.POST.get('quantidade_despesa') \
            and request.POST.get('custo') \
            and request.POST.get('tipo_gasto') \
            and request.POST.get('data_atualizacao') \
            or request.POST.get('nota_despesa'):
            
            despesa = ListaDespesas()
            despesa.nome_despesa = request.POST.get('nome_despesa')
            despesa.quantidade_despesa = request.POST.get('quantidade_despesa')
            despesa.custo = request.POST.get('custo')
            despesa.tipo_gasto = request.POST.get('tipo_gasto')
            despesa.data_atualizacao = request.POST.get('data_atualizacao')
            despesa.nota_despesa = request.POST.get('nota_despesa')
            despesa.save()
            messages.success(request, "Despesa adicionada com sucesso!")
            return HttpResponseRedirect('/gastos')
    else:
            return render(request, 'cadastro\\add-despesa.html')


#----------# Função VIEW Despesa #----------#


def despesa(request, despesas_id):
    despesas =  ListaDespesas.objects.get(id = despesas_id)
    if despesas != None:
        return render(request, "cadastro \\ edit-despesa.html", {'despesa':despesas})


#----------# Função EDIT Despesa #----------#

def edit_despesa(request):
    if request.method == 'POST':
        despesa = ListaDespesas.objects.get(id = request.POST.get('id'))
        if despesa != None:
            despesa.nome_despesa = request.POST.get('nome_despesa')
            despesa.quantidade_despesa = request.POST.get('quantidade_despesa')
            despesa.custo = request.POST.get('custo')
            despesa.tipo_gasto = request.POST.get('tipo_gasto')
            despesa.data_atualizacao = request.POST.get('data_atualizacao')
            despesa.nota_despesa = request.POST.get('nota_despesa')
            despesa.save()
            messages.success(request, "Despesa atualizada com sucesso!")
            return HttpResponseRedirect("/gastos")
            
            

#----------# Função DELETE Despesa #----------#

def delete_despesa(request, despesa_id):
    despesa = ListaDespesas.objects.get(id = despesa_id)
    despesa.delete()
    messages.success(request, "Despesa deletada com sucesso!")
    return HttpResponseRedirect("/gastos")







""" Configurações do CRUD da parte de Produtos """


def produto_List(request):
    produto_List = ListaProdutos.objects.all()
    return render(request, "paginas/estoque.html", {'produtos': produto_List})


#----------# Função ADD Produto #----------#


def add_produto(request):
    if request.method =="POST":
        if request.POST.get('nome_produto') \
            and request.POST.get('quantidade_produto') \
            and request.POST.get('data_adicao') \
            or request.POST.get('nota_produto'):
            
            produto = ListaProdutos()
            produto.nome_produto = request.POST.get('nome_produto')
            produto.quantidade_produto = request.POST.get('quantidade_produto')
            produto.data_adicao = request.POST.get('data_adicao')
            produto.nota_produto = request.POST.get('nota_produto')
            produto.save()
            messages.success(request, "Produto adicionado com sucesso!")
            return HttpResponseRedirect('/estoque')
    else:
            return render(request , 'cadastro\\add.html')


#----------# Função VIEW Produto #----------#


def produto(request, produto_id):
    produtos = ListaProdutos.objects.get(id=produto_id)
    if produtos != None:
        return render(request, 'cadastro\\edit.html', {'produto': produtos})


#----------# Função EDIT Produto #----------#


def edit_produto(request):
    if request.method == "POST":
        produto = ListaProdutos.objects.get(id=request.POST.get('id'))
        if produto != None:
            produto.nome_produto = request.POST.get('nome_produto')
            produto.quantidade_produto = request.POST.get('quantidade_produto')
            produto.data_adicao = request.POST.get('data_adicao')
            produto.nota_produto = request.POST.get('nota_produto')
            produto.save()
            messages.success(request, "Produto atualizado com sucesso!")
            return HttpResponseRedirect('/estoque')


#----------# Função DELETE Produto #----------#

def delete_produto(request, produto_id):
    produto = ListaProdutos.objects.get(id = produto_id)
    produto.delete()
    messages.success(request, "Produto deletado com sucesso!")
    return HttpResponseRedirect('/estoque')











""" Configuração dO JSON para Despesas """


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


""" def checkProduto(request):
    if is_ajax:
        if request.method == 'GET':
            produtos = list(ListaProdutos.objects.all().values())
            return JsonResponse({'produtos': produtos})

        return JsonResponse({'status': 'Invalid request'}, status=400)

    else:
        return HttpResponseBadRequest('Invalid request')
 """




