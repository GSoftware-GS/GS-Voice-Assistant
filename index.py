import tkinter as tk
from threading import Thread
from alexa import run
import alexa
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

encendido = True

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("480x720")
        
        self.title("Asistente virtual")
        
        
        self.start_button = customtkinter.CTkButton(self, text="Iniciar", command=self.on_start)
        self.start_button.pack()

        self.exit_button = customtkinter.CTkButton(self, text="Salir", command=self.on_exit)
        self.exit_button.pack()

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
        hilo = Thread(target=run)
        hilo.start()

    def on_exit(self):
        
        global hilo
        global encendido
        # Detiene el hilo de ejecución
        alexa.encendido = False
        # Cierra la ventana raíz
        self.destroy()

    def on_send(self):
        text = self.text_input.get()
        print(f"Enviando texto: {text}")


app = App()
app.mainloop()