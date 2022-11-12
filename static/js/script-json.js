$(document).ready(function () {
    $.getJSON("http://127.0.0.1:8000/json/", function (data) {
        console.log('v 1.11')
        
        // Parte que pega o JSON e transforma em um Array
        var dimension = data.data

        var listaProdutos = $.map(dimension, function (value, key) {

            return value.nome_produto
        })

        let quantidade = $.map(dimension, function (value, key) {

            return value.quantidade_produto
        })

        let quantidade_inicial = $.map(dimension, function (value, key) {

            return value.quantidade_produto
        })

        let gasto = $.map(dimension, function (value, key) {

            return 0
        })

        let gasto_inicial = $.map(dimension, function (value, key) {

            return 0
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

            var sel = $("#prod").val()

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

            var sel = $("#cod").val()

            for (i = 0; i < listaProdutos.length; i++) {

                if (sel == data.data[i]['id']) {

                    sel = data.data[i]['nome_produto']

                    $("#prod").val(sel)
                }
            }


        })

        let table = $.map(dimension, function (value, key) {
            let item = [{
                id: value.id,
                nome_produto: value.nome_produto,
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
                        gasto[i] += parseInt(table[i].quantidade_produto)
                        if(table[i].quantidade_produto > 0){
                            $("#sales-table").append(`
                            <tr id="sale-${i}">
                                <td id="id-prod-${i}">${table[i].id}</td>
                                <td id="name-prod-${i}">${table[i].nome_produto}</td>
                                <td id="qtt-prod-${i}">${table[i].quantidade_produto}</td>
                                <td><button class="btn btn-sucess text-center" id="excluir-${i}"><i class='bx bx-trash'></i></button></td>
                            </tr>
                            `)
                        }
                    }
                    for(let k = 0; k < quantidade.length; k++){
                        quantidade[k] -= gasto[k]
                    }
                    let ultimo_gasto = gasto.slice(0)
                    gasto = gasto_inicial.slice(0)
                    for(let j = 0; j < table.length; j++){
                        $(`#excluir-${j}`).click(function () {
                            table[j].quantidade_produto = 0
                            $(`#sale-${j}`).remove()
                            for(let k = 0; k < quantidade.length; k++){
                                quantidade[k] += ultimo_gasto[k]
                            }
                        })}
                } else {
                    alert(`Você tem apenas ${quantidade[indice]} unidades de ${$('#prod').val()}`)
                }
            } else {
                alert('Você está esquecendo algum campo!')
            }
        })


    });


})




