"""
    This file defines the Speak class that is used to speak the chatbot's response
"""


import pyttsx3


class Speak:
    """ Speak Class
    This class is used to speak the chatbot's response"""
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 360)
        self.engine.setProperty('volume', 0.8)

    def speak(self, text):
        """ Speak the text
        :param text: The text to speak
        """
        self.engine.say(text)
        self.engine.runAndWait()
