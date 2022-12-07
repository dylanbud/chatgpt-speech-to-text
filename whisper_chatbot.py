"""
    This file will be used to run the chatbot
    It will use the record.py file to record the user's input
    It will use the speak.py file to speak the chatbot's response
"""

import json
import colorama
from pychatgpt import Chat
from record import SpeechRecognizer
from speak import Speak

#### Using whisper-small.en, you can select a whisper model from the list of models here:
# https://huggingface.co/models?filter=whisper ####

### Use your Authorization Bearer token to replace the xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# in config.json ###
### You can also choose a different whisper model by changing the API_URL in config.json ###
### Make sure to generate a new token if you are switching whisper models on HuggingFace ###

config = json.load(open("config.json", encoding="utf-8"))

API_URL = config['API_URL']
TOKEN = config['TOKEN']
headers = {"Authorization": "Bearer "+ TOKEN}

chat = Chat(email=config['email'], password=config['password'])
listen = SpeechRecognizer()
speak = Speak()

speech = input("Do you want to enable speech? (y/n) ")
if speech == "y":
    SPEAK_ENABLED = True
else:
    SPEAK_ENABLED = False

print(colorama.Fore.RED + "Say something to chatbot! I am listening right now!\n"
+ colorama.Fore.RESET)

while True:
    # Listen for user input
    prompt = listen.listen()
    print(colorama.Fore.RED + "Activated\n" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "First prompt understood and sent\n" + colorama.Fore.RESET)
    print(f"Recognized: {prompt}")
    resp = chat.ask(prompt)
    response = resp
    print(colorama.Fore.MAGENTA + "Response received\n" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "###############\n" + colorama.Fore.RESET)
    print(colorama.Fore.YELLOW + "Response: " + response + "\n" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "###############\n" + colorama.Fore.RESET)
    # Speak the response if the user has enabled it with
    if SPEAK_ENABLED:
        speak.speak(response)
        print(colorama.Fore.GREEN + "Response spoken\n" + colorama.Fore.RESET)
    # Ask the user if they want to continue
    while True:
        user_input = input("Do you want to continue (y/n)? ")
        if user_input == "y":
            print(colorama.Fore.CYAN + "Please speak your additional prompt to chatbot..."
            + colorama.Fore.RESET)
            break
        elif user_input == "n":
            print("Exiting program")
            exit()
