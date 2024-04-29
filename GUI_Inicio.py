'''Este es una interfaz de bienvenida al sistema, 1era version -  Aun no contiene Logica'''
import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk

class GUIInicio:
    def __init__(self, master):
        self.master = master
        self.master.title("Bienvenid@")
        self.master.geometry("600x700") #Ancho x Alto
        self.master.configure(bg='#f0f0f0')

        self.label_welcome = tk.Label(master, text="Bienvenid@ al Sistema de Trabajos de Titulación",
                                      font=("Arial", 16), bg='#f0f0f0')
        self.label_welcome.pack(pady=20)

        self.btn_login = tk.Button(master, text="Ingresar", font=("Arial", 12), command=self.open_login_window) #Ya contiene la llamda a open_login_window
        self.btn_register = tk.Button(master, text="Registrarse", font=("Arial", 12), command=self.register)
        self.btn_about = tk.Button(master, text="Acerca de", font=("Arial", 12), command=self.about)

        self.btn_login.pack(pady=10)
        self.btn_register.pack(pady=10)
        self.btn_about.pack(pady=10)

        self.image = Image.open(r"Imagenes/escom.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(master, image=self.photo)
        self.label.image = self.photo  # mantener la referencia
        self.label.pack()

    def open_login_window(self):
        login_window = Toplevel(self.master)
        login_app = VentanaAcceso(login_window)

    def register(self):
        messagebox.showinfo("Registro", "Lógica de Registro Aquí")

    def about(self):
        messagebox.showinfo("Acerca del sistema", "Recuerda que para acceder es importante que tengas un registro previo, prueba el boton 'Ingresar' o si ya cuentas con un registro da click en 'Acceder'. Puedes comunicarte al tel: 55 5462 6374")

class VentanaAcceso:
    def __init__(self, master):
        self.master = master
        self.master.title("Acceso")
        self.master.geometry("300x200")

        self.label_usuario = tk.Label(master, text="Usuario:")
        self.label_usuario.pack(pady=5)

        self.entry_usuario = tk.Entry(master)
        self.entry_usuario.pack(pady=5)

        self.label_password = tk.Label(master, text="Contraseña:")
        self.label_password.pack(pady=5)

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack(pady=5)

        self.btn_aceptar = tk.Button(master, text="Aceptar", command=self.validar_acceso)
        self.btn_aceptar.pack(pady=10)

        self.btn_cancelar = tk.Button(master, text="Cancelar", command=master.destroy)
        self.btn_cancelar.pack(pady=10)

    def validar_acceso(self):
        # Aqui se implementa la logica de acceso con la base, aun no la contiene pero ya tiene los metodos 
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        print("Usuario:", usuario)
        print("Contraseña:", password)
        

def start_gui():
    root = tk.Tk()
    app = GUIInicio(root)
    root.mainloop()

if __name__ == "__main__":
    start_gui()
