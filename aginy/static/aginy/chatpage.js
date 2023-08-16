$(document).ready(function(){
    $('#chat-form').on("submit", function (event) {
        event.preventDefault()
        $.ajax({
            type: 'POST',
            url: {% url 'chat' %},
            data: $(this).serialize()
        });
    });
})