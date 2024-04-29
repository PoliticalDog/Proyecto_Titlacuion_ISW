'''
Ventana Principal 20/04/2024
Versión 1
'''

# Bibliotecas
import psycopg2
import pandas as pd
import sys

import tkinter as tk
import tkinter as tk

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import Label, ttk
from psycopg2 import Binary
from PIL import Image, ImageTk
from io import BytesIO

# Clase principal
class ventanaPrincipal:

    # Conexión a la base de datos y creación de la ventana principal (Constructor)
    def __init__(self, root):
        # Conexión a la base de datos
        try:
            db_params = {
                'dbname': 'ttitulacion',
                'user': 'postgres',
                'password': 'divar#63$divar',
                'host': '192.168.1.69',
                'port': '5432'
            }
            
            self.connection = psycopg2.connect(**db_params)
            print("\nConexión exitosa!\n")

        except psycopg2.Error as e:
            print(f"\nError al conectarse a PostgreSQL: {e}\n")
            sys.exit(1)

        self.cursor = self.connection.cursor()

        # TKinter
        self.root = root
        self.root.title("Trabajos de Titulación")
        self.root.geometry("1200x600")
        self.root.resizable(False, False)
        self.root.iconbitmap("Imagenes/ESCOM_logo.ico")
        self.root.configure(bg='#A6B5FF')

        self.configInicial()

    def configInicial(self):
        pass

# Ejecución de la función principal
if __name__ == "__main__":
    root = tk.Tk()
    app = ventanaPrincipal(root)
    root.mainloop()
