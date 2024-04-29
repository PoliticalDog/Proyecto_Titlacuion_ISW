'''Este es una interfaz de bienvenida al sistema, 1era version - funcional pero plana'''
#Biblioteca para la GUI
import tkinter as tk
from tkinter import messagebox
#Biblioteca para manipluacion de imagenes
import tkinter as tk
from PIL import Image, ImageTk

class GUIInicio: 
    def __init__(self, master):
        #sel.master sera mi forma para especificar mis widgets "Botonoes, labels, etc"
        self.master = master
        self.master.title("Bienvenid@") #Titulo de la ventana
        self.master.geometry("600x400") 
        self.master.configure(bg='#f0f0f0')

        self.label_welcome = tk.Label(master, text="Bienvenid@ al Sistema de Trabajos de Titulación",
                                      font=("Arial", 16), bg='#f0f0f0')
        self.label_welcome.pack(pady=20)

        self.btn_login = tk.Button(master, text="Ingresar", font=("Arial", 12), command=self.login)
        self.btn_register = tk.Button(master, text="Registrarse", font=("Arial", 12), command=self.register)
        self.btn_about = tk.Button(master, text="Acerca de", font=("Arial", 12), command=self.about)

        self.btn_login.pack(pady=10)
        self.btn_register.pack(pady=10)
        self.btn_about.pack(pady=10)

        #  iMAGEN
        self.image = Image.open(r"Imagenes/escom.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        # Mostrar la imagen usando un Label        
        self.label = tk.Label(master, image=self.photo)
        self.label.image = self.photo  # mantener la referencia
        self.label.pack()


    def login(self):     #Boton Acceder
        messagebox.showinfo("Login", "Lógica de Inicio de Sesión Aquí")

    def register(self):  #Boton Registrar
        messagebox.showinfo("Registro", "Lógica de Registro Aquí")

    def about(self):     #Boton Acerca de
        messagebox.showinfo("Acerca del sistema", "Recuerda que para acceder es importante que tengas un registro previo, prueba el boton 'Ingresar' o si ya cuentas con una cuenta da click en 'Acceder'. Puedes comunicate al tel: 55 5462 6374")

def start_gui():        #inicializador
    root = tk.Tk()
    app = GUIInicio(root)
    root.mainloop()

if __name__ == "__main__":
    start_gui() 
