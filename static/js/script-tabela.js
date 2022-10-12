$(document).ready( function(){
    $('#example').DataTable({
        // Configuração geral das tabelas
        paging: true,
        pageLength: 10,
        lengthChange: true,
        autoWidth: true,
        searching: true,
        bInfo: true,
        bSort: true,
        

        // Configuração de exclusão de filtros em colunas
        "columnDefs": [{
            "targets": [5 , 6],
            "orderable": false,

        }],

        // Botões PDF - Excel - Print - Cópia
        dom: '.lBfrtip',
        buttons: [
            {
                //Botão Cópia
                extend: 'copy',
                text: "<i class='bx bx-copy'></i>",
                className: 'btn btn-secondary',
                titleAttr: 'Copiar tabela',
                exportOptions: {
                    columns: [ 0 , 1 , 2 , 3 , 4]
                },
            },

            {
                //Botão Excel
                extend: 'excel',
                text: "<i class='bx bx-file'></i>",
                className: 'btn btn-secondary',
                titleAttr: 'Excel',
                exportOptions: {
                    columns: [ 0 , 1 , 2 , 3 , 4]
                },
            },

            {
                //Botão Impressão
                extend: 'print',
                text: "<i class='bx bx-printer'></i>",
                className: 'btn btn-secondary',
                titleAttr: 'Imprimir',
                exportOptions: {
                    columns: [ 0 , 1 , 2 , 3 , 4]
                },

                //Customização da Fonte para impressão
                customize: function (win){
                    $(win.document.body).css('font-size', '10pt')
                    $(win.document.body).find('table')
                        .addClass('compact')
                        .css('font-size', 'inherit')
                }

            },

            {
                //Botão PDF
                extend: 'pdf',
                text: "<i class='bx bxs-file-pdf'></i>",
                className: 'btn btn-secondary',
                titleAttr: 'PDF',
                exportOptions: {
                    columns: [ 0 , 1 , 2 , 3 , 4]
                },

                //Configuração da tabela no PDF
                tableHearder: {
                    alignment: 'center'
                },
                customize: function (doc){
                    doc.styles.tableHeader.alignment = 'center'
                    doc.styles.tableBodyOdd.alignment = 'center'
                    doc.styles.tableBodyEven.alignment = 'center'
                    doc.styles.tableHeader.fontSize = 7
                    doc.defaultStyle.fontSize = 6 

                    doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('')
                }
            
            },
        ]

    })
})


 