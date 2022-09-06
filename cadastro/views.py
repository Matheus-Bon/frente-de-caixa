from multiprocessing import context
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import ListaDespesas, ListaProdutos
from django.urls import reverse_lazy




""" Views """

class ProdutoCreate(CreateView):
    model = ListaProdutos
    fields = ['nome_produto', 'quantidade_produto', 'custo_venda', 'fornecedor', 'data_adicao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('vendas')

class DespesaCreate(CreateView):
    model = ListaDespesas
    fields = ['nome_despesa', 'quantidade_despesa', 'custo', 'tipo_gasto', 'data_atualizacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('vendas')


""" Update """

class ProdutoUpdate(UpdateView):
    model = ListaProdutos
    fields = ['nome_produto', 'quantidade_produto', 'custo_venda', 'fornecedor', 'data_adicao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('vendas')

class DespesaUpdate(UpdateView):
    model = ListaDespesas
    fields = ['nome_despesa', 'quantidade_despesa', 'custo', 'tipo_gasto', 'data_atualizacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('vendas')


""" Delete """

class ProdutoDelete(DeleteView):
    model = ListaProdutos
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('vendas')

class DespesaDelete(UpdateView):
    model = ListaDespesas
    template_name = 'cadastro/form-excluir.html'
    succes_url = reverse_lazy('vendas')


""" Lista """

class ProdutoList(ListView):
    model = ListaProdutos
    template_name = 'paginas/gastos.html'

class DespesaList(ListView):
    model = ListaDespesas
    template_name = 'paginas/gastos.html'