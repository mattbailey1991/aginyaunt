$(document).ready(function(){
    
    console.log(messages)
    messages = JSON.parse(messages.replace(/&quot;/g,'"'));
    console.log(messages)
    console.log(messages[0].role)
    function update_page(messages) {
        let i = 0;

        while (i < messages.length) {
            $("#message-area").append("<p>"+messages[i].role+": "+messages[i].content+"</p")
            i++;
        }
    }
    
    console.log(messages)
    update_page(messages);
    
    $('#chat-form').submit(function (event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: "",
            data: $(this).serialize(),
            success: function(response) {
                $('#chat-form').trigger('reset');
                $("#message-area").html("")
                messages = response["messages"];
                messages = JSON.parse(messages.replace(/&quot;/g,'"'))
                update_page(messages);
                console.log(messages)
            }
        });
    });
})