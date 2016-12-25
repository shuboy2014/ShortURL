/**
 * Created by shubham on 24/12/16.
 */

$(document).ready(function () {

    $('#reset-btn').click(function () {
        $('#tobeshort').val("");
    });

    $('#short-btn').click(function () {
        var urls = ($('#tobeshort').val());
        var data = {
            "longUrls" : urls,
            "csrfmiddlewaretoken" : $('input[name="csrfmiddlewaretoken"]').val()
        };

        $.ajax({
            type : 'POST',
            url : '',
            data : data,
            dataType : 'json',
            success : function (data) {
                console.log(data);
            },
            error : function () {
                alert("failed")
            }
        });
    });
});