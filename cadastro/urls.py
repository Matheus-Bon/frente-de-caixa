from django.urls import path
from .views import ProdutoCreate, DespesaCreate, ProdutoCreate1
from .views import ProdutoUpdate, DespesaUpdate
from .views import ProdutoDelete, DespesaDelete
from .views import ProdutoList
from . import views


urlpatterns = [
    path('cadastrar/produto', ProdutoCreate.as_view(), name='cadastrar-produto'),
    #path('cadastrar/despesas', DespesaCreate.as_view(), name='cadastrar-despesa'),

    path('editar/produto/<int:pk>', ProdutoUpdate.as_view(),name='editar-produto'),
    #path('editar/despesa/<int:pk>', DespesaUpdate.as_view(),name='editar-despesa'),

    path('excluir/produto/<int:pk>', ProdutoDelete.as_view(),name='excluir-produto'),
    #path('excluir/despesa/<int:pk>', DespesaDelete.as_view(),name='excluir-despesa'),
    
   # path('gastos/despesas',DespesaList.as_view(), name='lista-despesa'),

    # Estoque
    path('estoque',views.estoqueList, name='estoque'),
    path('estoque/adicionar', views.addProduct, name='estoque-adicionar'),
    path('estoque/editar/', views.editProduct, name='estoque-editar'),
    path('estoque/produto/<int:product_id>', views.viewProduct, name='produto-unico'),
    path('estoque/deletar/<int:product_id>', views.delProduct, name='estoque-deletar'),

    # Despesa
    path('gastos', views.lista_despesa, name='gastos')
]