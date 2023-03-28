import os
import tkinter as tk
from tkinter import messagebox
from analizador_lexico import Analizador
from tkinter.filedialog import askopenfilename, asksaveasfilename
import webbrowser
from Errores.errores import *
from tkinter import Tk
from tkinter import *
import tkinter.filedialog as fd
import tkinter as botones
import webbrowser

class Ventana_principal:
    
    def __init__(self):
        self.analizador = Analizador()
        self.ventana = tk.Tk()
        self.ventana.title("LFP-PROYECTO1-202100096")
        self.ventana.geometry("800x600+0+0")
        self.ventana.geometry("+%d+%d" % ((self.ventana.winfo_screenwidth() - self.ventana.winfo_reqwidth()) / 3, 
                                    (self.ventana.winfo_screenheight() - self.ventana.winfo_reqheight()) / 5.7))
        self.ventana.configure(bg='#EDBB99')
        self.pantalla_1()
        
        
    def pantalla_1(self):
    
        self.Frame = Frame(self.ventana, width=700, height=500, bg="#A3E4D7", highlightthickness=5, highlightbackground="#FF5733", padx=10, pady=10 )
        
        label_titulo = Label(self.Frame, text="202100096 - PROYECTO 1 - LENGUAJE FORMALES B+", font=("Verdana", 16, "bold"), highlightthickness=2, highlightbackground="#7203FF", padx=10, pady=10)
        label_titulo.place(x=10, y=30)
        
        
        Button(self.Frame, text="ABRIR ARCHIVO", command= self.abrir_archivo, font=("Verdana", 13, 'bold'), bg="#1E90FF", fg="#FFFFFF", width=15).place(x=20, y=175)
        
        Button(self.Frame, text="GUARDAR", command= self.guardar_archivo, font=("Verdana", 13, 'bold'), bg="#1E90FF", fg="#FFFFFF", width=15).place(x=20, y=225)
        
        Button(self.Frame, text="GUARDAR COMO", command=self.guardar_como, font=("Verdana", 13, 'bold'), bg="#1E90FF", fg="#FFFFFF", width=15).place(x=20, y=275)
        
        Button(self.Frame, text="ANALIZAR", command= self.analizar,  font=("Verdana", 13, 'bold'), bg="#1E90FF", fg="#FFFFFF", width=15).place(x=20, y=325)
        
        Button(self.Frame, text="ERRORES", command= self.getErrores, font=("Verdana", 13, 'bold'), bg="#1E90FF", fg="#FFFFFF", width=15).place(x=20, y=375)
    
        Button(self.Frame, text="SALIR", command=self.salir, font=("Verdana", 13, 'bold'), bg="#8B0000", fg="#FFFFFF", width=15).place(x=20, y=425)
        
        Button(self.Frame, text="MANUAL DE USUARIO", command=self.manual_usario,  font=("Verdana", 11, 'bold'), bg="#4B0082", fg="#FFFFFF", width=20).place(x=20, y=95)
        
        Button(self.Frame, text="MANUAL TECNICO", command=self.manual_tecnico, font=("Verdana", 11, 'bold'), bg="#4B0082", fg="#FFFFFF", width=20).place(x=255, y=95)
        
        Button(self.Frame, text="AYUDA", command= self.tema_ayuda, font=("Verdana", 11, 'bold'), bg="#8B0000", fg="#FFFFFF", width=15).place(x=490, y=95)
        
        
        self.text = tk.Text(self.Frame)
        self.text.grid(row=1, column=2, rowspan=6, padx=10, pady=10)
        self.text.configure(font=("Verdana", 12),bg="#D2F7CB", fg="#000000",)
        self.text.place(width=400, height=310, x=255, y=150)
        
        

        self.Frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.Frame.mainloop()
        
    def abrir_archivo(self):
        
        try:
            
            filetypes = ( ('TXT', '*'), ('All files', '.'))
            self.fileRoute = askopenfilename( title='SELECCIONE UN ARCHIVO', initialdir='',filetypes=filetypes)

            with open(self.fileRoute, 'r', encoding='latin-1') as file:
                self.text.delete('1.0', tk.END)
                self.text.insert(tk.END, file.read())

        except:
            messagebox.showerror('Error', 'No se ha seleccionado un archivo válido.')

            return


    def guardar_archivo(self):
    
        with open(self.fileRoute, 'w') as file:
                file.write(self.text.get("1.0", tk.END))
                self.fileRoute = self.text.get("1.0",tk.END)
                self.analizador.entrada1(self.fileRoute)
    
    def guardar_como(self):
        
        filetypes = ( ('TXT', '*'), ('All files', '.'))
        ruta_guardado = fd.asksaveasfilename(title='GUARDAR COMO', initialdir='', filetypes=filetypes, defaultextension='.txt')

        if ruta_guardado:
            with open(ruta_guardado, 'w') as file:
                file.write(self.text.get("1.0", tk.END))
                self.fileRoute = ruta_guardado
                self.analizador.entrada1(self.fileRoute)
        else:
            pass
        
    def analizar(self):
        
        instrucciones = self.analizador.operar_()
        dot = 'digraph grafo{\n'
        for instruccion in instrucciones:
            instruccion.operar(None)
        for i in range(len(instrucciones)):
            dot += self.analizador.grafica(i,0,'',instrucciones[i])
        dot += '}'
        
        
        with open('Arbol/RESULTADOS_202100096.txt','w',encoding='utf-8') as report:
            report.write(dot)

        os.system('dot -Tpdf Arbol/RESULTADOS_202100096.txt -o Arbol/RESULTADOS_202100096.pdf')
        webbrowser.open('Arbol\RESULTADOS_202100096.pdf')


    
    
    def getErrores(self):
        
        lista_errores = self.analizador.getErrores()
        contenido = "{\n"
        contador = 1
        while lista_errores:
            error = lista_errores.pop(0)
            contenido += f"\t{{\n\t\t\"No.\":, {contador},\n\t\t\"Descripcion-Token\": {{\n\t\t\t\"Lexema\": \"{error.lexema}\",\n\t\t\t\"Tipo\": \"Error\",\n\t\t\t\"Columna\": {error.columna},\n\t\t\t\"Fila\": {error.fila}\n\t\t}}\n\t}},\n"
            contador += 1
        contenido += "}"
        with open("ERRORES_202100096.txt", "w") as f:
            f.write(contenido)    

        archivo = "ERRORES_202100096.txt"
        os.startfile(archivo)


    def salir(self):
        
            messagebox.showinfo('ADIOS', 'EL PROGRAMA SE CERRARÁ' )
            self.ventana.destroy()
        
    def tema_ayuda(self):
        
        global ventana_ayuda
        global ventana_ayuda
        
        ventana_ayuda = botones.Toplevel()
        ventana_ayuda.title("A Y U D A")
        ventana_ayuda.geometry("700x280")
        ventana_ayuda.configure(bg='#A1AC69')

        ventana_ayuda_ancho = ventana_ayuda.winfo_screenwidth()
        ventana_ayuda_altura = ventana_ayuda.winfo_screenheight()

        pos_x = int((ventana_ayuda_ancho - ventana_ayuda.winfo_reqwidth())/2.7)
        pos_y = int((ventana_ayuda_altura - ventana_ayuda.winfo_reqheight())/3)
    
        ventana_ayuda.geometry("+{}+{}".format(pos_x, pos_y))

        label_titulo = botones.Label(ventana_ayuda, text="TEMA DE AYUDA", font=("Verdana", 16, 'bold'), highlightthickness=2, highlightbackground="#7203FF", padx=10, pady=10)
        label_titulo.pack(pady=10)

        label_datos = botones.Label(ventana_ayuda, text="CREADO POR: 202100096", font=("Verdana", 12, 'bold'), bg="white", highlightthickness=2, highlightbackground="#D500FF", padx=3, pady=3 )
        label_datos.pack(padx=10, pady=10)
    
        label_datos1 = botones.Label(ventana_ayuda, text="RIVER ANDERSON ~ ISMALEJ ROMAN", font=("Verdana", 12, 'bold'), bg="white", highlightthickness=2, highlightbackground="#0008FF", padx=3, pady=3 )
        label_datos1.pack(padx=10, pady=10)
    
        label_datos2 = botones.Label(ventana_ayuda, text="LENGUAJES FORMALES ~ B+", font=("Verdana", 12, 'bold'), bg="white", highlightthickness=2, highlightbackground="#00E8FF", padx=3, pady=3)
        label_datos2.pack(padx=10, pady=10)
    

        boton_regresar = botones.Button(ventana_ayuda, text=" <- REGRESAR", font=("Verdana", 12, 'bold'), bg="#859AEE" ,command=self.regresar_principal)
        boton_regresar.pack()

    def regresar_principal(self):
        
        ventana_ayuda.destroy()
    
    def manual_usario(self):
        
        link = "https://github.com/riverroman/-LFP--PROYECTO1-202100096/blob/main/Manuals/manual_usuario.md"
        webbrowser.open(link)
        
        pass

    def manual_tecnico(self):
        
        link = "https://github.com/riverroman/-LFP--PROYECTO1-202100096/blob/main/Manuals/manual_tecnico.md"
        
        webbrowser.open(link)
    
    
if __name__ == '__main__':
    app = Ventana_principal()
    app.ventana.mainloop()
    
    