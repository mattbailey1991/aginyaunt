$(document).ready(function(){
    
    // Parse the JSON messages file
    console.log(messages)
    messages = JSON.parse(messages.replace(/&quot;/g,'"').replace(/"role": "assistant"/g,'"role": "Aginy Aunt"').replace(/"role": "user"/g,'"role":"' + username +'"'));
    console.log(messages)

    // Adds all messages to the message area
    function update_page(messages) {
        let i = 0;

        while (i < messages.length) {
            $("#message-area").append("<div class=\"msg-item-area\"><p class=\"msg-item\">"+messages[i].role+": "+messages[i].content+"</p></div>")
            i++;
        }
    }
    
    // Regular expression check for aginy aunt message
    function is_agi(msg) {
        re = /^Aginy Aunt:/
        return re.test(msg)
    }

    // Classifies each message as either user or aginy aunt
    function add_message_class() {
        $.each($(".msg-item"), function() {
            if (is_agi($(this).text())) {
                $(this).addClass("agi-msg");  
            }
            
            else {
                $(this).addClass("user-msg")
            }
        });
    }

    // Updates messages on first load
    update_page(messages);
    add_message_class();
    
    // Sends prompt to server, then refreshes message area
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
                messages = JSON.parse(messages.replace(/&quot;/g,'"').replace(/"role": "assistant"/g,'"role": "Aginy Aunt"').replace(/"role": "user"/g,'"role":"' + username +'"'));
                update_page(messages);
                add_message_class();
            }
        });
    });
})