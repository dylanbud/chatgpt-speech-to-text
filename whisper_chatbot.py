from revChatGPT.revChatGPT import Chatbot
import json
import colorama
from record import SpeechRecognizer
from speak import Speak
from dotenv import load_dotenv
import os

# Load the API key from the .env file
load_dotenv()
API_KEY = os.environ.get("API_KEY")

#### Using whisper-tiny.en, you can select a whisper model from the list of models here: https://huggingface.co/models?filter=whisper ####

### Use your API KEY to replace the xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx below ###


API_URL = "https://api-inference.huggingface.co/models/openai/whisper-tiny.en"
headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}


config = json.load(open("config.json"))
chatbot = Chatbot(config, conversation_id=None)
chatbot.refresh_session() # You need to log in on the first run

listen = SpeechRecognizer()

speak = Speak()

speech = bool(input("Do you want to enable speech? (y/n) ") == "n")

def get_chat_response(self, prompt, output="text"):
    return {'message':message, 'conversation_id':self.conversation_id, 'parent_id':self.parent_id}

print(colorama.Fore.RED + "Say something to chatbot! I am listening right now!\n" + colorama.Fore.RESET)
while True:
    # Listen for user input
    prompt = listen.listen()
    print(colorama.Fore.RED + "Activated\n" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "First prompt understood and sent\n" + colorama.Fore.RESET)
    print(f"Recognized: {prompt}")
    print (f"Conversation ID: {chatbot.conversation_id}")
    print (f"Parent ID: {chatbot.parent_id}")
    resp = chatbot.get_chat_response(prompt)
    response = resp['message']
    print(colorama.Fore.MAGENTA + "Response received\n" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "###############\n" + colorama.Fore.RESET)
    print(colorama.Fore.YELLOW + "Response: " + response + "\n" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "###############\n" + colorama.Fore.RESET)
    # Speak the response if the user has enabled it with
    speak.speak(response)
    print(colorama.Fore.GREEN + "Response spoken\n" + colorama.Fore.RESET)
    # Ask the user if they want to continue
    while True:
        user_input = input("Do you want to continue (y/n)? ")
        if user_input == "y":
            print(colorama.Fore.CYAN + "Please speak your additional prompt to chatbot..." + colorama.Fore.RESET)
            break
        elif user_input == "n":
            print("Exiting program")
            exit()