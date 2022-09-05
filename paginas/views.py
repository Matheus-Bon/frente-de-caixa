from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



""" Aqui mexe na visualização de cada página """

class VendasView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "paginas/vendas.html"

class EstoqueView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "paginas/estoque.html"

class GastosView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "paginas/gastos.html"
reverse_lazy
class RelatoriosView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "paginas/relatorios.html"





