import wave
import pyaudio
import requests
import json
import threading
import time
import keyboard
import colorama
from dotenv import load_dotenv
from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"TOKEN": "foo", "EMAIL": "foo@example.org"}

TOKEN = config["TOKEN"]


# Function that continuously checks for changes to the audio wav file
def check_for_changes():
  # Get the current version of the audio wav file
  current_version = get_current_version_of_audio_wav("output.wav")
  
  # Continuously check for changes to the audio wav file
  while True:
    # Check if the audio wav file has been updated
    updated_version = get_current_version_of_audio_wav("output.wav")
    if updated_version != current_version:
      # If the audio wav file has been updated, perform the desired check
      current_version = updated_version
      check_audio_wav(updated_version)
    
    # Sleep for a short amount of time before checking again
    time.sleep(0.1)

# Start the thread that checks for changes to the audio wav file
import requests

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-tiny"
headers = {"Authorization": "Bearer " + TOKEN}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

output = query("output.wav")


def transcribe_recording(filename):
    # Define a function to query the speech-to-text model with the given file
    def query(filename):
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.request("POST", API_URL, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))
        # Return the transcription result
    return query(filename)["text"]

    # Query the speech-to-text model with the recording
    output = query(filename)

    # Print the transcription result
    print(output)

    # Return the transcription result
    return output

def record(chunk, format, channels, rate, record_seconds, wave_output_filename):
    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print(colorama.Fore.BLUE + "* recording for " +str(record_seconds) + " seconds" + colorama.Fore.RESET)


    frames = []

    for i in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
       

    print(colorama.Fore.GREEN + "* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(wave_output_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

print("Welcome to the Whisper Chatbot! Press Ctrl+C to exit.")

record(1024, pyaudio.paInt16, 2, 44100, 2, "output.wav")
transcribe_recording("output.wav")

output = query("output.wav")

#return output["text"]


from chatgpt_wrapper import ChatGPT

chatbot = ChatGPT()

def get_response(message):
    return chatbot.ask(message)

while True:
    output = query("output.wav")
    inp = input(colorama.Fore.CYAN + "You: " + str(output['text']))
    response = chatbot.ask(inp + (output['text']))
    #parse the response on nice lines
    print(colorama.Fore.YELLOW + "\nChatGPT: " + response + "\n" + colorama.Style.RESET_ALL)
    print(colorama.Fore.LIGHTMAGENTA_EX+ "##################################################" + "\n" + colorama.Style.RESET_ALL)

 
    #await response
    #await asyncio.sleep(0.1)
    print(colorama.Fore.GREEN + "Success!" + "\n"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.RED + "Read the above response..." + "\n" + "Enter a time for the next window of wav recording, that is an even number and press enter to continue when ready; to exit, press Ctrl+C" + "\n" +colorama.Style.RESET_ALL)
    duration = input("Enter the duration in seconds. And hit enter twice. Type " + colorama.Fore.RED + 'n' + colorama.Style.RESET_ALL + " or " + colorama.Fore.BLUE + "'exit' " + colorama.Style.RESET_ALL + "to quit: ")
    duration = int(duration)
    choice = input()
    if choice == 'n' or choice == 'exit':
        break
    else:
        record(1024, pyaudio.paInt16, 2, 44100, duration, "output.wav")
        transcribe_recording("output.wav")





# if __name__ == "__main__":
#     interface = gr.Interface(fn=get_response, inputs=gr.inputs.Textbox(
#         lines=5, label="You"), outputs=gr.outputs.Textbox(label="chatGPT"))
#     interface.launch()