from django.urls import path
from . import views
from .views import checkProduto


# routes 
urlpatterns = [

    # URLs da parte do CRUD em Estoque
    path('estoque',views.estoqueList, name='estoque'),
    path('estoque/adicionar', views.addProduct, name='estoque-adicionar'),
    path('estoque/editar/', views.editProduct, name='estoque-editar'),
    path('estoque/produto/<int:product_id>', views.viewProduct, name='produto-unico'),
    path('estoque/deletar/<int:product_id>', views.delProduct, name='estoque-deletar'),


    # URLs da parte do CRUD em Despesas
    path('gastos', views.despesa_List, name='gastos'),
    path('add_despesa', views.add_despesa, name="add_despesa"),
    path('despesa/<str:despesa_id>', views.despesa, name='despesa'),
    path('edit_despesa', views.edit_despesa, name='edit_despesa'),
    path('delete_despesa/<str:despesa_id>', views.delete_despesa, name='delete_despesa'),


    # checkProduto

    path('get/ajax/validate/produto', checkProduto, name='validate_produto' )
]