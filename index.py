import tkinter as tk
from threading import Thread
from alexa import run

encendido = True

# Crea una ventana raíz de tkinter
root = tk.Tk()
root.title("Jarvis Control")
root.geometry("300x200")

# Crea un diseño responsive para la interfaz gráfica
# Utilizando diferentes diseños para diferentes tamaños de pantalla

# Crea una variable que almacene el hilo de ejecución


# Crea una función que se llame al hacer clic en el botón Iniciar
def iniciar():
    global hilo
    print("Iniciando Jarvis")
    # Crea un nuevo hilo de ejecución que ejecuta el código de alexa
    # Pasando la variable encendido como argumento
    run(encendido)

# Crea una función que se llame al hacer clic en el botón Salir


def salir():
    encendido=False
    run(encendido)
    # Cierra la ventana raíz
    root.destroy()


# Crea un gradiente de fondo utilizando dos colores
gradient = tk.Canvas(root, width=300, height=200)
gradient.pack()
start_color = "#001f3f"
end_color = "#0074D9"
gradient.create_rectangle(0, 0, 300, 200, fill=start_color)
gradient.create_rectangle(0, 0, 300, 100, fill=end_color)

# Crea un contenedor para los botones
container = tk.Frame(gradient, bg="white")
container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Crea un botón Iniciar y lo añade al contenedor
iniciar_btn = tk.Button(container, text="Iniciar", command=iniciar,
                        bg="#0074D9", fg="white", font=("Arial", 12))
iniciar_btn.pack()

# Crea un botón Salir y lo añade al contenedor
salir_btn = tk.Button(container, text="Salir", command=salir,
                      bg="#FF4136", fg="white", font=("Arial", 12))
salir_btn.pack()

# Muestra la ventana raíz y espera a que se cierre
root.mainloop()
