# Whisper Chatbot

The Whisper Chatbot is a simple voice-based chatbot that uses the ChatGPT model to generate responses to a users voice input.

## Requirements

The following packages are required to run the Whisper Chatbot:

    Python 3.6 or higher
    PyAudio
    Colorama
    HuggingFace
    homebrew for OSX (if using OSX)
    brew install pyaudio (if using OSX)
  

## Installation

To install the dependencies, run the following command:

    pip3 install -r requirements.txt

  
## Usage

To run the Whisper Chatbot, simply run the following command:

    python3 whisper_chatbot.py

Depending on the length of the prompt, the chatbot may take a few seconds to generate a response. The chatbot will also speak the response to the user if the user has enabled speech. The user can also enable speech by typing "y" when prompted. Please note that the chatbot will not speak the response if the user has not enabled speech, and when speaking, will only speak the response, not the prompt. The user can continue the conversation after the assistant has completed speaking.

It will take some moments for the speech to be picked up and transformed by Whisper, and also some time for ChatGPT to process the request, so please be patient. Start with smaller 2-3 word prompts to test it out at first.

## Example 
```
Do you want to enable speech? (y/n) y
Say something to chatbot! I am listening right now!

Recognized in 2.482357740402222 seconds - maybe try using a small model. See https://github.com/openai/whisper#available-models-and-languages.
Activated

First prompt understood and sent

Recognized:  Apple.
Response received

###############

Response: Apple is a multinational technology company that designs and sells consumer electronics, computer software, and online services. The company's best-known hardware products include the iPhone, the iPad, the Mac, and the iPod. Apple's software includes the macOS and iOS operating systems, the iTunes media player, and the App Store, among others. The company also offers online services such as iCloud, Apple Music, and the Apple Store. Apple was founded in 1976 by Steve Jobs, Steve Wozniak, and Ronald Wayne, and is headquartered in Cupertino, California.

###############

Response spoken

Do you want to continue (y/n)? n
Exiting program
```

## License

See LICENSE.md for more information.