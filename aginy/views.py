
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core import serializers
from aginy.chatbot import OpenAIBot
import json

def index(request):
    return render(request, "aginy/index.html", {})

def chatpage(request):
    # Sends prompt to OpenAI API, then updates message history in session and returns to client   
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    apikey = settings.OPENAI_API_KEY
    # Reset messages if page was reloaded
    if not is_ajax:
        request.session['messages'] = []
    # Initialises an OpenAI bot using message history
    bot = OpenAIBot(apikey, request.session['messages'])
    prompt = request.POST.get("prompt")
    bot.chat(prompt)
    # Updates message history in session and dumps into a JSON file for JavaScript processing 
    request.session['messages'] = bot.messages[1:]
    ser_messages = json.dumps(request.session['messages'])
    # If first time on page, render HTML
    if not is_ajax:
        return render(request, "aginy/chat.html", {'messages': ser_messages})
    # Otherwise, if prompt submitted from page, return the JSON file 
    else:
        return JsonResponse({'messages': ser_messages}, status = 200)
    