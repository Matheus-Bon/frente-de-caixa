from django.urls import path
from . import views



# routes 
urlpatterns = [

    # URLs da parte do CRUD em Produtos
    path('add_produto', views.add_produto, name='add_produto2'),
    path('produto/<str:produto_id>', views.produto, name='produto'),
    path('edit_produto', views.edit_produto, name='edit_produto'),
    path('delete_produto/<str:produto_id>', views.delete_produto, name='delete_produto'),

    # URLs da parte do CRUD em Despesas
    path('add_despesa', views.add_despesa, name='add_despesa'),
    path('despesa/<str:despesa_id>', views.despesa, name='despesa'),
    path('edit_despesa', views.edit_despesa, name='edit_despesa'),
    path('delete_despesa/<str:despesa_id>', views.delete_despesa, name='delete_despesa'),

    path('finalizar-vendas', views.finalizar_vendas, name='finalizar_vendas'),

    path('edit_by_type', views.edit_by_type, name='edit_lote'),

    # checkProduto
    path('json/', views.produto_json, name='produto_json' )
]
