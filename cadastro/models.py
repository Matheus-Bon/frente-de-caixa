from audioop import reverse
from django.db import models


""" Modelo para Produtos """

class ListaProdutos(models.Model):
    nome_produto = models.CharField(max_length=50, verbose_name='Produto')
    quantidade_produto = models.IntegerField(verbose_name='Qntd.')
    data_adicao = models.DateTimeField(auto_now_add= True ,verbose_name='Data de Adição')
    nota_produto = models.TextField()
    

    def __str__(self):
        return "{} {} {} {}".format(self.nome_produto, self.quantidade_produto,self.data_adicao)



""" Modelo para Despesas """
class ListaDespesas(models.Model):

    GASTO = (
        ('Semanal', 'Semanal'),
        ('Mensal', 'Mensal'),
        ('Esporádico', 'Esporádico'),
    )

    nome_despesa = models.CharField(max_length=50, verbose_name='Despesas')
    quantidade_despesa = models.CharField(max_length=50, verbose_name='Qntd.')
    custo = models.IntegerField(verbose_name='Custo')
    tipo_gasto = models.CharField(max_length=50, choices= GASTO, verbose_name='Tipo de Gasto')
    data_atualizacao = models.DateTimeField(auto_now_add=True)
    nota_despesa = models.TextField(null = True)

    def __str__(self):
        return "{} {} {} {} {}".format(self.nome_despesa, self.quantidade_despesa, self.custo, self.tipo_gasto, self.data_atualizacao, self.nota_despesa)