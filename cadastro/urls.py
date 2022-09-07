from django.urls import path
from .views import ProdutoCreate, DespesaCreate
from .views import ProdutoUpdate, DespesaUpdate
from .views import ProdutoDelete, DespesaDelete
from .views import ProdutoList, DespesaList



urlpatterns = [
    path('cadastrar/produto', ProdutoCreate.as_view(), name='cadastrar-produto'),
    path('cadastrar/despesas', DespesaCreate.as_view(), name='cadastrar-despesa'),

    path('editar/produto/<int:pk>/', ProdutoUpdate.as_view(),name='editar-produto'),
    path('editar/despesa/<int:pk>', DespesaUpdate.as_view(),name='editar-despesa'),

    path('excluir/produto/<int:pk>/', ProdutoDelete.as_view(),name='excluir-produto'),
    path('excluir/despesa/<int:pk>', DespesaDelete.as_view(),name='excluir-despesa'),
    
    path('estoque/lista-produtos',ProdutoList.as_view(), name='lista-produto'),
    path('gastos/despesas',DespesaList.as_view(), name='lista-despesa'),


]