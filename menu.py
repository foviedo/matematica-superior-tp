from tkinter import ttk
from tkinter import *
from newton_gregory import newton_gregory, newton_gregory_regresivo
from lagrange import lagrange


class Menu:
    def __init__(self, window):
        # Initializations
        self.wind = window
        self.wind.title('FINTER')

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text='Ingrese los puntos a interpolar')
        frame.grid(row=0, column=0, columnspan=1, pady=20, padx=20)

        # Creo botones radiales para seleccionar el Metodo
        self.metodoVar = StringVar()
        frame2 = LabelFrame(self.wind, text='Seleccione un método para aproximar')
        frame2.grid(row=0, column=1, columnspan=1, pady=20, padx=20)
        rl = Radiobutton(frame2, text="Lagrange", value='Lagrange', variable=self.metodoVar)
        rl.grid(row=1, column=0, sticky=W)
        rl.select() # Lagrange va a ser el default
        Radiobutton(frame2, text="Newton-Gregory (Progresivo)",
                    value='Newton-Gregory (Progresivo)',
                    variable=self.metodoVar).grid(row=2, column=0, sticky=W)

        Radiobutton(frame2, text="Newton-Gregory (Regresivo)",
                    value='Newton-Gregory (Regresivo)',
                    variable=self.metodoVar).grid(row=3, column=0, sticky=W)

        # X Input
        Label(frame, text='X: ').grid(row=1, column=0)
        self.px = Entry(frame)
        self.px.focus()
        self.px.grid(row=1, column=1)

        # Y Input
        Label(frame, text='Y: ').grid(row=2, column=0)
        self.py = Entry(frame)
        self.py.grid(row=2, column=1)

        # Button Add Product
        ttk.Button(frame, text='Ingresar punto', command = self.add_punto).grid(row=3, columnspan=2, sticky=W+E)

        # Output Messages
        self.message = Label(text='Utilice el punto como signo para separar decimales. ej: 3.141592', fg='grey')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # Table
        self.tree = ttk.Treeview(height=8, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2, sticky=W+E)
        self.tree.heading('#0', text='X', anchor=CENTER)
        self.tree.heading('#1', text='Y', anchor=CENTER)

        # Buttons
        ttk.Button(text='Borrar', command=self.delete_punto).grid(row=5, column=0, sticky=W + E)
        ttk.Button(text='Iniciar', command=self.pcd_iniciar).grid(row=5, column=1, sticky=W + E)


        # Borrar estas lineas luego:
        borrar = [(1, 1), (3, 3), (4, 13), (5, 37), (7, 151)]
        for element in borrar:
            self.tree.insert('', 0, text=str(element[0]), values=str(element[1]))


# User Input Validation
    def validation(self):
        ptoX:str = self.px.get()
        ptoY:str = self.py.get()
        puntos_no_nulos = len(ptoX) != 0 and len(ptoY) != 0
        puntos_son_floats = is_float(ptoX) and is_float(ptoY)
        unicidad = self.verificar_unicidad(ptoX)
        return puntos_no_nulos and puntos_son_floats and unicidad

    def verificar_unicidad(self, ptoX):
        if is_float(ptoX):
            ptoX = float(ptoX)
        else:
            return False

        equis = []
        for item in self.tree.get_children():
            elemento = self.tree.item(item)
            x = float(elemento["text"])
            equis.append(x)

        return ptoX not in equis


    def add_punto(self):
        if self.validation():
            self.tree.insert('', 0, text=self.px.get(), values=self.py.get())
            self.message['fg'] = 'green'
            self.message['text'] = 'Punto ingresado correctamente'
            self.px.delete(0, END)
            self.py.delete(0, END)
            self.px.focus()
        else:
            self.message['fg'] = 'red'
            self.message['text'] = 'No se pudo ingresar el punto'

    def delete_punto(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['fg'] = 'red'
            self.message['text'] = 'Seleccione una fila primero'
            return
        self.message['text'] = ''
        self.tree.delete(self.tree.selection())
        self.message['fg'] = 'green'
        self.message['text'] = 'El punto fue eliminado correctamente'

    def pcd_iniciar(self):
        self.puntos = []
        for item in self.tree.get_children():
            elemento = self.tree.item(item)
            x = float(elemento["text"])
            y = float(elemento["values"][0])
            self.puntos.append((x, y))

        if len(self.puntos) == 0:
            self.message['fg'] = 'red'
            self.message['text'] = 'Debe ingresar al menos un punto'
            return

        self.puntos.sort(key=lambda tup: tup[0])
        self.metodo = self.metodoVar.get()
        print(self.metodo)
        print(self.puntos)
        # self.wind.withdraw()

        self.finter()


    def finter(self):
        ventana = Toplevel(self.wind)

        if(self.metodo == "Lagrange"):
            resultado, pasos = lagrange(*self.puntos)
        elif(self.metodo == "Newton-Gregory (Progresivo)"):
            resultado, pasos = newton_gregory(*self.puntos)
        elif(self.metodo == "Newton-Gregory (Regresivo)"):
            resultado, pasos = newton_gregory_regresivo(*self.puntos)
        self.resultado = resultado

        frame = ttk.LabelFrame(ventana, text="Resolviendo por el método de {}:".format(self.metodo))
        Label(frame, text=pasos, anchor="e").grid(row=0, column=0)

        frameFinal = ttk.LabelFrame(ventana, text="Resultado Final")
        frameFinal.grid(row=0, column=0, columnspan=4, sticky="ew", pady=2)
        ttk.Label(frameFinal, text=resultado).grid(row=0, column=0, sticky="ew")

        frameValor = ttk.LabelFrame(ventana, text="Especializar en valor X")
        frameValor.grid(row=1, column=0, columnspan=2, sticky="ew", pady=2)
        self.entryP = Entry(frameValor)
        self.entryP.grid(row=0, column=1)
        ttk.Button(frameValor, text='Calcular', command = self.calcular_punto).grid(row=0, column=9)

        self.frameEspe = ttk.LabelFrame(ventana, text="Resultado de Especializar")
        self.especializado = Label(self.frameEspe, text='', fg='black')
        self.especializado.grid(row=0, column=0, sticky="ew")



        framePasos = ttk.LabelFrame(ventana, text="Pasos")
        framePasos.grid(row=1, column=2, columnspan=2, sticky="ew")
        ttk.Button(framePasos, text='Mostrar', command= lambda : frame.grid(row=3, column=0, columnspan=4))\
            .grid(row=0, column=0, columnspan=1, sticky="ew")
        ttk.Button(framePasos, text='Ocultar', command = lambda: frame.grid_forget())\
            .grid(row=0, column=1, columnspan=1, sticky="ew")

    def calcular_punto(self):
        #Primero verifico si lo ingresado es valido
        puntos_no_nulos = len(self.entryP.get()) != 0
        puntos_son_floats = is_float(self.entryP.get())
        if not puntos_no_nulos or not puntos_son_floats:
            self.especializado['fg'] = 'red'
            self.especializado['text'] = "\tError: ingrese un numero decimal"
            self.frameEspe.grid(row=2, column=0, columnspan=4, sticky=W+E, pady=2)
            return

        x = float(self.entryP.get())
        ecuacion = self.resultado
        resultado = eval(str(ecuacion))
        self.frameEspe['text'] = "Resultado de especializar el polinomio en {}".format(x)
        self.especializado['fg'] = 'black'
        self.especializado['text'] = '\tP({}) = {}'.format(x, resultado)
        self.frameEspe.grid(row=2, column=0, columnspan=4, sticky=W+E, pady=2)



def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    window = Tk()
    application = Menu(window)
    window.mainloop()
