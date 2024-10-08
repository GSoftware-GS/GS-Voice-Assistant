# Import necessary modules
import pyttsx3
from threading import Thread
import time
import alexa
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set the voice to use for speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    """
    Synthesizes speech from the given text using a text-to-speech engine.

    :param text: The text to synthesize speech for.
    """
    engine.say(text)
    #engine.stop()  # Stop any previous audio before starting new audio
    print("runandwait")

    talk_thread = Thread(target=engine.runAndWait)
    talk_thread.start()
    
    talk_thread.join(5)
    print("runandwait terminado")
    if alexa.parar_evento.is_set():
        print("parar_evento")
        engine.endLoop()
        engine.stop()
        sys.exit()


    # Close the engine instance

# def talk_thread(text):
#     """
#     Synthesizes speech from the given text using a text-to-speech engine in a separate thread.

#     :param text: The text to synthesize speech for.
#     """
    
#     hilo_talk = Thread(target=talk, args=(text,))
#     hilo_talk.start()
#     hilo_talk.join(5)
#     print("hilotalk"+str(hilo_talk.is_alive()))

