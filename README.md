# Whisper Chatbot

The Whisper Chatbot is a simple voice-based chatbot that uses the ChatGPT model to generate responses to user inputs.

## Requirements

The following packages are required to run the Whisper Chatbot:

    Python 3.6 or higher
    PyAudio
    Colorama
    HuggingFace API key
    homebrew for OSX (if using OSX)
    brew install pyaudio (if using OSX)
    pip install pyaudio (if using OSX)
    playwright (if using OSX)

## Usage

To use the Whisper Chatbot, you will need to obtain an API key from HuggingFace. To do this, go to the [HuggingFace website](https://huggingface.co/) and sign up for an account. Once you have an account, go to the "Models" section and search for the "Whisper-Tiny" model. Click on the model to see the details, and then click on the "Create a new model" button. Give your model a name, and click on the "Create" button. This will generate an API key that you can use with the Whisper Chatbot.

In the latest version of the code, the API key is no longer hardcoded in the script and instead is stored in a config.json file. This allows for easier management of the API key, as well as the ability to use different API keys for different environments (e.g. development and production).

To use your API key with the Whisper Chatbot, you will need to add it to the config.json file. The file should look like this:

{
  "api_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

Simply replace the xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx placeholder with your actual API key, and save the file. The Whisper Chatbot will then use this API key to access the HuggingFace Whisper-Tiny API.

Note that you will need to obtain an API key from HuggingFace as described in the Usage section of the README.

Including a screenshot section:

Whisper Chatbot screenshot

The goal of this code is to create a voice-based chatbot that uses the ChatGPT model to generate responses to user inputs. The chatbot uses the HuggingFace Whisper-Tiny API for speech-to-text transcription, and allows users to interact with the chatbot by speaking to it. The chatbot will transcribe the user's speech and generate a response based on the ChatGPT model.

We recommend using a virtual environment to manage the dependencies for the Whisper Chatbot. To create a virtual environment and install the necessary packages, you can use the following commands:

# Create a virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate

# Install the dependencies using the requirements file
pip install -r requirements.txt

To run the Whisper Chatbot, simply run the whisper_chatbot.py script using the python command:

python whisper_chatbot.py


This will start the Whisper Chatbot, and you can start talking to it by pressing the Ctrl+C key combination to exit the program.

## Example Output

``` python Welcome to the Whisper Chatbot! Press Ctrl+C to exit.

Logging in...
Do you want to enable speech? (y/n) y
Say something to chatbot! I am listening right now!

Recognized in 2.646164894104004 seconds
Activated

First prompt understood and sent

Recognized:  What's the capital of Spain?
Conversation ID: 
Parent ID: 
Response received

###############

Response: The capital of Spain is Madrid.

###############

Response spoken

Do you want to continue (y/n)? y
Please speak your additional prompt to chatbot...
