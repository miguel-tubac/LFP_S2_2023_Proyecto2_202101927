import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename



class ScrollText(tk.Frame):
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
        # Con esta linea activo el text area por si deseo despues desactivarlo:
    def activarTextArea(self):
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

    def desactivarTextArea(self):
        self.text.pack_forget()

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)
    

class ScrollText2(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(
            self,
            bg="#f8f9fa",
            foreground="#343a40",
            insertbackground="#3b5bdb",
            selectbackground="blue",
            width=60,
            height=38,
            font=("Courier New", 10),
        )
        # Con esta linea activo el text area por si deseo despues desactivarlo:
    def activarTextArea(self):
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

    def desactivarTextArea(self):
        self.text.pack_forget()

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

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
        self.menu.add_command(label=" Analizar ")

        self.menu.add_cascade(label=" Reportes ▼", menu=self.filemenu)
        self.filemenu.add_command(label="Rep. Tokens")
        self.filemenu.add_command(label="Rep. Errores")
        self.filemenu.add_command(label="Árbol de derivación")


    def open_file(self):
        filepath = askopenfilename(
            filetypes=[("bizdata Files", "*.bizdata"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        
        # Se almacena la path
        self.path = filepath
        # Se muestra la direcion del archivo en la ventana
        self.title(f"Proyecto 2 - LFP - {filepath}")
        # Mensaje de ingreso de archivo correcto
        self.mostrar_infoIngresoArchivo()


    def mostrar_infoIngresoArchivo(self):
        messagebox.showinfo("Información", "Archivo Ingresado con Exito")

app = Ventana()
app.mainloop()