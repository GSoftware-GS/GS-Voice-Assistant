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

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..JYNF4K15M5nsNt1a.dbPxqMEVJEOrJCd261Iqhwe2WWV7oX36M4UT2vRkyKKvWUIN-q9fBa7xV9bKDLxHK-jtsWSiQ0JnmF61slZy1ryEJH-y_pjusowXlqjLPqhzegkESeqvWS8Yv0k-Ib2GfexIm2F8BPz7tjoVdSFB2dh7Ndg3S_6FwzzeRt0-mm0Bwkp2Q_dhZoZ0Q-kZdIFvmZvfrqEoih7wh8frSCtyaMw-LhIE8Yq5WYX0tH4r0u3bH9nhFj_gTboE-94cjiJOE0EHocVrvp7g_SYTqfJc2H1YFkcHcQHUJ0j0K5jYmqux5Kr2rzXM8XaFFBuLDK03wYAVXhCj0PUAZwDVlDIYDxDFIZm4EHsL0g6g3_nF1Z-zgk-4NIhwNnjvTNacd5SPoLbUFuk-Nl8XoTJrmFkr7w2VKZhek1se8B4ns1QEMc2rCJNVhP5Mmv_dGhYZzodjPqh0q59-odkFD-HwR7LxZ3pgdOEvpEagLz_HtDT53j1qEwUuLJrQpi4LgOrJKR-Br_cJmYLMd3DPvXW2vJlXuV99F4_dw26iol1xjGwMQbM96D5o7oqlbK0iiRFf9AzyCw-P6NWtw4UCKIF7ZEvUwSYUmBjvXvGUCG_l2TcJRoqclvlW6Lp2B41Ddmntb2lKZYes0qEhgZpm1q6NOVRpW3txnUdXtf1i0mSOXF_7jEKPCC0C9hIqy3CQ2z_Osp-Bu8BoWYb3vvHSelo2J0awLEwm0ermPntG8ooh-H-ghtTNeDEnCnqZ1awTUP3WJxNeZlyc7Dh2gD3Yeqb8GGufwcH5XwQQ3wt4IDxxpDDi_nxiBlY7ana7c6UkvGSPUN1yaJXScNcDRNCtpqwXgI0S4fYPdpstmHAR50uMWNEuzYeu8d-T6VmaS6KfCi-F1Zz81Ay2HSXheolI6aw-5fPrTOoE4upIzoZIxeRtBohlMdm5yizbhtepZzihgBRRnBlGAiwACYClN51dZBTMgItwsGHoeyxH6m-N6OHYuSW5j1dSCktq7opOxY-5rWMaJ1cvzJvV_DVPdEHywP-QF9ekVZb2udOlBaDIfJKL8DN1nxRJd0qvppx6pMbzjo2_0lkTZiAMgDY5sHTpbL0KgmRMNAL1oSmMDCgxO6AcTrLBX0B2Gq9Xy88lKXWJ-4OVzqcQPIWPPCcrh8J8Viq9qMBmy_MQjrOOQNC0syR3iXVD7Qb39KYX63NaLTDnMGl8Ef-En4MqoN-1r87bzBZFg6QfZOjTyfwvTUoCh07-Y7VXBH9nAxGAaIl84739PQ1ybDkH-ZNEKQjBNDI44xKBGUguVZGnpUtIOrQUBxdFImuzRmVt8Gc0RJ_cDr1E1-sOrkTuQkNt2hWKG0VHmXBR4vfdElDkf4Sz3EhWk29kNMktWq41Gi7Ulu4KwlpcnerWPrn3Ec5HWyUx0ERs06pQs9Jt8Ta-tVZAbkwyWpiwa4dFuVWfwIP_6xFR-3XvSH2qK3ymUuGw1-WWrRilpacbJG2D8xz04PhNVp_P8Di1W4shzKIKP1EqtCfeMw00mofHoKwttb4eAZ6iV4RTx76PGVtLCpA2qKPc5NofnCC39zjhKWaV4Lx61SmSaEvpqgxf04KOz6x2KvIXFT9z4AUBM29Vyy1NVvWaEHVray9d71BxLHJ1esXD2WHo_U13QzDE-LWJA6OzxuctClhEwEsoBCvVUMZY8xFfWjLyQOUDsV4VusxH7rMd3jDrnuBFwnFRfAfBhRH5JvMRJBGZRQwfAEFHayVgFQb1-53Rpc0z4yYZZY7dlSjXl4_56Yytb_cRsBWqhrveqozSY3ynFo3bT2tTNAzWNfb4HON3f8KlzxiFwyeozkkYv6o0Z2M9AuOUWQC0xVGANwbbtNAqVQZZoBmx019uKy3nQ7szR7r5RIIvR9m4sikvKJXVWTD9rYuzhSrOCFdrOD81Rw_SYabMin5IAoIJ2bLDFQm40FcBfB3Tf0slc0nHIal7z-CCjxkx77DzgCZdgM7YiI9s6-WZIzbguEZBjtD9GEIu2C0lU-YNmTkwl99OqdM2_YfYH_ufuOTT1LwjvnLj42NjUY7fFdEIfQDYwteZlphf9G_DKuu_LU-WcdB_UgZ-rel-5hOH19jYoDWFpFJq5HvxkOHecIDFTK5X0EgaVm7bP5o6lJbjGhW1ar1qqtUxNfJsIyfwDk2QVFc5d4xK4Al9jc4RZVBZVattaYOp1kV-O8DLemhQweBxcPbLS7l8skWXBtTBAFKJDc4aU4GNpqtm1C4xq-blrIy3sQo-fK0h-O4QvA9A5m79RBzsQUpzpV8.wC-bXwYaHwRg7DFtoq5Oqg'  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
api = ChatGPT(session_token)  # auth with session token


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
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            print ("rec:"+rec)
            if nombre in rec:
                rec = rec.replace(nombre, '')
                talk(rec)
                print(rec)
                return rec
                
            else:
                #listen()
                pass

    except:
        print("Excepcion")
        listen()


def run(encendido):
    
    encendido = encendido
    
    while encendido:
    
        if not encendido:
            return False

        rec = listen()
        #rec = input("Input: ")
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
            resp = ask(rec)
            print(resp)
            talk(resp["message"])