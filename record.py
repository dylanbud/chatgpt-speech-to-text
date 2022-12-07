""" Record audio from microphone and save to file
"""

#!/usr/bin/env python3

import time

import speech_recognition as sr


class SpeechRecognizer:
    """ SpeechRecognizer Class"""
    def __init__(self, ambient_duration=2):
        self.recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=ambient_duration)

    def listen(self, model="base.en"):
        """ Listen to the microphone and return the recognized text"""
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

        try:
            t_time = time.time()
            text = self.recognizer.recognize_whisper(audio, language="english", model=model)
            time_parsing = time.time() - t_time
            if time_parsing > 2:
                print(f"Recognized in {time.time() - t_time} seconds."
                      f"See https://github.com/openai/whisper#available-models-and-languages.")

            return text

        except sr.UnknownValueError:
            print("Whisper could not understand audio")
        except sr.RequestError as _:
            print("Could not request results from Whisper")
