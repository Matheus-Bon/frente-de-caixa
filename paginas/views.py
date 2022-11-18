from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib import messages


#               Autenticação para entrar nas páginas




@login_required(login_url='login/')
@cache_control(no_cache=True, must_revalidate=True, no_store= True)

def relatorios(request):
    return render(request , 'paginas/relatorios.html')


@login_required(login_url='login/')
@cache_control(no_cache=True, must_revalidate=True, no_store= True)
def vendas(request):
    return render(request , 'paginas/vendas.html')


# Função login

def Login(request):
    if request.user == None or request.user == '' or request.user.username =='':
        return render(request, 'paginas/login.html')
    else:
        return HttpResponseRedirect('/')

# Função user


def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password = password)
     
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/vendas')
        else:
            messages.error(request, "Entre com os dados corretos.")

# Função logout

def LogoutUser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('/login')