$(document).ready(function () {
    $("#table thead tr")
        .clone(true)
        .addClass('filters')
        .appendTo('#table thead');

    var table = $('#table').DataTable({


        // Configuração de tradução
        language: {
            url: 'https://cdn.datatables.net/plug-ins/1.12.1/i18n/pt-BR.json'
        },

        // Configuração geral das tabelas
        paging: true,
        pageLength: 10,
        lengthChange: true,
        autoWidth: false,
        searching: true,
        bInfo: true,
        bSort: true,
        orderCellsTop: true,


        // Configuração de exclusão de filtros em colunas
        "columnDefs": [{
            "targets": [4, 5],
            "orderable": false,

        }],

        initComplete: function(){
            var api = this.api();

            //Configuração de quais colunas receberão o filtro
            api
                .columns([0 , 1 , 2 , 3 ])
                .eq(0)
                .each(function(colIdx){

                    var cell = $('.filters th').eq(
                        $(api.column(colIdx).header()).index()
                    );

                    var title = $(cell).text();
                    $(cell).html('<input type="text" placeholder="' + title + '"/>');

                    $(
                        'input',
                        $('.filters th').eq($(api.column(colIdx).header()).index())
                    )
                    .off('keyip change')
                    .on('keyup change' , function(e){
                        e.stopPropagation();

                        $(this).attr('title', $(this).val());
                        var regexr = '({search})';

                        var cursorPosition = this.selectionStart;

                        api
                            .column(colIdx)
                            .search(
                                this.value != ''
                                    ? regexr.replace('{search}', '(((' + this.value + ')))')
                                    : '',
                                this.value != '',
                                this.value == ''
                            )
                        .draw();

                    $(this)
                        .focus()[0]
                        .setSelectionRange(cursorPosition , cursorPosition);
                    });

                });

        },
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
                    columns: [1 , 2 , 3 ]
                },
            },

            {
                //Botão Excel
                extend: 'excel',
                text: "<i class='bx bx-file'></i>",
                className: 'btn btn-secondary',
                titleAttr: 'Excel',
                exportOptions: {
                    columns: [1 , 2 , 3 ]
                },
            },

            {
                //Botão Impressão
                extend: 'print',
                text: "<i class='bx bx-printer'></i>",
                className: 'btn btn-secondary',
                titleAttr: 'Imprimir',
                exportOptions: {
                    columns: [1 , 2 , 3 ]
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
                    columns: [1 , 2 , 3 ]
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
