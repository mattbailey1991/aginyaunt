
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core import serializers
from aginy.chatbot import OpenAIBot
from aginy.dbmanager import save_chat
import json
import datetime as dt

def index(request):
    return render(request, "aginy/index.html", {})

def chatpage(request):
    # Sends prompt to OpenAI API, then updates message history in session and returns to client   
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    apikey = settings.OPENAI_API_KEY
   
    # Reset messages if page was reloaded
    if not is_ajax:
        request.session['messages'] = []
    
    # Get username
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Guest"
    
    # Initialises an OpenAI bot using message history
    bot = OpenAIBot(apikey, request.session['messages'])
    prompt = request.POST.get("prompt")
    bot.chat(prompt)
    
    # Updates message history in session and dumps into a JSON file for JavaScript processing and saving to database 
    request.session['messages'] = bot.messages[1:]
    request.session['ser_messages'] = json.dumps(request.session['messages'])
    
    # If first time on page, save chat to database and render HTML
    if not is_ajax:
        request.session["chat_start_time"] = dt.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        if request.user.is_authenticated:
            save_chat(request)
        return render(request, "aginy/chat.html", {'messages': request.session['ser_messages'], 'username': username})
    
    # Otherwise, if prompt submitted from page, save chat to database and return the JSON file 
    else:
        if request.user.is_authenticated:
            save_chat(request)
        return JsonResponse({'messages': request.session['ser_messages']}, status = 200)
    