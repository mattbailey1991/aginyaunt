from django.conf import settings
from django.db import models
 
class ChatHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    datetime = models.DateTimeField("Date and time of chat")
    title = models.CharField("Chat title", max_length=50)
    content = models.TextField("Message history")