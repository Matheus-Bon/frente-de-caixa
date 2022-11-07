
from math import prod
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import ListaDespesas, ListaProdutos
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib import messages



""" Configurações do CRUD de Produtos """

def estoque(request):
    produto_list = ListaProdutos.objects.all()
    return render (request , 'paginas/estoque.html',{'produtos':produto_list})

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
            produto.save()
            messages.success(request, 'Produto editado com sucesso!')
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
    return render (request , 'paginas/gastos.html',{'despesas':despesa_list})


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

# def vendas(request):
#     # venda = ListaVendas.objects.all()
#     return render(request, "paginas/vendas.html")

# ADD Produto-Venda

# def add_venda(request):
#     if request.method == 'POST':
#         if request.POST.get('nome_produto')\
#             and request.POST.get('quantidade_produto'):
#             produto = ListaProdutos.objects.get(id = request.POST.get('id'))
#             venda = ListaVendas()
#             venda.nome_produto = produto.nome_produto
#             venda.quantidade_produto = produto.quantidade_produto
#             venda.save()
#             messages.success(request, 'Produto adicionado com sucesso!')
#             return HttpResponseRedirect("/vendas")
#     else:
#         return render(request, 'cadastro\\add-venda.html')

# # DELETE Produto-Venda

# def delete_venda(request, despesa_id):
#     despesa = ListaVendas.objects.get(id = despesa_id)
#     despesa.delete()
#     messages.success(request, "Despesa deletada com sucesso!")
#     return HttpResponseRedirect('/vendas') 
