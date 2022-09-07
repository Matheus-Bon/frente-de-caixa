from audioop import reverse
from django.db import models

class ListaProdutos(models.Model):
    nome_produto = models.CharField(max_length=50, verbose_name='Produto')
    quantidade_produto = models.IntegerField(verbose_name='Qntd.')
    custo_venda = models.CharField(max_length=10, verbose_name='Custo/Venda')
    fornecedor = models.CharField(max_length=50, verbose_name='Fornecedor')
    data_adicao = models.DateTimeField(verbose_name='Data de Adição')

    def __str__(self):
        return "{} {} {} {} {}".format(self.nome_produto, self.quantidade_produto, self.custo_venda, self.fornecedor, self.data_adicao)

class ListaDespesas(models.Model):
    nome_despesa = models.CharField(max_length=50, verbose_name='Despesas')
    quantidade_despesa = models.CharField(max_length=50, verbose_name='Qntd.')
    custo = models.IntegerField(verbose_name='Custo')
    tipo_gasto = models.CharField(max_length=50, verbose_name='Tipo de Gasto')
    data_atualizacao = models.DateTimeField(verbose_name='Data de Atualização')

    def __str__(self):
        return "{} {} {} {} {}".format(self.nome_despesa, self.quantidade_despesa, self.custo, self.tipo_gasto, self.data_atualizacao)