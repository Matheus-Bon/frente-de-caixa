$(document).ready(function () {
    $.getJSON("http://127.0.0.1:8000/json/", function (data) {
        console.log('v 1.14')
        
        // Parte que pega o JSON e transforma em um Array
        let dimension = data.data

        // Apenas os nomes dos produtos
        let listaProdutos = $.map(dimension, function (value, key) {

            return value.nome_produto
        })

        // Quantidade do estoque que vai ser alterada na hora de colocar o produto no carrinho
        let quantidade = $.map(dimension, function (value, key) {

            return value.quantidade_produto
        })

        //
        let quantidade_inicial = $.map(dimension, function (value, key) {

            return value.quantidade_produto
        })

        let lista = listaProdutos.filter( (value, key) => {
            
            if(data.data[key].quantidade_produto > 0){
                return value
            }
        })

        console.log(data.data)
        
        // Autocomplete da label 'Nome do Produto'
        $("#prod").autocomplete({
                source: lista
        })


        // Add cód/produto automaticamente 
                // Parte Cod
        $("#prod").focusout(function () {

            let sel = $("#prod").val()

            for (i = 0; i < listaProdutos.length; i++) {
                if(data.data[i]['quantidade_produto'] > 0){
                    if (sel == data.data[i]['nome_produto']) {

                        sel = data.data[i]['id']

                        $("#cod").val(sel)
                    }
                } else {
                    listaProdutos.splice(i, 1)
                }
            }
        })

                // Parte Cod
        $("#cod").focusout(function () {

            let sel = $("#cod").val()

            for (i = 0; i < listaProdutos.length; i++) {

                if (sel == data.data[i]['id']) {

                    sel = data.data[i]['nome_produto']

                    $("#prod").val(sel)
                }
            }


        })

        let custo = 0
        let custo_total = 0

        let table = $.map(dimension, function (value, key) {
            let item = [{
                id: value.id,
                nome_produto: value.nome_produto,
                custo: value.custo,
                quantidade_produto: 0
            }]

            return item
        })

        $("#btn-add").click(function () {
            if(lista.includes($('#prod').val()) && $('#cod').val() && $('#qtt').val()){
                let indice = listaProdutos.indexOf($('#prod').val())
                if( quantidade[indice] >= $('#qtt').val()){
                    quantidade = quantidade_inicial.slice(0)
                    table[indice].quantidade_produto += parseInt($('#qtt').val())
                    $("#sales-table").html('')
                    for(i = 0; i < table.length; i++){
                        quantidade[i] -= parseInt(table[i].quantidade_produto)
                        if(table[i].quantidade_produto > 0){
                            $("#sales-table").append(`
                            <tr id="sale-${i}">
                                <td id="id-prod-${i}">${table[i].id}</td>
                                <td id="name-prod-${i}">${table[i].nome_produto}</td>
                                <td id="custo-prod-${i}">R$ ${table[i].custo.toFixed(2)}</td>
                                <td id="qtt-prod-${i}">${table[i].quantidade_produto}</td>
                                <td><button class="btn btn-sucess text-center" id="excluir-${i}"><i class='bx bx-trash'></i></button></td>
                            </tr>
                            `)
                        custo = custo + (table[i].custo * parseInt(table[i].quantidade_produto))
                        $('#total-value').html('').append(`R$ ${custo.toFixed(2)}`)
                        }
                    }
                    custo_total = custo
                    custo = 0
                    document.getElementById('cart').value = JSON.stringify(table)
                    $('#prod').val(''), $('#cod').val(''), $('#qtt').val('')
                    for(let j = 0; j < table.length; j++){
                        $(`#excluir-${j}`).click(function () {
                            table[j].quantidade_produto = 0
                            quantidade[j] = quantidade_inicial[j]
                            console.log(table[j])
                            custo = custo + (table[j].custo * parseInt(table[j].quantidade_produto))
                            $(`#sale-${j}`).remove()
                            $('#total-value').html('').append(`R$ ${custo.toFixed(2)}`)
                            custo_total = custo
                            custo = 0
                        })}
                        console.log(quantidade)
                } else {
                    alert(`Você tem apenas ${quantidade[indice]} unidades de ${$('#prod').val()}`)
                }
            } else {
                alert('Você está esquecendo algum campo!')
            }
        })


    });


})




