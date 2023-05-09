import openai
import os

openai.api_key = os.getenv('OPENAI_KEY')

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0.8,
    max_tokens = 2000,
    messages = [
        {"role": "system", "content": "You are a funny comedian who tells dad jokes."},
        {"role": "user", "content": "Write a dad joke related to numbers."},
        {"role": "assistant", "content": "Q: How do you make 7 even? A: Take away the s."},
        {"role": "user", "content": "Write one related to programmers."}
        ]
)