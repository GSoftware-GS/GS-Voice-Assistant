import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import csv
import random
import webbrowser
import os
from pyChatGPT import ChatGPT
from threading import Thread, Event
import threading
from talk import talk, talk
import sys

global encendido 
encendido = True
nombre = 'alexa'
global hilo

parar_evento = threading.Event()

listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def ask(prompt):
    response = api.send_message(prompt)

    return response


def listen():
    global encendido
    if not encendido:
            exit()
    else:
        try:
            with sr.Microphone() as source:
                print("Escuchando...")
                talk(text="Escuchando...")
                voice = listener.listen(source = source, timeout=5, phrase_time_limit=5)
                rec = listener.recognize_google(voice, language='es-ES')
                rec = rec.lower()
                print ("rec:"+rec)
                if nombre in rec:
                    rec = rec.replace(nombre, '')
                    talk(rec)
                    print(rec)
                    
                    return rec
                else:
                    print("No has dicho mi nombre")
                    return("No has dicho mi nombre")
                
            
        except Exception as e:
            print("Excepcion: ")
            print(e)
            return("no te he entendido")


def run():
    
    global encendido
    
    
    
    while not parar_evento.is_set():
        rec = listen()
        print("run: "+str(parar_evento.is_set()))
        if type(rec) == str:
            print("estoi en listen")
            if 'reproduce' in rec:
                print("Inicializando reproducción")
                music = rec.replace('reproduce', '')
                print('Reproduciendo')
                talk('Reproduciendo ' + music)
                pywhatkit.playonyt(music)

            elif 'hora' in rec:
                hora = datetime.datetime.now().strftime('%I:%M %p')
                talk("Son las " + hora)
            elif 'busca' in rec:
                order = rec.replace('busca', '')
                try:
                    info = wikipedia.summary(order, 1)
                except wikipedia.exceptions.PageError as e:
                    print("No se ha encontrado la página")
                    talk("No se ha encontrado la página")
                    continue
                
                talk(info)

            elif 'chiste' in rec:

                with open("chistes.txt") as f:

                    content = f.read()
                    cadena = content
                    separador = "-"
                    separado_por_espacios = cadena.split(separador)

                    tam = 0
                    for j in separado_por_espacios:
                        tam += 1

                    i = random.randint(0, tam-1)

                    print(separado_por_espacios[i])
                    talk(separado_por_espacios[i])

            elif "donde esta" in rec:
                location = rec.replace('donde esta', '')
                webbrowser.open("https://www.google.es/maps/place/" +
                                location + "/&amp;")
            
            elif 'terminar' in rec:
                parar_evento.set()

            elif 'abre' in rec:

                aplication = input("abre: ")
                #aplication = rec.replace('abre', '')
                aplication = aplication.replace(" ", "")
                print("Aplicación " + aplication)
                try:
                    os.system("open -a " + aplication + ".app")
                except Exception as e:
                    print("No se ha encontrado la aplicación")
                    talk("No se ha encontrado la aplicación")

            else:
                print("No entiendo lo que dices")
                talk("No entiendo lo que dices")
    print("Adios alexa")
    sys.exit()
    
def stop():
    # Establece la bandera de parar_evento a True para detener el hilo
    parar_evento.set()