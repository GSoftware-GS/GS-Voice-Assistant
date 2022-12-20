import tkinter as tk
from threading import Thread
from alexa import run,stop
import alexa
import customtkinter
import time
import sys

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

hilo = Thread(target=run)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("480x720")
        
        self.title("Asistente virtual")
        
        self.title_text = customtkinter.CTkLabel(master=self,
                                              text="GSoftware - GSChat")  # font name and size in px
        self.title_text.pack()
        
        self.name_output_text = customtkinter.CTkLabel(master=self, text=alexa.nombre)  # font name and size in px
        self.name_output_text.pack()
        
        self.start_button = customtkinter.CTkButton(self, text="Iniciar", command=self.on_start)
        self.start_button.pack()
        
        self.exit_button = customtkinter.CTkButton(self, text="Salir", command=self.on_exit)
        self.exit_button.pack()

        self.name_text = customtkinter.CTkLabel(master=self,
                                              text="Nombre de tu Asistente")  # font name and size in px
        self.name_text.pack()
        
        self.text_input = customtkinter.CTkEntry(self)
        self.text_input.pack()

        self.send_button = customtkinter.CTkButton(self, text="Enviar", command=self.on_send)
        self.send_button.pack()
        
        
        self.start_button.place(x=200, y=100)
        self.exit_button.place(x=200, y=120)
        self.text_input.place(x=200, y=140)
        self.send_button.place(x=200, y=160)
        
        
        self.start_button.pack(pady=10, side=tk.TOP)
        self.exit_button.pack(pady=10, side=tk.TOP)
        self.send_button.pack(pady=10, side=tk.BOTTOM)
        self.text_input.pack(pady=50, side=tk.BOTTOM)
        
        

    def on_start(self):
        print("Iniciando...")
        global hilo
        print("Iniciando Jarvis")
        # Crea un nuevo hilo de ejecución que ejecuta el código de alexa
        # Pasando la variable encendido como argumento
        
        hilo.start()

    def on_exit(self):
        
        global hilo
        global encendido
        # Detiene el hilo de ejecución
        alexa.stop()
        if hilo is not None:
            print("Apagando...")
            while hilo.is_alive():
                print(alexa.parar_evento.is_set())
                time.sleep(1)
            
            
        print ("Hilo detenido")
        # Cierra la ventana raíz
        self.destroy()
        print("Cerrando...")
        sys.exit()
        print("Noexit")

    def on_send(self):
        global nombre
        text = self.text_input.get()
        print(f"Nombre cambiado a {text}")
        self.name_output_text.configure(text=text)
        alexa.nombre = text
        


app = App()
app.mainloop()



