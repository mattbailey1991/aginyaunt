
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core import serializers
from aginy.chatbot import OpenAIBot
from aginy.dbmanager import save_chat, get_all_chats, get_chat_history
import json
import datetime as dt

def index(request):
    return render(request, "aginy/index.html", {})


def chatpage(request):
    # Sends prompt to OpenAI API, then updates message history in session and returns to client   
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    apikey = settings.OPENAI_API_KEY
    action_type = request.POST.get("action-type")

    # Reset messages if page was reloaded
    if not is_ajax and action_type != "view":
        request.session['messages'] = []

    # Get message history and chat time if page accessed from chat history
    if action_type == "view":
        chat_id = request.POST.get("chat-id")
        chat_history = get_chat_history(chat_id)
        if chat_history.user == request.user:
            request.session['messages'] = json.loads(chat_history.content)
            request.session['chat_start_time'] = chat_history.datetime.strftime("%d/%m/%Y, %H:%M:%S")
        else:
            response = render(request, "404.html")
            response.status_code = 404
            return response

    # Get username
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Guest"
    
    # Initialises an OpenAI bot using message history 
    bot = OpenAIBot(apikey, request.session['messages'])
    if action_type == "chat":
        prompt = request.POST.get("prompt")
        bot.chat(prompt)
    
    # Updates message history in session and dumps into a JSON file for JavaScript processing and saving to database 
    request.session['messages'] = bot.messages[1:]
    request.session['ser_messages'] = json.dumps(request.session['messages'])
    
    # If page is a new chat, save chat to database and render HTML
    if not is_ajax and action_type == "chat":
        request.session["chat_start_time"] = dt.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        if request.user.is_authenticated:
            save_chat(request)
        return render(request, "aginy/chat.html", {'messages': request.session['ser_messages'], 'username': username})
    
    # If prompt submitted from page via AJAX, save chat to database and return the JSON file 
    elif is_ajax:
        if request.user.is_authenticated:
            save_chat(request)
        return JsonResponse({'messages': request.session['ser_messages']}, status = 200)
    
    # If accessing from chat history, just render history 
    elif action_type == "view":
        return render(request, "aginy/chat.html", {'messages': request.session['ser_messages'], 'username': username})
    

def history(request):
    chat_history = get_all_chats(request)
    return render(request, "aginy/history.html", {'chat_history': chat_history})