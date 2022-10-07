
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










def estoqueList(request):
    qs = ListaProdutos.objects.all()
    return render(request, "paginas/estoque.html", {'object_list': qs})


def addProduct(request):
    if request.method == "POST":
        product = ListaProdutos()
        product.nome_produto = request.POST.get('nome_produto')
        product.quantidade_produto = request.POST.get('quantidade_produto')
        product.custo_venda = request.POST.get('custo_venda')
        product.fornecedor = request.POST.get('fornecedor')
        product.data_adicao = request.POST.get('data_adicao')
        product.save()
        return HttpResponseRedirect('/estoque')
    else:
        return render(request, 'cadastro\\add.html')


def viewProduct(request, product_id):
    product = ListaProdutos.objects.get(id=product_id)
    if product != None:
        return render(request, 'cadastro\\edit.html', {'produto': product})


def editProduct(request):
    if request.method == "POST":
        product = ListaProdutos.objects.get(id=request.POST.get('id'))
        if product != None:
            product.nome_produto = request.POST.get('nome_produto')
            product.quantidade_produto = request.POST.get('quantidade_produto')
            product.custo_venda = request.POST.get('custo_venda')
            product.fornecedor = request.POST.get('fornecedor')
            product.data_adicao = request.POST.get('data_adicao')
            product.save()
            return HttpResponseRedirect('/estoque')


def delProduct(request, product_id):
    product = ListaProdutos.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect('/estoque')











""" Configuração dO JSON para Despesas """


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def checkProduto(request):
    if is_ajax:
        if request.method == 'GET':
            produtos = list(ListaProdutos.objects.all().values())
            return JsonResponse({'produtos': produtos})

        return JsonResponse({'status': 'Invalid request'}, status=400)

    else:
        return HttpResponseBadRequest('Invalid request')


def checkProduto2(request):
    result = ListaProdutos.objects.all()
    serialized_data = json.dumps(list(result), default=str)

    return JsonResponse({'PRODUTOS': serialized_data})

    # return HttpResponse(serialized_data)



