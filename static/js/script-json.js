

$(document).ready(function(){

    $.getJSON("http://127.0.0.1:8000/get/ajax/validate/produto", function (data) {
        console.log(data);
        $.each(data.produtos, (i, r) => {
            $("#prod").append(
                '<option value="' + r.id + '">' + r.nome_produto + ' (R$ 2,50) <option>'
            )
        });
    
        $("#prod").select2()
    });
    $("#prod").on('change', () => {
        let s = $("#prod option:selected");
        console.log(s.text(), s.val());
    })

})









