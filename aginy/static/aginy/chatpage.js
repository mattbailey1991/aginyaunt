$(document).ready(function(){
    
    function update_page(messages) {
        for (var message in messages) {
            $("#message-area").append("<p>"+message.role+": "+message.content+"</p")
        }
    }
    
    messages = "{{ messages }}";
    console.log(messages);
    update_page(messages);
    
    $('#chat-form').submit(function (event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: "",
            data: $(this).serialize(),
            success: function(response) {
                $('#chat-form').trigger('reset');
                var messages = response["messages"];
                update_page(messages);
            }
        });
    });
})