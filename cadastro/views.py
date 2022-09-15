from itertools import product
from django.http import HttpResponseRedirect
import imp
from multiprocessing import context
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import ListaDespesas, ListaProdutos
from django.urls import reverse_lazy




""" Views """

class ProdutoCreate(CreateView):
    model = ListaProdutos
    fields = ['nome_produto', 'quantidade_produto', 'custo_venda', 'fornecedor', 'data_adicao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('lista-produto')

class DespesaCreate(CreateView):
    model = ListaDespesas
    fields = ['nome_despesa', 'quantidade_despesa', 'custo', 'tipo_gasto', 'data_atualizacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('lista-despesa')


class ProdutoCreate1(CreateView):
    model = ListaProdutos
    fields = ['nome_produto', 'quantidade_produto', 'custo_venda', 'fornecedor', 'data_adicao']
    template_name = 'cadastro/form1.html'

""" Update """

class ProdutoUpdate(UpdateView):
    model = ListaProdutos
    fields = ['nome_produto', 'quantidade_produto', 'custo_venda', 'fornecedor', 'data_adicao']
    template_name = 'paginas/listas/estoque.html'
    success_url = reverse_lazy('lista-produto')

    
class DespesaUpdate(UpdateView):
    model = ListaDespesas
    fields = ['nome_despesa', 'quantidade_despesa', 'custo', 'tipo_gasto', 'data_atualizacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('lista-despesa')


""" Delete """

class ProdutoDelete(DeleteView):
    model = ListaProdutos
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('lista-produto')

class DespesaDelete(DeleteView):
    model = ListaDespesas
    template_name = 'cadastro/form-excluir.html'
    succes_url = reverse_lazy('lista-despesa')


""" Lista """

class ProdutoList(ListView):
    model = ListaProdutos
    template_name = 'paginas/listas/estoque.html'


###class DespesaList(ListView):
   ### model = ListaDespesas
    ###template_name = 'paginas/listas/gastos.html'





def estoqueList(request):
    qs = ListaProdutos.objects.all()
    return render(request, "paginas/listas/estoque.html", {'object_list':qs})

def addProduct(request):
    if request.method == "POST":
        product = ListaProdutos()
        product.nome_produto = request.POST.get('nome_produto')
        product.quantidade_produto  = request.POST.get('quantidade_produto')
        product.custo_venda = request.POST.get('custo_venda')
        product.fornecedor = request.POST.get('fornecedor')
        product.data_adicao = request.POST.get('data_adicao')
        product.save()
        return HttpResponseRedirect('/estoque')
    else:
        return render(request, 'cadastro\\add.html')


def editProduct(request):
    if request.method == "POST":
        product = ListaProdutos.objects.get(id = request.POST.get('id'))
        if product != None:
            product.nome_produto = request.POST.get('nome_produto')
            product.quantidade_produto  = request.POST.get('quantidade_produto ')
            product.custo_venda = request.POST.get('custo_venda')
            product.fornecedor = request.POST.get('fornecedor')
            product.data_adicao = request.POST.get('data_adicao')
            product.save()
            return HttpResponseRedirect('estoque')

def delProduct(request, product_id):
    product = ListaProdutos.objects.get(id = product_id)
    product.delete()
    return HttpResponseRedirect('estoque')




""" Configuração da views para Despesas """

def lista_despesa(request):
    lista_despesa = ListaDespesas.objects.all()
    return render(request, "paginas/listas/gastos.html", {"despesa":lista_despesa})