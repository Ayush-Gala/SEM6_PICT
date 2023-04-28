import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('SECRET_KEY') #getting the api-key from env file

messages = []
message = ""
print("SAY HELLO TO YOUR NEW FRIEND!\n\n")
while(message != "exit"):
    message = str(input("Human: "))
    messages.append({"role":"user", "content":message})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = completion["choices"][0]["message"]["content"]
    messages.append({"role":"assistant", "content":reply})
    print("\nAI: " + reply + "\n")