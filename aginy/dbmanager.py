from aginy.models import ChatHistory
import re
import datetime as dt

def save_chat(request):
    chat_start_time = dt.datetime.strptime(request.session["chat_start_time"] ,"%d/%m/%Y, %H:%M:%S")
    try:
        chat = ChatHistory.objects.get(user = request.user, datetime = chat_start_time)
        chat.content = request.session["ser_messages"]
    except:
        first_message = request.session["messages"][0]['content']
        chat_title = re.sub(r'^(.{75}).*$', '\g<1>...', first_message)
        chat = ChatHistory(user = request.user, datetime = chat_start_time, title = chat_title, content = request.session["ser_messages"])
    
    chat.save()


def get_chat_history(request):
    return ChatHistory.objects.filter(user = request.user).order_by('-datetime').values()