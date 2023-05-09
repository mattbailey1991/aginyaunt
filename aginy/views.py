
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    apikey = settings.OPENAI_API_KEY
    return render(request, "aginy/index.html", {"apikey" : apikey})
