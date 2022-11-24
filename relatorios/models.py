from django.db import models

# Create your models here.

class Caixa(models.Model):
    periodo = models.DateTimeField(auto_now_add= True ,verbose_name='Data de Criação')
    caixa = models.FloatField(verbose_name='Caixa')
    log_forma_pagamento = models.CharField(max_length=50, verbose_name='Forma de Pagamento')


    def __str__(self):
        return "{} {} {}".format(self.periodo, self.caixa, self.log_forma_pagamento)

    def get_data(self):
        return{
            'periodo': self.periodo,
			'caixa': self.caixa,
			'log_forma_pagamento': self.log_forma_pagamento
        }

class ControleProduto(models.Model):
	periodo = models.DateTimeField(auto_now_add= True, verbose_name='Período')
	produtos = models.JSONField(verbose_name='Produtos')
	faturamento = models.FloatField(verbose_name='Faturamento')
	log_forma_pagamento = models.CharField(max_length=50, verbose_name='Forma de Pagamento')

	def __str__(self):
		return "{} {} {} {}".format(self.periodo, self.produtos, self.faturamento, self.log_forma_pagamento)
    
	def get_data(self):
		return{
            'periodo': self.periodo,
            'produtos': self.produtos,
            'faturamento': self.faturamento,
			'log_forma_pagamento': self.log_forma_pagamento
        }

class ControleGastos(models.Model):
	periodo = models.DateTimeField(auto_now_add= True, verbose_name='Período')
	despesas = models.JSONField(verbose_name='Despesas')
	caixa = models.JSONField(verbose_name="Caixa")

	def __str__(self):
		return "{} {} {}".format(self.periodo, self.despesas, self.caixa)
    
	def get_data(self):
		return{
            'periodo': self.periodo,
            'despesas': self.despesas,
			'caixa': self.caixa
        }
