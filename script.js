

function appendChatbotMessage(message) {
    var chatbotMessage = $('<div class="chatbot-message"></div>');
    var chatbotText = $('<span class="typing"></span>').appendTo(chatbotMessage);
    var characters = message.split('');
    var delay = 70; // Delay in milliseconds between each character

    chatbotMessage.appendTo('#chatbot-response');

    $.each(characters, function(index, char) {
        setTimeout(function() {
            chatbotText.text(chatbotText.text() + char);
        }, delay * index);
    });

    setTimeout(function() {
        chatbotText.removeClass('typing');
        $(".chat-body").scrollTop($(".chat-body")[0].scrollHeight);
    }, delay * characters.length);
}

var isChatOpen = false;

function toggleChatContainer() {
    if (isChatOpen) {
        $(".chat-container").addClass("minimized");
        isChatOpen = false;
    } else {
        $(".chat-container").removeClass("minimized");
        isChatOpen = true;
    }
}

$(".chat-container").mouseenter(function() {
    $(".chat-container").removeClass("minimized");
});


$(".chat-container").mouseleave(function() {
    if (!isChatOpen) {
        $(".chat-container").addClass("minimized");
    }
});

$(document).ready(function() {
    $(".chat-container").addClass("minimized");
});

$('form').on('submit', function(event) {
    event.preventDefault();
    var userMessage = $('input[name="user_message"]').val();
    $('#chatbot-response').append('<div class="user-message">' + userMessage + '</div>');
    $.ajax({
        url: "{{ url_for('get_response') }}",
        method: 'POST',
        data: $('form').serialize(),
        success: function(response) {
            appendChatbotMessage(response);
            $('form')[0].reset();
        }
    });
});