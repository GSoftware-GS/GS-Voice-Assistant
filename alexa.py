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

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..9GLG8p2l9VcvZ8lL.eUSm8DnWX-i08ithfJnCi91oh0Mtby2N26z5s9XuBOCAAiDvQ1bdPq2qg1QMzDLcQ3XEcyeEHr5s2o-XY8jlGVYUtoiF61MkcSWi0NzW-0ZH3RWw0e5AB2RGmZdaxTJPx2ZQMMQ4YbetfPSpQSvv1miMBw9_JPhqWO477mZRCndUbhFYjmdBSDZPJqcfWOvdmtF9Ap2ijZf6exPcnfAJvNqvYxEqlxNjUfDxteswXi9vST3WY5XlKufky_88nYPS6HRvVvhAcyO1i74KiPIM_6ZKTKmBtEoKDgOs98DTiTKWb-5mZVA3YmY45Ran1XD6xMyeTGu6K7SWM_bCj_3uZI9or4YhJ4lZqJXmxz0vAkuN2AeLImkgBsrwzshCdJTFcIi_I7aKSIyHcMdxp5FLXFDu-yWVNKxMg1Gz8QDol-ed8ghdI_kNviAHr8INWGqtpLeIVgVCjZODOn8GM7T1TOR2lkK9y8_x5a1qzQSgrZKbOJswEEBTG9Nx3WGFwlBwtCU6pDFcHnjJdwA7qy9VqqTdA9jYU5BTN1mbEMkBowkyPu6xTP6RU_iiJQfrmbT6AJfsmhg_M_ccgMCxoWLsygFpA-Ld7va0cMbv-l0yRB1NOKsaddtEunk4iJWOYafznAjtpO-EcRBsc5XWgFLnPSGFS8xjOPZ5XaVbz56ksA5ydVTQ2ubzHIjO_aCuMOilLb34l5wXuq27HjlqF5_WEhWeAC87RVUDdkJocRdmp9mEcjZaxJS14WJk_LVgtQoeGwxA1knOiHYVQxQcDDMExiDU1Frf8tA5q-aGnx-q0N6G6nF6EtqR9w4sNWS2x1_Km-Ebqjm_jneJua9lhZkfB7HdyBVSRSTEgHesSH0xTeh3GyPd0EacA2zE5Obqgxr3bE1HN8oEdI35M_GRXVsYV4a7scIbzZBUCHGPBkKFc_3waNyAxn4mFI3ZJqXoMyDQk4vXyfO1IGGF_umYOz9QPbef3fSieGtkpAfSbMrZQi43z_9-rF2pWuc4h01dYT1OW8izxmV1a1gotzGpAAUoyBXsdpITTgtspswCzXRIskDFqKl7W6QtqjMVPRoHAzYB5ZsxAKaOPPBZOz8cHXdTj9p_6wAbedPikpvDNauwbY5tpdSxFDlL9-D7xGe5yc_xdnu8d5G1vQA2_b-FKftBcLVxlZtBSQdA1ogj22y3TMP22O1uinWmuZffdZzpLjd8_AfrjtEKFP-G_VmhnB-8n6fcf8IV5nErRWc16JWcBX75eDBtoqO9hGO4-gWFiMvm1KxrgYlpECaxcXvX3iwHEOIEQ0VaBOs5MSaXbOrnpR-L-bvhRiYHHbfwRjTxp6yHgTQjRdHLKy6pEYOekJ0dZpqCLzZf1KPOD6Wve6rpVL5H6AFHEZfuSVnfb6G5vfQP2DRv9yjY2HbEqQKZ-at-6ILcJth8MzM_NDDI087qvQZ0gpanEcMNCORPhpjvPo35gtsoJuIkDz8LdarYuzLd-fPAgbRCdL4V4lIS3vrnXBM6-t1u7x96DiTcz1IpO1X88hlwYZfY5fmR29gA2iO4w_kSy9crsL0mZjF6diDR5hQPakRAPQZXna8e0u503nnn7OUN_NSZqyPULtL5o3SL_vucsEOfpJ_QHbXrLE92SpZav2ZOghVF_8fTLjtzYiYUMEi9uxUywOuQuOYLt0yyPzFshBIolgrwT6CeJ2cb_1G_3qvwQzrCz0k-Yy41cFMQL-C2ZwA9_UUXhQmAmJFcqHJal2ypL5ixYgAOfPcliGtesMaktSCK0iiG2TDdFskaK_T9ieOQY9H1Evf-IH7fPAoc3H10zVkB2N7shtOZakTw9PYSvgNS9j4GH80XZa2nRx25lxbxbYjjR1_4hRtDECT5DveQf2PdUezv6AtXmmbB34H2Z4BoIXynOtoZ-KLT5diqh3DYnStqAqUZIWfDxTh4A92XNUWugBewH7okNnScFNjQk91-2vN-CzEg1i9Lx4VmnF20EkiE71Cxv4iC11fm2nMVOURUK16TIhFSLqzi7_7QSf_-3hRLJzR95_xOdGYkdPsF9zWGbuqdN-NtVDRSNnylOw-qaKRMTokM8kbZF8xMcdpPPI9MEymoiZqYjlY4jKg5QsZfylnuPK3ttwsElX8LnKT54-UMLu0CtvkghrJnd7B5O5QTa_0leTN6NE1eV04p-FCAWznY4XV1w0gShesXGLpbrpS_z-lD7mhQb8JayJPvcdonUsuN_NigIQLa-rLdSbsrRxdpXcQD3RpWGbJ1MpwJGGAgUj-hd9YK16oUElSSa9I.zzsUfwlrlxqYLHxKMDNVIg'
#try:
#    api = ChatGPT(session_token)  # auth with session token
#except Exception as e:
#    print("Error al iniciar sesión")
#    print(e)
#    exit()

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
                listen()
                

    except Exception as e:
        print("Error al escuchar")
        print(e)
        return False
        
        


def run(encendido):
    
    encendido = encendido
    
    while encendido:
    
        if not encendido:
            return False

        rec = listen()
        #rec = input("Input: ")
        print("rec:"+rec)
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
            #resp = ask(rec)
            #print(resp)
            #talk(resp["message"])
            pass