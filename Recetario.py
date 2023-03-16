import tkinter as tk
import csv
import json
from datetime import datetime

class RecetarioApp:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Recetario de cocina")
        
        # Definir los widgets
        self.receta_listbox = tk.Listbox(self.master, height=20, width=50)
        self.receta_listbox.grid(row=0, column=0, padx=10, pady=10)
        self.receta_listbox.bind('<<ListboxSelect>>', self.mostrar_receta)
        
        self.receta_dia_label = tk.Label(self.master, text="Receta del día:", font=("Helvetica", 16))
        self.receta_dia_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.receta_dia_frame = tk.Frame(self.master, width=200, height=200)
        self.receta_dia_frame.grid(row=2, column=0, padx=10, pady=10)
        
        self.crear_receta_button = tk.Button(self.master, text="Crear receta", command=self.crear_receta)
        self.crear_receta_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        
        self.editar_receta_button = tk.Button(self.master, text="Editar receta", command=self.editar_receta)
        self.editar_receta_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        
        self.eliminar_receta_button = tk.Button(self.master, text="Eliminar receta", command=self.eliminar_receta)
        self.eliminar_receta_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")
        
        self.buscar_label = tk.Label(self.master, text="Buscar receta:", font=("Helvetica", 12))
        self.buscar_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        self.buscar_entry = tk.Entry(self.master, width=30)
        self.buscar_entry.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.buscar_entry.bind('<KeyRelease>', self.buscar_receta)
        
        # Cargar las recetas desde un archivo csv o json
        self.recetas = self.cargar_recetas_desde_archivo("recetas.csv")
        
        # Mostrar las recetas en la lista
        self.actualizar_lista_recetas()
        
        # Mostrar la receta del día
        self.mostrar_receta_del_dia()
        
    def cargar_recetas_desde_archivo(self, archivo):
        # Cargar las recetas desde un archivo csv o json
        recetas = []
        if archivo.endswith('.csv'):
            with open(archivo, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # saltar la primera fila (cabecera)
                for row in reader:
                    recetas.append
