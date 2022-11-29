
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from relatorios.models import *


#               Autenticação para entrar nas páginas





def relatorios(request):
    return render(request , 'paginas/relatorios.html')



def vendas(request):
    return render(request , 'paginas/vendas.html')



