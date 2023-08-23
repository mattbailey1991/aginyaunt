$(document).ready(function() {
    function fetch_history(id) {
        $('#chat-id').val(id)
        $('#history-form').trigger("submit")
    }

    $('#history-table tbody td').on("click", function() {
        var id = parseInt($(this).siblings('th').text())
        fetch_history(id)
    })
})