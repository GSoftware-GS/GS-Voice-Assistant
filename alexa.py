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

global encendido 
encendido = True
nombre = 'alexa'


listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)





# Hace una petición a GPT-3 utilizando el prompt definido anteriormente
def ask(prompt):
    response = api.send_message(prompt)

    return response


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    global encendido
    if not encendido:
        print("Apagado")
        exit()
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source = source, timeout=5, phrase_time_limit=5)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            print ("rec:"+rec)
            if nombre in rec:
                rec = rec.replace(nombre, '')
                talk(rec)
                print(rec)
                if isinstance(rec, str):
                    return(rec)
                else:
                    print("no es str")
                    return("no es str")
                
            else:
                print("No has dicho mi nombre")
                return("No has dicho mi nombre")

    except Exception as e:
        print("Excepcion: ")
        print(e)
        listen()


def run():
    
    global encendido
    
    if not encendido:
            exit()
            
    while encendido:
    
        

        rec = listen()
        #rec = input("Input: ")
        print(f'Has dicho: {rec}')
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
            encendido = False

        elif 'abre' in rec:

            aplication = input("abre: ")
            #aplication = rec.replace('abre', '')
            direccion = r'C:\Users\gonza\OneDrive\Escritorio'+aplication
            os.system(direccion)

        

        else:
            print("No se ha entendido la orden")
            talk("No se ha entendido la orden")
            
    print("Alexa se ha apagado")
    exit()