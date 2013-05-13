$(function() {
    if ("WebSocket" in window) {
        ws = new WebSocket("ws://" + document.domain + ":8000/websocket");
        ws.onmessage = function (msg) {
            var message = JSON.parse(msg.data);
            $("ul#entries").append("<li>" + message.output + "</li>");
        };
    };

    $('#chat_form input[name=text]').focus();

        $("#chat_form").on('submit', function(e){
        e.preventDefault();

        var input = $('#chat_form input[name=text]');
        var message = $(input).val();


        $.get("/addsong", { idsong: message})
        .done(function(data) {
            $(input).val('');
        }).fail(function(xhr, status, error) {
            console.error(error)
            alert("No no no no" + status + "\nError: " + error);
        });
    });

//    $("#chat_form").on('submit', function(e){
//        e.preventDefault();
//
//        var input = $('#chat_form input[name=text]');
//        var message = $(input).val();
//        $(input).val('');
//
//        ws.send(JSON.stringify({'output': message}));
//    });

    window.onbeforeunload = function() {
        ws.onclose = function () {};
        ws.close()
    };
});

