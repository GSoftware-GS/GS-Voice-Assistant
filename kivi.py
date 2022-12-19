import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from threading import Thread
import alexa

encendido = True

class App(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Inicializar atributos y configuraciones aquí
        "Asistente virtual"
        self.title_text = Label(text="GSoftware - GSChat")
        self.name_output_text = Label(text=alexa.nombre)
        self.start_button = Button(text="Iniciar", on_press=self.on_start)
        self.exit_button = Button(text="Salir", on_press=self.on_exit)
        self.name_text = Label(text="Nombre de tu Asistente")
        self.text_input = TextInput()
        self.send_button = Button(text="Enviar", on_press=self.on_send)
        
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.title_text = Label(text="GSoftware - GSChat")
        layout.add_widget(self.title_text)
        
        self.name_output_text = Label(text=alexa.nombre)
        layout.add_widget(self.name_output_text)
        
        self.start_button = Button(text="Iniciar", on_press=self.on_start)
        layout.add_widget(self.start_button)

        self.exit_button = Button(text="Salir", on_press=self.on_exit)
        layout.add_widget(self.exit_button)

        self.name_text = Label(text="Nombre de tu Asistente")
        layout.add_widget(self.name_text)
        
        self.text_input = TextInput()
        layout.add_widget(self.text_input)

        self.send_button = Button(text="Enviar", on_press=self.on_send)
        layout.add_widget(self.send_button)
        
        return layout

    def on_start(self):
        print("Iniciando...")
        global hilo
        print("Iniciando Jarvis")
        hilo = Thread(target=run)
        hilo.start()

    def on_exit(self):
        global hilo
        global encendido
        alexa.encendido = False
        print("Apagando...")
        print(alexa.encendido)
        hilo.join()
        App.get_running_app().stop()

    def on_send(self):
        global nombre
        text = self.text_input.text
        print(f"Nombre cambiado a {text}")
        self.name_output_text.text = text
        alexa.nombre = text
        

if __name__ == "__main__":
    app = App()
    app.__init__()
    app.build()