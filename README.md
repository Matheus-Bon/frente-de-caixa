# PDV (Ponto de Venda)
<h3> Considerações Iniciais </h3>

Esse projeto tem como base nos colocar a prova de nossos conhecimentos das ferramentas usadas no site. A ideia inical é criarmos um PDV nível <strong>basico</strong>, com opção de venda dos produtos, uma área de estoque, despesa e por fim uma aba de relatórios. 

Nossa ideia mais para frente é ir melhorando esse projeto a fim de ficar o mais completo possível. 

<h3> Ferramentas Usadas </h3> 

A base de todo o site é feita pelo framework Django; usamos, claro, HTML para estrutura; para estilização CSS e Bootstrap 5.0; para armazenar os dados usamos o SQLite; e outras ferramentas como: JQuery, Ajax e CDNs para criação rápida de tabela e outros recursos. Por fim, as duas linguagens de programação foram Python e JavaScript.

Agora, iremos falar um pouco do site.


# Login

Tela básica para acessar o PDV (User: admin ; PassWord: admin), ela não possui um sistema de autenticação é somente uma aba de "apresentação".


# Vendas

Aqui é onde se faz as vendas (Nesse caso, o banco de dados está povoado com dados de uma lanchonete que vende salgados). 

---> Na parte direita, temos 3 inputs, sendo que o input de Código e o input de Nome eles se autocompletam a fim de aumentar a fluidez da venda. Temos, também, a parte da quantidade do produto que será vendido. A quantidade está ligada direto com o estoque, caso não possua o produto que você queira vender, não irá aparecer ele na aba de escolha. Para adicionar o item na tabela, precisamos clicar no botão "Adicionar Item" e para finalizar a compra, cliquemos no botão "Finalizar Compras" (Assim que clicado aparecerá um modal de troco junto a forma de pagamento). Por fim, temos o botão "Fechar Caixa", esse botão é para ser usado quando o user fechar o estabelecimento e sabe que não haverá mais vendas no dia. Esse botão é super importante ser clicado, já que é ele que enviará as informações para a aba relatório.

---> Na parte do meio, temos uma lista de produtos que estão sendo colocados no carrinho, depois de ter clicado, na parte direita, em 'Adicionar Item'. Logo, na parte final tem a visualização de quanto está ficando a compra do cliente.

---> Na parte esquerda possui a sidebar para navegação entre as abas.


# Estoque

---> Essa parte serve para analisar o que há no estoque, bem como adicionar novos produtos, editar, ou deletar. Você pode pesquisar da forma que quiser, por quantidade, por nome, por preço e por código. Há também botões para criação de PDF da tabela, exportar a lista para o Excel, copiar a lista, bem como imprimir.

---> Temos os dois botões superiores um para adicionar item outro para editar em lote. 

---> O botão de adiconar item possui esses inputs básicos, sendo o "diferencial" a parte de "Tipo Produto", é ele que faz a edição de preço ser rápida, dependendendo da situação.

---> É nesse modal que faz a mudança de preço dos produtos de uma forma rápida.


# Contas a Pagar

---> Aqui também é baseado em tabelas, adicionamos as despesas quanto a nome, quantidade, custo, tipo de gasto e caso precise, notas. Na parte superior à direita, temos a soma dos tipos de gasto (Semanal, Mensal ou Esporádico). Para finalizar, há um botão ao lado de 'Adicionar Despesa', chamado 'Finalizar Despesa' é nele que fará a ligação dessa tabela com a parte de ralatório; assim que clicado todas as despesas serão apagadas para novas despesas seguintes assumirem a tabela.


# Relatórios

---> Aqui você possui três inputs. Darei o exemplo do primeiro input, ele nos leva para o relatório de vendas de um dia XX/XX/XXXX; Por isso, é de extrema importância que assim que o user finalize seu dia de vendas, clique no botão 'Fechar Caixa', pois é ele que fará o reletório e é aqui que ele verá o que foi vendido, bem como outras informações (Mesma lógica para despesas).

---> Uma vez selecionada a data, você clique em 'Procurar', você será levado para uma outra página, é nela que estão as informações do dia, como produtos vendidos, quantidade usada de cada forma de pagamento e por fim o faturamento.


# Algumas Imagens

![image](https://user-images.githubusercontent.com/98958613/204900084-a8d5eb05-c63c-4c95-9d1e-dfe0e3e050f7.png)
![image](https://user-images.githubusercontent.com/98958613/204900146-d381c7ce-f0df-440e-a299-6060785f5851.png)
![image](https://user-images.githubusercontent.com/98958613/204900424-067d1604-489e-4697-ab8c-87c7e483028f.png)
![image](https://user-images.githubusercontent.com/98958613/204900178-0900fbbb-0701-41a0-a282-75f6ec1d930a.png)
![image](https://user-images.githubusercontent.com/98958613/204900230-506f4014-7d5a-40b3-8a0c-92780816e10e.png)
![image](https://user-images.githubusercontent.com/98958613/204900588-e2d40368-d9d5-46f3-8717-68e7f2417ce6.png)


# Criadores

<h3> Matheus Bon e Carlos Eduardo </h3> 



