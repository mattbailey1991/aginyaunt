
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core import serializers
from aginy.chatbot import OpenAIBot
import json

def index(request):
    return render(request, "aginy/index.html", {})

def chatpage(request):
    # If user submits a new prompt on the chatpage via AJAX, send request to OpenAI API and return messages
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if request.method == "POST" and is_ajax:
        apikey = settings.OPENAI_API_KEY
        bot = OpenAIBot(apikey, request.session['messages'])
        prompt = request.POST.get("prompt")
        bot.chat(prompt)
        request.session['messages'] = bot.messages[1:]
        ser_messages = json.dumps(request.session['messages'])
        return JsonResponse({'messages': ser_messages}, status = 200)

    # Otherwise, initialise a new chatbot, send request to OpenAI API and return messages
    else:    
        apikey = settings.OPENAI_API_KEY
        bot = OpenAIBot(apikey)
        prompt = request.POST.get("prompt")
        bot.chat(prompt)
        request.session['messages'] = bot.messages[1:]
        return render(request, "aginy/chat.html", {'messages': request.session['messages']})