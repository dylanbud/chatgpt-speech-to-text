# Whisper Chatbot

The Whisper Chatbot is a simple voice-based chatbot that uses the ChatGPT model to generate responses to user inputs.

## Requirements

- Python 3.6 or higher
- PyAudio
- Colorama
- HuggingFace API key
- homebrew for OSX
- brew install pyaudio may be required
- pip install pyaudio may be required
- playwright may be required after chatgpt install


The Whisper Chatbot uses the [HuggingFace Whisper-Tiny API](https://api-inference.huggingface.co/models/openai/whisper-tiny) for speech-to-text transcription.

- Follow the instructions here to configure ChatGPT with Playwright:  https://github.com/mmabrouk/chatgpt-wrapper

## Usage

To use the Whisper Chatbot, you will need to obtain an API key from HuggingFace. To do this, go to the [HuggingFace website](https://huggingface.co/) and sign up for an account. Once you have an account, go to the "Models" section and search for the "Whisper-Tiny" model. Click on the model to see the details, and then click on the "Create a new model" button. Give your model a name, and click on the "Create" button. This will generate an API key that you can use with the Whisper Chatbot.

Once you have an API key, you can add it to the script by replacing the `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` placeholder in the following line of code with your actual API key:

```python
headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
```

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
* recording for 2 seconds
* done recording
Starting ... Done
You:  Apple.

ChatGPT: Apple is a multinational technology company that designs, develops, and sells consumer electronics, computer software, and online services. The company's best-known hardware products include the iPhone, iPad, and Mac personal computers. Apple's software includes the macOS and iOS operating systems, the iTunes media player, and the Safari web browser. The company also offers online services such as the iCloud cloud storage service and the Apple Music streaming service.

##################################################

Success!

Read the above response...
Enter a time for the next window of wav recording, that is an even number and press enter to continue when ready; to exit, press Ctrl+C

Enter the duration in seconds. And hit enter twice. Type n or 'exit' to quit:  

```



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
