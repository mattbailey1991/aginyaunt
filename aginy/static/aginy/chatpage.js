$(document).ready(function(){
    $('#chat-form').submit(function (event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: "",
            data: $(this).serialize(),
            success: function(response) {
                $(this).trigger('reset');
            }
        });
    });
})