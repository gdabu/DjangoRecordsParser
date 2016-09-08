function sortTable(columnNumber) {
    var rows = $('#records-table tbody  tr').get();
    rows.sort(function(a, b) {

        var A = $(a).children('td').eq(columnNumber).text().toUpperCase();
        var B = $(b).children('td').eq(columnNumber).text().toUpperCase();

        if (A < B) {
            return -1;
        }

        if (A > B) {
            return 1;
        }

        return 0;

    });

    $.each(rows, function(index, row) {
        $('#records-table').children('tbody').append(row);
    });
}

function sortTableByDate() {
    var rows = $('#records-table tbody  tr').get();
    rows.sort(function(a, b) {

        var A = Date.parse($(a).children('td').eq(0).text().toUpperCase());
        var B = Date.parse($(b).children('td').eq(0).text().toUpperCase());

        if (A < B) {
            return -1;
        }

        if (A > B) {
            return 1;
        }

        return 0;

    });

    $.each(rows, function(index, row) {
        $('#records-table').children('tbody').append(row);
    });
}

$("#records-table thead tr th").click(function() {
    $("#records-table thead tr th i").remove();

    $(this).append('<i class="fa fa-sort pull-right"></i>');

    var thIndex = $("#records-table thead tr th").index(this);
    if (thIndex == 0) {
        sortTableByDate()
    } else {
        sortTable(thIndex)
    }
})
