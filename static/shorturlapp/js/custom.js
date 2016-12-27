/**
 * Created by shubham on 24/12/16.
 */

$(document).ready(function () {

    function test_turncate(longurl) {

        if (longurl.length > 60) {
            return true;
        } else {
            return false;
        }

    }

    $('#reset-btn').click(function () {
        $('#tobeshort').val("");
    });

    $('#short-btn').click(function () {

        var id_result = $('#result')
        var id_serialnum = $('#serial-number');
        var id_longurls = $('#longUrls');
        var id_shorturls = $('#shortUrls');


        var urls = ($('#tobeshort').val());

        var data = {
            "longUrls": urls,
            "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val()
        };

        if (id_result.css('display') == 'block') {
            id_result.slideToggle();
            id_serialnum.children("p").remove();
            id_serialnum.children("hr").remove();
            id_longurls.children("p").remove();
            id_longurls.children("hr").remove();
            id_shorturls.children("p").remove();
            id_shorturls.children("hr").remove();
        }

        $.ajax({
            type: 'POST',
            url: '',
            data: data,
            dataType: 'json',
            success: function (data) {

                var shorted_urls = JSON.parse(data["shorturls"]);
                var longurls = urls.split('\n');

                for (var url = 0; url < Object.keys(shorted_urls).length; ++url) {

                    if (longurls[url] == "") {
                        id_serialnum.append('<hr><p><i class="fa fa-thumbs-down" aria-hidden="true"></i> </p>');
                    } else {
                        id_serialnum.append('<hr><p><i class="fa fa-thumbs-up" aria-hidden="true"></i> </p>');
                    }

                    if (longurls[url] != "" && test_turncate(longurls[url])) {
                        id_longurls.append("<hr><p>" + longurls[url].substring(0, 57) + "...</p>");
                    } else {
                        if (longurls[url] == "") {
                            id_longurls.append("<hr><p><br></p>");
                        } else {
                            id_longurls.append("<hr><p>" + longurls[url] + "</p>");
                        }
                    }

                    id_shorturls.append("<hr><p>" + shorted_urls[url.toString()] + " <i class='twa twa-thumbs-up twa-1x'></i></p>");

                }

                id_serialnum.append("<hr>");
                id_longurls.append("<hr>");
                id_shorturls.append("<hr>");

                id_result.slideToggle();
            },
            error: function () {
                alert("failed")
            }
        });
    });
});