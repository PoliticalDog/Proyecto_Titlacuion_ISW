import tkinter as tk
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    app = GUIInicio(root)
    root.mainloop()

class GUIInicio:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplicación con Imagen")
        self.master.geometry("600x400")

        # Cargar la imagen con una raw string para la ruta
        self.image = Image.open(r"C:\Users\godie\Documents\Proyecto_Titulacion_ISW\Gestor_Trabajos_Titulacion\Imagenes\escom.jpg")
        self.photo = ImageTk.PhotoImage(self.image)

        # Mostrar la imagen usando un Label
        self.label = tk.Label(master, image=self.photo)
        self.label.image = self.photo  # mantener la referencia
        self.label.pack()

if __name__ == "__main__":
    main()
