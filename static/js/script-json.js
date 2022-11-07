$(document).ready(function () {
    $.getJSON("http://127.0.0.1:8000/json/", function (data) {

        
        // Parte que pega o JSON e transforma em um Array
        var dimension = data.data

        var listaProdutos = $.map(dimension, function (value, key) {

            return value.nome_produto
        })

        let quantidade = $.map(dimension, function (value, key) {

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

        let tabela = []

        $("#btn-add").click(function () {
            if(lista.includes($('#prod').val()) && $('#cod').val() && $('#qtt').val()){
                let indice = listaProdutos.indexOf($('#prod').val())
                if( quantidade[indice] >= $('#qtt').val()){
                    console.log('Bob Jeff')
                    let obj = {
                        nome: $('#prod').val(),
                        codigo: $('#cod').val(),
                        quantidade: $('#qtt').val()
                    }
                    tabela.push(obj)
                    console.log(tabela)
                    $("#sales-table").html('')
                    for(i = 0; i < tabela.length; i++){
                        $("#sales-table").append(`
                        <tr id="sale-${i}">
                            <td>${tabela[i].codigo}</td>
                            <td>${tabela[i].nome}</td>
                            <td>${tabela[i].quantidade}</td>
                            <td><button id="excluir-${i}"><i class='bx bx-trash'></i></button></td>
                        </tr>
                        `)
                        // $(`#excluir-${i}`).click(function () {
                        //     tabela.splice((i-1), 1)
                        //     console.log(tabela)
                        //     $(`#sale-${i}`).remove()
                        // })
                    }
                } else {
                    alert(`Você tem apenas ${quantidade[indice]} unidades de ${$('#prod').val()}`)
                }
            } else {
                alert('Você está esquecendo algum campo!')
            }
        })






    });


})




