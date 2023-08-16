
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from aginy.chatbot import OpenAIBot

# Create your views here.
def index(request):
    return render(request, "aginy/index.html", {})

def chatpage(request):
    apikey = settings.OPENAI_API_KEY
    bot = OpenAIBot(apikey)
    prompt = request.POST.get("prompt")
    completion = bot.chat(prompt)
    messages = bot.messages[1:]
    return render(request, "aginy/chat.html", {'messages': messages})