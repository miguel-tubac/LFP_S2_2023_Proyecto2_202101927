import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from Analizador import *

class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(
            self,
            bg="#f8f9fa",
            foreground="#343a40",
            insertbackground="#3b5bdb",
            selectbackground="blue",
            width=68,
            height=38,
            font=("Courier New", 10),
        )
        # Con esta linea activo el text area por si deseo despues desactivarlo:
    def activarTextArea(self):
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

    def desactivarTextArea(self):
        self.text.pack_forget()

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)
    

class ScrollText2(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(
            self,
            bg="#f8f9fa",
            foreground="#343a40",
            insertbackground="#3b5bdb",
            selectbackground="blue",
            width=80,
            height=38,
            font=("Courier New", 10),
        )
    # Con esta linea muestro el area de texto:
    def activarTextArea(self):
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
    #Con esta funcion quito el area de texto
    def desactivarTextArea(self):
        self.text.pack_forget()

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)
    
    # con esta funcion desabilito la edicion del area de texto
    def deshabilitarEdicion(self):
        self.text.config(state=tk.DISABLED)

    def habilitarEdicion(self):
        self.text.config(state=tk.NORMAL)

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto 2 - LFP")
        self.geometry("1200x650+70+20")
        self.scroll = ScrollText(self)
        self.scroll2 = ScrollText2(self)
        self.scroll.pack()
        self.scroll.activarTextArea()
        self.scroll2.activarTextArea()

        # Se almacena la direcion del archivo
        self.path = None

        # Utiliza pack con side para especificar el lado de empaquetado
        self.scroll.pack(side=tk.LEFT)
        self.scroll2.pack(side=tk.RIGHT)
        

        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.filemenu = Menu(self.menu)

        self.menu.add_command(label="Salir", command=self.quit)

        self.menu.add_command(label=" Abrir ", command=self.open_file)
        self.menu.add_command(label=" Analizar ", command=self.analizar_texto, state=tk.DISABLED)

        self.menu.add_cascade(label=" Reportes ▼", menu=self.filemenu, state=tk.DISABLED)
        self.filemenu.add_command(label="Rep. Tokens", command=self.mostrar_tokens)
        self.filemenu.add_command(label="Rep. Errores", command=self.mostrar_errores)
        self.filemenu.add_command(label="Árbol de derivación")


    def open_file(self):
        filepath = askopenfilename(
            filetypes=[("bizdata Files", "*.bizdata"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        
        self.scroll.delete(1.0,tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.scroll.insert(tk.END, text)
        # Se almacena la path
        self.path = filepath
        # Se muestra la direcion del archivo en la ventana
        self.title(f"Proyecto 2 - LFP - {filepath}")
        # Mensaje de ingreso de archivo correcto
        self.mostrar_infoIngresoArchivo()
        self.habilitar_botonAnalizar()

    def analizar_texto(self):
        text = self.scroll.get(1.0, tk.END)
        analizar(text)
        self.mostrar_infoAnalisisFinalizado()
        self.habilitar_botonReportes()
        # implementar el analisis

    def mostrar_tokens(self):
        text = ""
        #abilita la edicion del texto en el text area si no da error
        self.scroll2.habilitarEdicion()
        self.scroll2.delete(1.0, tk.END)
        for tok in tokens:
            # Acceder a los atributos de Token y concatenarlos como strings
            token_str = f"Token(value= '{tok.value}', Line= '{tok.line}', Col= '{tok.col}'\n"
            text += token_str

        self.scroll2.insert(tk.END, text)
        # se desavilita el area de texto
        self.scroll2.deshabilitarEdicion()

    def mostrar_errores(self):
        text = ""
        #abilita la edicion del texto en el text area si no da error
        self.scroll2.habilitarEdicion()
        self.scroll2.delete(1.0,tk.END)
        for tok in errores:
            # Acceder a los atributos de Token y concatenarlos como strings
            token_str = f'Token(Lexema= "{tok.lexema}", tipo= "{tok.tipo}", fila= "{tok.fila}", columna= "{tok.columna}")\n'
            text += token_str
        self.scroll2.insert(tk.END, text)
        # se desavilita el area de texto
        self.scroll2.deshabilitarEdicion()

    def mostrar_infoIngresoArchivo(self):
        messagebox.showinfo("Información", "Archivo Ingresado con Exito")

    def mostrar_infoAnalisisFinalizado(self):
        messagebox.showinfo("Información", "Archivo Analizado con Exito")

    # Función que habilita el botón Analisis
    def habilitar_botonAnalizar(self):
        self.menu.entryconfig(" Analizar ", state=tk.NORMAL)   

    # Función que habilita el botón Reportes
    def habilitar_botonReportes(self):
        self.menu.entryconfig(" Reportes ▼", state=tk.NORMAL) 

app = Ventana()
app.mainloop()