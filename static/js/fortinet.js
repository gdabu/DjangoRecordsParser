
$(document).ready(function() {


    // 
    // Make an AJAX request whenever the refresh button is clicked. 
    // 
    $("#table-refresh").click(function() {

        $("select.form-control option:selected").each(function() {

            var selection = $(this).text();
            var periodType = null;
            var periodVal = null;

            if (selection == "24 hours") {

                periodType = "hours";
                periodVal = 24;

            } else if (selection == "7 days") {

                periodType = "days";
                periodVal = 7;

            } else if (selection == "4 weeks") {

                periodType = "weeks";
                periodVal = 4;

            }

            $.ajax({
                url: "http://localhost:8000/renderer/period/?periodType=" + periodType + "&periodVal=" + periodVal,
                dataType: 'json',
                success: function(records) {
                    $("#records-table tbody").empty()
                    $("#records-table thead tr th i").remove();
                    for (var i = 0; i < records.length; i++) {
                        $("#records-table tbody").append('<tr class="' + records[i].rating + '"><td>' + records[i].date + '</td><td>' + records[i].filename + '</td><td>' + records[i].action + '</td><td>' + records[i]["submit-type"] + '</td><td>' + records[i].rating + '</td></tr>')
                    }
                    $("#threat-alert").hide();
                },
                failure: function(data) {
                    console.log(data)
                }
            })

        })
    })

    // 
    // Poll the server to see if there are new records
    // 
    setInterval(function() {

        $("select.form-control option:selected").each(function() {
            var selection = $(this).text();
            var periodType = null;
            var periodVal = null;

            if (selection == "24 hours") {

                periodType = "hours";
                periodVal = 24;

            } else if (selection == "7 days") {

                periodType = "days";
                periodVal = 7;

            } else if (selection == "4 weeks") {

                periodType = "weeks";
                periodVal = 4;

            }

            current_records_amt = $("#records-table tbody tr").length;

            $.ajax({
                url: "http://localhost:8000/renderer/poll/?periodType=" + periodType + "&periodVal=" + periodVal,
                dataType: 'json',

                success: function(new_records_amt) {
                    if (new_records_amt != current_records_amt) {
                        $("#threat-alert").show();
                    }
                },
                failure: function(data) {
                    console.log(data)

                },
                timeout: 2000
            });

        })
    }, 10000);


    // 
    // Make an AJAX request whenever a period is selected from the drop down
    // 
    $(".form-control").change(function() {
        $("select.form-control option:selected").each(function() {

            var selection = $(this).text();
            var periodType = null;
            var periodVal = null;

            if (selection == "24 hours") {

                periodType = "hours";
                periodVal = 24;

            } else if (selection == "7 days") {

                periodType = "days";
                periodVal = 7;

            } else if (selection == "4 weeks") {

                periodType = "weeks";
                periodVal = 4;

            }

            $.ajax({
                url: "http://localhost:8000/renderer/period/?periodType=" + periodType + "&periodVal=" + periodVal,
                dataType: 'json',
                success: function(records) {
                    $("#records-table tbody").empty()
                    $("#records-table thead tr th i").remove();
                    for (var i = 0; i < records.length; i++) {
                        $("#records-table tbody").append('<tr class="' + records[i].rating + '"><td class="records-date">' + records[i].date + '</td><td class="records-filename">' + records[i].filename + '</td><td class="records-action">' + records[i].action + '</td><td class="records-submit-type">' + records[i]["submit-type"] + '</td><td class="records-rating">' + records[i].rating + '</td></tr>')
                    }
                },
                failure: function(data) {
                    console.log(data)
                }
            });

        });
    });

});
