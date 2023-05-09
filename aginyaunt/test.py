import os
import openai
from dotenv import load_dotenv

class OpenAIBot:
    def __init__(self):
        # Sets API key and provides initial system message to bot
        load_dotenv("api.env")
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.messages = [
            {"role": "system", "content": 
             "You are a coding tutor bot to help user write and optimize python code."
             },
        ]

    def chat(self, message):
        self.messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
        return response["choices"][0]["message"]